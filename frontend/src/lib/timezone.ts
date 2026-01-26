/**
 * Timezone utilities for chart and trade display.
 *
 * Uses native Intl.DateTimeFormat API - zero external dependencies.
 * IANA timezone database is built into browsers.
 */

// Timezone entry structure
export interface TimezoneEntry {
  id: string; // IANA format: "America/New_York"
  label: string; // Display: "New York"
  offset: string; // Display offset: "UTC-5"
  region: string; // Grouping: "Americas"
}

// Special timezone options
export const TIMEZONE_SPECIAL = {
  UTC: "UTC",
  EXCHANGE: "EXCHANGE",
} as const;

// Common timezones list (~50 entries)
export const TIMEZONE_LIST: TimezoneEntry[] = [
  // Americas
  { id: "Pacific/Honolulu", label: "Honolulu", offset: "UTC-10", region: "Americas" },
  { id: "America/Anchorage", label: "Anchorage", offset: "UTC-9", region: "Americas" },
  { id: "America/Los_Angeles", label: "Los Angeles", offset: "UTC-8", region: "Americas" },
  { id: "America/Denver", label: "Denver", offset: "UTC-7", region: "Americas" },
  { id: "America/Phoenix", label: "Phoenix", offset: "UTC-7", region: "Americas" },
  { id: "America/Chicago", label: "Chicago", offset: "UTC-6", region: "Americas" },
  { id: "America/Mexico_City", label: "Mexico City", offset: "UTC-6", region: "Americas" },
  { id: "America/New_York", label: "New York", offset: "UTC-5", region: "Americas" },
  { id: "America/Toronto", label: "Toronto", offset: "UTC-5", region: "Americas" },
  { id: "America/Bogota", label: "Bogota", offset: "UTC-5", region: "Americas" },
  { id: "America/Caracas", label: "Caracas", offset: "UTC-4", region: "Americas" },
  { id: "America/Santiago", label: "Santiago", offset: "UTC-3", region: "Americas" },
  { id: "America/Sao_Paulo", label: "Sao Paulo", offset: "UTC-3", region: "Americas" },
  { id: "America/Buenos_Aires", label: "Buenos Aires", offset: "UTC-3", region: "Americas" },

  // Europe
  { id: "Atlantic/Reykjavik", label: "Reykjavik", offset: "UTC+0", region: "Europe" },
  { id: "Europe/London", label: "London", offset: "UTC+0", region: "Europe" },
  { id: "Europe/Dublin", label: "Dublin", offset: "UTC+0", region: "Europe" },
  { id: "Europe/Lisbon", label: "Lisbon", offset: "UTC+0", region: "Europe" },
  { id: "Europe/Paris", label: "Paris", offset: "UTC+1", region: "Europe" },
  { id: "Europe/Berlin", label: "Berlin", offset: "UTC+1", region: "Europe" },
  { id: "Europe/Amsterdam", label: "Amsterdam", offset: "UTC+1", region: "Europe" },
  { id: "Europe/Zurich", label: "Zurich", offset: "UTC+1", region: "Europe" },
  { id: "Europe/Madrid", label: "Madrid", offset: "UTC+1", region: "Europe" },
  { id: "Europe/Rome", label: "Rome", offset: "UTC+1", region: "Europe" },
  { id: "Europe/Warsaw", label: "Warsaw", offset: "UTC+1", region: "Europe" },
  { id: "Europe/Athens", label: "Athens", offset: "UTC+2", region: "Europe" },
  { id: "Europe/Helsinki", label: "Helsinki", offset: "UTC+2", region: "Europe" },
  { id: "Europe/Kyiv", label: "Kyiv", offset: "UTC+2", region: "Europe" },
  { id: "Europe/Istanbul", label: "Istanbul", offset: "UTC+3", region: "Europe" },
  { id: "Europe/Moscow", label: "Moscow", offset: "UTC+3", region: "Europe" },

  // Africa & Middle East
  { id: "Africa/Cairo", label: "Cairo", offset: "UTC+2", region: "Africa & Middle East" },
  { id: "Africa/Johannesburg", label: "Johannesburg", offset: "UTC+2", region: "Africa & Middle East" },
  { id: "Asia/Jerusalem", label: "Jerusalem", offset: "UTC+2", region: "Africa & Middle East" },
  { id: "Asia/Dubai", label: "Dubai", offset: "UTC+4", region: "Africa & Middle East" },
  { id: "Asia/Riyadh", label: "Riyadh", offset: "UTC+3", region: "Africa & Middle East" },

  // Asia
  { id: "Asia/Karachi", label: "Karachi", offset: "UTC+5", region: "Asia" },
  { id: "Asia/Kolkata", label: "Mumbai / Kolkata", offset: "UTC+5:30", region: "Asia" },
  { id: "Asia/Dhaka", label: "Dhaka", offset: "UTC+6", region: "Asia" },
  { id: "Asia/Bangkok", label: "Bangkok", offset: "UTC+7", region: "Asia" },
  { id: "Asia/Jakarta", label: "Jakarta", offset: "UTC+7", region: "Asia" },
  { id: "Asia/Ho_Chi_Minh", label: "Ho Chi Minh", offset: "UTC+7", region: "Asia" },
  { id: "Asia/Singapore", label: "Singapore", offset: "UTC+8", region: "Asia" },
  { id: "Asia/Hong_Kong", label: "Hong Kong", offset: "UTC+8", region: "Asia" },
  { id: "Asia/Shanghai", label: "Shanghai", offset: "UTC+8", region: "Asia" },
  { id: "Asia/Taipei", label: "Taipei", offset: "UTC+8", region: "Asia" },
  { id: "Asia/Manila", label: "Manila", offset: "UTC+8", region: "Asia" },
  { id: "Asia/Seoul", label: "Seoul", offset: "UTC+9", region: "Asia" },
  { id: "Asia/Tokyo", label: "Tokyo", offset: "UTC+9", region: "Asia" },

  // Pacific
  { id: "Australia/Perth", label: "Perth", offset: "UTC+8", region: "Pacific" },
  { id: "Australia/Adelaide", label: "Adelaide", offset: "UTC+9:30", region: "Pacific" },
  { id: "Australia/Sydney", label: "Sydney", offset: "UTC+10", region: "Pacific" },
  { id: "Australia/Brisbane", label: "Brisbane", offset: "UTC+10", region: "Pacific" },
  { id: "Pacific/Auckland", label: "Auckland", offset: "UTC+12", region: "Pacific" },
];

