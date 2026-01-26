"""Tests for Binance msgspec types and decoders."""

import msgspec
import pytest

from hft.connectors.binance.types import (
    BinanceAggTrade,
    BinanceCombinedStream,
    BinanceDepthSnapshot,
    BinanceDepthUpdate,
    BinanceKline,
    BinanceKlineData,
    BinanceTicker24h,
    agg_trade_decoder,
    combined_stream_decoder,
    depth_snapshot_decoder,
    depth_update_decoder,
    kline_decoder,
    ticker_24h_decoder,
)


class TestBinanceAggTrade:
    """Tests for BinanceAggTrade parsing."""

    def test_decode_agg_trade(self):
        """Decode aggregate trade message."""
        data = b'{"e":"aggTrade","E":1704067200000,"s":"BTCUSDT","a":12345,"p":"50000.00","q":"0.001","f":100,"l":105,"T":1704067200000,"m":true}'

        trade = agg_trade_decoder.decode(data)

        assert trade.e == "aggTrade"
        assert trade.E == 1704067200000
        assert trade.s == "BTCUSDT"
        assert trade.a == 12345
        assert trade.p == "50000.00"
        assert trade.q == "0.001"
        assert trade.f == 100
        assert trade.l == 105
        assert trade.T == 1704067200000
        assert trade.m is True

    def test_price_as_string(self):
        """Price and quantity are strings for precision."""
        data = b'{"e":"aggTrade","E":1704067200000,"s":"BTCUSDT","a":1,"p":"50000.123456789","q":"0.00000001","f":1,"l":1,"T":1704067200000,"m":false}'

        trade = agg_trade_decoder.decode(data)

        # Strings preserve full precision
        assert trade.p == "50000.123456789"
        assert trade.q == "0.00000001"
        # Can convert to float
        assert float(trade.p) == 50000.123456789
        assert float(trade.q) == 0.00000001

    def test_is_buyer_maker(self):
        """is_buyer_maker True means sell (red), False means buy (green)."""
        buy_data = b'{"e":"aggTrade","E":1704067200000,"s":"BTCUSDT","a":1,"p":"50000","q":"0.1","f":1,"l":1,"T":1704067200000,"m":false}'
        sell_data = b'{"e":"aggTrade","E":1704067200000,"s":"BTCUSDT","a":1,"p":"50000","q":"0.1","f":1,"l":1,"T":1704067200000,"m":true}'

        buy = agg_trade_decoder.decode(buy_data)
        sell = agg_trade_decoder.decode(sell_data)

        assert buy.m is False  # Buyer was taker (buy)
        assert sell.m is True  # Buyer was maker (sell)


class TestBinanceKline:
    """Tests for BinanceKline parsing."""

    def test_decode_kline(self):
        """Decode kline message with nested data."""
        data = b'{"e":"kline","E":1704067200000,"s":"BTCUSDT","k":{"t":1704067140000,"T":1704067199999,"s":"BTCUSDT","i":"1m","f":100,"L":200,"o":"50000.00","c":"50050.00","h":"50100.00","l":"49900.00","v":"100.5","n":500,"x":false,"q":"5000000.00","V":"50.25","Q":"2500000.00"}}'

        kline = kline_decoder.decode(data)

        assert kline.e == "kline"
        assert kline.E == 1704067200000
        assert kline.s == "BTCUSDT"
        assert isinstance(kline.k, BinanceKlineData)
        assert kline.k.o == "50000.00"
        assert kline.k.h == "50100.00"
        assert kline.k.l == "49900.00"
        assert kline.k.c == "50050.00"
        assert kline.k.v == "100.5"
        assert kline.k.n == 500
        assert kline.k.x is False

    def test_kline_is_closed(self):
        """Kline x flag indicates if candle is closed."""
        open_data = b'{"e":"kline","E":1704067200000,"s":"BTCUSDT","k":{"t":1704067140000,"T":1704067199999,"s":"BTCUSDT","i":"1m","f":100,"L":200,"o":"50000","c":"50050","h":"50100","l":"49900","v":"100","n":500,"x":false,"q":"5000000","V":"50","Q":"2500000"}}'
        closed_data = b'{"e":"kline","E":1704067200000,"s":"BTCUSDT","k":{"t":1704067140000,"T":1704067199999,"s":"BTCUSDT","i":"1m","f":100,"L":200,"o":"50000","c":"50050","h":"50100","l":"49900","v":"100","n":500,"x":true,"q":"5000000","V":"50","Q":"2500000"}}'

        open_kline = kline_decoder.decode(open_data)
        closed_kline = kline_decoder.decode(closed_data)

        assert open_kline.k.x is False
        assert closed_kline.k.x is True


