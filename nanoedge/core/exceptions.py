"""Custom exceptions for the HFT platform."""


class HFTError(Exception):
    """Base exception for all HFT platform errors."""

    pass


class ConnectionError(HFTError):
    """WebSocket or REST API connection failed."""

    pass


class OrderBookError(HFTError):
    """Order book state is inconsistent or invalid."""

    pass


class DataGapError(HFTError):
    """Missing data detected in the stream."""

    pass


class ConfigurationError(HFTError):
    """Invalid or missing configuration."""

    pass


class ExchangeError(HFTError):
    """Error returned by the exchange API."""

    def __init__(self, message: str, code: int | None = None):
        super().__init__(message)
        self.code = code