/**
 * Get exchange timezone from symbol.
 * NSE/BSE symbols use IST, everything else uses UTC.
 */
export function getExchangeTimezone(symbol: string): string {
  if (symbol.startsWith("NSE:") || symbol.startsWith("BSE:")) {
    return "Asia/Kolkata";
  }
  return "UTC"; // Default for crypto
}

/**
 * Resolve "EXCHANGE" to actual timezone based on symbol.
 */
export function resolveTimezone(timezone: string, symbol: string): string {
  if (timezone === "EXCHANGE") {
    return getExchangeTimezone(symbol);
  }
  return timezone;
}

/**
 * Transform UTC timestamp to appear in target timezone.
 *
 * TradingView Lightweight Charts processes all timestamps as UTC.
 * To display in a different timezone, we adjust the timestamp value
 * so that when the chart interprets it as UTC, it shows the correct
 * local time for the target timezone.
 *
 * @param utcTimeSeconds - Original UTC timestamp in seconds
 * @param timezone - Target IANA timezone (e.g., "America/New_York")
 * @returns Adjusted timestamp in seconds
 */
export function timeToTz(utcTimeSeconds: number, timezone: string): number {
  if (timezone === "UTC") {
    return utcTimeSeconds;
  }

  // Get the date in target timezone
  const date = new Date(utcTimeSeconds * 1000);

  // Format in target timezone and parse back
  // This gives us what the clock would show in that timezone
  const tzString = date.toLocaleString("en-US", {
    timeZone: timezone,
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    hour12: false,
  });

  // Parse the formatted string back to a Date
  // Format: "MM/DD/YYYY, HH:MM:SS"
  const [datePart, timePart] = tzString.split(", ");
  const [month, day, year] = datePart.split("/").map(Number);
  const [hour, minute, second] = timePart.split(":").map(Number);

  // Create a new date treating these values as UTC
  // This is the "fake UTC" timestamp that will display correctly
  const fakeUtc = Date.UTC(year, month - 1, day, hour, minute, second);

  return Math.floor(fakeUtc / 1000);
}