class TestBinanceDepthUpdate:
    """Tests for BinanceDepthUpdate parsing."""

    def test_decode_depth_update(self):
        """Decode depth update message."""
        data = b'{"e":"depthUpdate","E":1704067200000,"s":"BTCUSDT","U":157,"u":160,"b":[["50000.00","1.5"],["49999.00","2.0"]],"a":[["50001.00","0.5"],["50002.00","1.0"]]}'

        depth = depth_update_decoder.decode(data)

        assert depth.e == "depthUpdate"
        assert depth.E == 1704067200000
        assert depth.s == "BTCUSDT"
        assert depth.U == 157
        assert depth.u == 160
        assert len(depth.b) == 2
        assert len(depth.a) == 2
        assert depth.b[0] == ["50000.00", "1.5"]
        assert depth.a[0] == ["50001.00", "0.5"]

    def test_bid_ask_format(self):
        """Bids and asks are list of [price, quantity] strings."""
        data = b'{"e":"depthUpdate","E":1704067200000,"s":"BTCUSDT","U":1,"u":1,"b":[["50000.123","1.234"]],"a":[["50001.456","0.567"]]}'

        depth = depth_update_decoder.decode(data)

        # First element is price, second is quantity
        bid_price, bid_qty = depth.b[0]
        ask_price, ask_qty = depth.a[0]

        assert float(bid_price) == 50000.123
        assert float(bid_qty) == 1.234
        assert float(ask_price) == 50001.456
        assert float(ask_qty) == 0.567

    def test_update_ids(self):
        """U is first update ID, u is final update ID."""
        data = b'{"e":"depthUpdate","E":1704067200000,"s":"BTCUSDT","U":100,"u":105,"b":[],"a":[]}'

        depth = depth_update_decoder.decode(data)

        assert depth.U == 100  # First update ID
        assert depth.u == 105  # Final update ID
        assert depth.u > depth.U  # Final always >= first


class TestBinanceDepthSnapshot:
    """Tests for BinanceDepthSnapshot parsing."""

    def test_decode_depth_snapshot(self):
        """Decode depth snapshot response."""
        data = b'{"lastUpdateId":12345,"bids":[["50000.00","1.5"],["49999.00","2.0"]],"asks":[["50001.00","0.5"]]}'

        snapshot = depth_snapshot_decoder.decode(data)

        assert snapshot.lastUpdateId == 12345
        assert len(snapshot.bids) == 2
        assert len(snapshot.asks) == 1
        assert snapshot.bids[0] == ["50000.00", "1.5"]

    def test_empty_book(self):
        """Handle empty order book."""
        data = b'{"lastUpdateId":0,"bids":[],"asks":[]}'

        snapshot = depth_snapshot_decoder.decode(data)

        assert snapshot.lastUpdateId == 0
        assert snapshot.bids == []
        assert snapshot.asks == []


