"""Symbol-related type definitions and filter helpers."""

from hft.core.types import InstrumentType

# Filter presets for UI
FILTER_PRESETS = {
    "all": None,  # No filter
    "spot": [InstrumentType.SPOT.value],
    "futures": [
        InstrumentType.PERP_LINEAR.value,
        InstrumentType.PERP_INVERSE.value,
        InstrumentType.FUTURE_LINEAR.value,
        InstrumentType.FUTURE_INVERSE.value,
        InstrumentType.EQUITY_FUTURE.value,
        InstrumentType.INDEX_FUTURE.value,
        InstrumentType.CURRENCY_FUTURE.value,
        InstrumentType.COMMODITY_FUTURE.value,
    ],
    "options": [
        InstrumentType.OPTION_CALL.value,
        InstrumentType.OPTION_PUT.value,
        InstrumentType.EQUITY_OPTION_CE.value,
        InstrumentType.EQUITY_OPTION_PE.value,
        InstrumentType.INDEX_OPTION_CE.value,
        InstrumentType.INDEX_OPTION_PE.value,
        InstrumentType.CURRENCY_OPTION_CE.value,
        InstrumentType.CURRENCY_OPTION_PE.value,
        InstrumentType.COMMODITY_OPTION_CE.value,
        InstrumentType.COMMODITY_OPTION_PE.value,
    ],
    "stocks": [InstrumentType.EQUITY.value],
    "index_fo": [
        InstrumentType.INDEX.value,
        InstrumentType.INDEX_FUTURE.value,
        InstrumentType.INDEX_OPTION_CE.value,
        InstrumentType.INDEX_OPTION_PE.value,
    ],
    "equity_fo": [
        InstrumentType.EQUITY.value,
        InstrumentType.EQUITY_FUTURE.value,
        InstrumentType.EQUITY_OPTION_CE.value,
        InstrumentType.EQUITY_OPTION_PE.value,
    ],
    "currency": [
        InstrumentType.CURRENCY_FUTURE.value,
        InstrumentType.CURRENCY_OPTION_CE.value,
        InstrumentType.CURRENCY_OPTION_PE.value,
    ],
    "commodity": [
        InstrumentType.COMMODITY_FUTURE.value,
        InstrumentType.COMMODITY_OPTION_CE.value,
        InstrumentType.COMMODITY_OPTION_PE.value,
    ],
}


def get_filter_types(filter_name: str) -> list[str] | None:
    """
    Get instrument types for a filter preset.

    Args:
        filter_name: Filter name ("all", "spot", "futures", etc.)

    Returns:
        List of instrument types or None for no filter
    """
    return FILTER_PRESETS.get(filter_name.lower())


def parse_filter_string(filter_str: str) -> list[str]:
    """
    Parse comma-separated filter string into list of types.

    Args:
        filter_str: "spot,perp_linear,equity" or "futures"

    Returns:
        List of instrument type strings
    """
    if not filter_str:
        return []

    # Check if it's a preset
    preset = get_filter_types(filter_str)
    if preset is not None:
        return preset

    # Parse as comma-separated types
    return [t.strip() for t in filter_str.split(",") if t.strip()]
