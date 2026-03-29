"""Application configuration using pydantic-settings."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings with environment variable support."""

    # Fyers (NSE/India)
    fyers_app_id: str = ""
    fyers_secret: str = ""
    fyers_access_token: str = ""  # OAuth2 access token (from login flow)
    fyers_redirect_uri: str = "http://localhost:8000/fyers/callback"
    fyers_ws_url: str = "wss://api-t1.fyers.in/feed/data-ws"
    fyers_rest_url: str = "https://api-t1.fyers.in"

    # Binance
    binance_api_key: str = ""
    binance_secret: str = ""
    binance_ws_url: str = "wss://stream.binance.com:9443"
    binance_futures_ws_url: str = "wss://fstream.binance.com"
    binance_coin_ws_url: str = "wss://dstream.binance.com"
    binance_rest_url: str = "https://api.binance.com"
    binance_futures_rest_url: str = "https://fapi.binance.com"
    binance_coin_rest_url: str = "https://dapi.binance.com"

    # QuestDB
    questdb_host: str = "localhost"
    questdb_ilp_port: int = 9009
    questdb_http_port: int = 9000

    # API Server
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    # Default symbols to track (for backward compatibility)
    symbols: list[str] = ["BTCUSDT", "ETHUSDT"]

    # Ring buffer size (ticks per symbol)
    ring_buffer_capacity: int = 1_000_000

    # Symbol refresh settings
    symbol_refresh_on_startup: bool = True
    symbol_db_path: str = "nanoedge/data/symbols.db"

    # Subscription settings
    max_cached_symbols: int = 5  # Number of symbols to keep in LRU cache

    # Auto-backfill settings
    auto_backfill_on_startup: bool = True  # Backfill all symbols on server start
    startup_backfill_days: int = 7  # Lookback for finding symbols with data
    backfill_on_symbol_switch: bool = True  # Backfill when user switches symbols
    symbol_switch_backfill_hours: int = 24  # How far back to check on switch

    model_config = {"env_file": ".env", "env_prefix": "NANOEDGE_"}


# Global settings instance
settings = Settings()