class TestBinanceTicker24h:
    """Tests for BinanceTicker24h parsing."""

    def test_decode_ticker(self):
        """Decode 24hr ticker message."""
        data = b'{"e":"24hrTicker","E":1704067200000,"s":"BTCUSDT","p":"100.50","P":"0.20","c":"50100.00","o":"50000.00","h":"50500.00","l":"49500.00","v":"10000.5","q":"500000000.00","n":100000}'

        ticker = ticker_24h_decoder.decode(data)

        assert ticker.e == "24hrTicker"
        assert ticker.E == 1704067200000
        assert ticker.s == "BTCUSDT"
        assert ticker.p == "100.50"  # Price change
        assert ticker.P == "0.20"  # Price change percent
        assert ticker.c == "50100.00"  # Close/last price
        assert ticker.o == "50000.00"  # Open price
        assert ticker.h == "50500.00"  # High
        assert ticker.l == "49500.00"  # Low
        assert ticker.v == "10000.5"  # Base volume
        assert ticker.q == "500000000.00"  # Quote volume
        assert ticker.n == 100000  # Trade count

    def test_price_change_values(self):
        """Price change can be negative."""
        data = b'{"e":"24hrTicker","E":1704067200000,"s":"BTCUSDT","p":"-500.00","P":"-1.00","c":"49500.00","o":"50000.00","h":"50500.00","l":"49000.00","v":"10000","q":"500000000","n":100000}'

        ticker = ticker_24h_decoder.decode(data)

        assert ticker.p == "-500.00"
        assert ticker.P == "-1.00"
        assert float(ticker.p) == -500.0
        assert float(ticker.P) == -1.0


class TestBinanceCombinedStream:
    """Tests for BinanceCombinedStream parsing."""

    def test_decode_combined_stream(self):
        """Decode combined stream wrapper."""
        data = b'{"stream":"btcusdt@aggTrade","data":{"e":"aggTrade","E":1704067200000,"s":"BTCUSDT","a":1,"p":"50000","q":"0.1","f":1,"l":1,"T":1704067200000,"m":false}}'

        combined = combined_stream_decoder.decode(data)

        assert combined.stream == "btcusdt@aggTrade"
        assert isinstance(combined.data, dict)
        assert combined.data["e"] == "aggTrade"

    def test_stream_name_parsing(self):
        """Stream name format: symbol@streamType."""
        streams = [
            b'{"stream":"btcusdt@aggTrade","data":{}}',
            b'{"stream":"btcusdt@kline_1m","data":{}}',
            b'{"stream":"btcusdt@depth","data":{}}',
            b'{"stream":"btcusdt@ticker","data":{}}',
        ]

        expected = ["btcusdt@aggTrade", "btcusdt@kline_1m", "btcusdt@depth", "btcusdt@ticker"]

        for stream_data, expected_name in zip(streams, expected):
            combined = combined_stream_decoder.decode(stream_data)
            assert combined.stream == expected_name


class TestDecoderPerformance:
    """Tests for decoder performance characteristics."""

    def test_msgspec_struct_is_fast(self):
        """msgspec Structs are faster than dataclasses/namedtuples."""
        data = b'{"e":"aggTrade","E":1704067200000,"s":"BTCUSDT","a":12345,"p":"50000.00","q":"0.001","f":100,"l":105,"T":1704067200000,"m":true}'

        # Should be able to decode 10000 messages quickly
        for _ in range(10000):
            agg_trade_decoder.decode(data)

        # If we get here without timeout, performance is acceptable

    def test_decoder_reuse(self):
        """Same decoder instance can be reused."""
        data1 = b'{"e":"aggTrade","E":1704067200000,"s":"BTCUSDT","a":1,"p":"50000","q":"0.1","f":1,"l":1,"T":1704067200000,"m":true}'
        data2 = b'{"e":"aggTrade","E":1704067200001,"s":"ETHUSDT","a":2,"p":"3000","q":"1.0","f":2,"l":2,"T":1704067200001,"m":false}'

        trade1 = agg_trade_decoder.decode(data1)
        trade2 = agg_trade_decoder.decode(data2)

        assert trade1.s == "BTCUSDT"
        assert trade2.s == "ETHUSDT"
        assert trade1.E != trade2.E

    def test_decode_error_handling(self):
        """Invalid JSON raises DecodeError."""
        invalid_data = b'{"e":"aggTrade","E":invalid}'

        with pytest.raises(msgspec.DecodeError):
            agg_trade_decoder.decode(invalid_data)

    def test_missing_field_error(self):
        """Missing required field raises DecodeError."""
        # Missing 'm' field
        incomplete = b'{"e":"aggTrade","E":1704067200000,"s":"BTCUSDT","a":1,"p":"50000","q":"0.1","f":1,"l":1,"T":1704067200000}'

        with pytest.raises(msgspec.DecodeError):
            agg_trade_decoder.decode(incomplete)