/**
 * Format timestamp in specified timezone.
 * Used for tooltip/legend display (not chart data).
 *
 * @param timestampSeconds - Timestamp in seconds
 * @param timezone - IANA timezone ID
 * @param format - Output format
 */
export function formatInTimezone(
  timestampSeconds: number,
  timezone: string,
  format: "date" | "time" | "datetime"
): string {
  const date = new Date(timestampSeconds * 1000);

  if (format === "date") {
    return date.toLocaleDateString("en-GB", {
      timeZone: timezone,
      day: "2-digit",
      month: "2-digit",
      year: "numeric",
    });
  }

  if (format === "time") {
    return date.toLocaleTimeString("en-GB", {
      timeZone: timezone,
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
    });
  }

  // datetime
  return date.toLocaleString("en-GB", {
    timeZone: timezone,
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  });
}

/**
 * Get current UTC offset string for display (e.g., "UTC-5", "UTC+5:30").
 * Uses current date to account for DST.
 */
export function getTimezoneOffsetLabel(timezone: string): string {
  if (timezone === "UTC") {
    return "UTC";
  }

  const date = new Date();
  const formatter = new Intl.DateTimeFormat("en-US", {
    timeZone: timezone,
    timeZoneName: "shortOffset",
  });

  const parts = formatter.formatToParts(date);
  const offsetPart = parts.find((p) => p.type === "timeZoneName");

  if (offsetPart?.value) {
    // Convert "GMT-5" to "UTC-5"
    return offsetPart.value.replace("GMT", "UTC");
  }

  return timezone;
}

/**
 * Get current time in timezone (for clock display in header).
 */
export function getCurrentTimeInTimezone(timezone: string): string {
  return new Date().toLocaleTimeString("en-GB", {
    timeZone: timezone,
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  });
}

/**
 * Get timezone label for display in selector.
 * Returns city name for regular timezones, or special label for UTC/EXCHANGE.
 */
export function getTimezoneLabel(timezone: string, symbol?: string): string {
  if (timezone === "UTC") {
    return "UTC";
  }

  if (timezone === "EXCHANGE") {
    const resolved = symbol ? getExchangeTimezone(symbol) : "UTC";
    const entry = TIMEZONE_LIST.find((tz) => tz.id === resolved);
    return `Exchange (${entry?.label || resolved})`;
  }

  const entry = TIMEZONE_LIST.find((tz) => tz.id === timezone);
  return entry?.label || timezone;
}

/**
 * Get unique regions from timezone list for grouping in selector.
 */
export function getTimezoneRegions(): string[] {
  const regions = new Set(TIMEZONE_LIST.map((tz) => tz.region));
  return Array.from(regions);
}

/**
 * Filter timezone list by search query.
 * Matches against label, id, and offset.
 */
export function filterTimezones(query: string): TimezoneEntry[] {
  if (!query.trim()) {
    return TIMEZONE_LIST;
  }

  const lowerQuery = query.toLowerCase();
  return TIMEZONE_LIST.filter(
    (tz) =>
      tz.label.toLowerCase().includes(lowerQuery) ||
      tz.id.toLowerCase().includes(lowerQuery) ||
      tz.offset.toLowerCase().includes(lowerQuery)
  );
}

/**
 * Parse UTC offset string to numeric hours for sorting.
 * e.g., "UTC-5" → -5, "UTC+5:30" → 5.5, "UTC+0" → 0
 */
function parseOffsetHours(offset: string): number {
  const match = offset.match(/UTC([+-])(\d+)(?::(\d+))?/);
  if (!match) return 0;

  const sign = match[1] === "-" ? -1 : 1;
  const hours = parseInt(match[2], 10);
  const minutes = match[3] ? parseInt(match[3], 10) / 60 : 0;

  return sign * (hours + minutes);
}

/**
 * Get timezone list sorted by UTC offset (TradingView style).
 * Most negative (UTC-10) first, most positive (UTC+12) last.
 */
export function getTimezonesSortedByOffset(): TimezoneEntry[] {
  return [...TIMEZONE_LIST].sort((a, b) => {
    const offsetA = parseOffsetHours(a.offset);
    const offsetB = parseOffsetHours(b.offset);
    if (offsetA !== offsetB) return offsetA - offsetB;
    // Same offset: sort alphabetically by label
    return a.label.localeCompare(b.label);
  });
}
