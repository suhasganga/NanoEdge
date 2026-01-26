"""Generate latency profile report from running HFT server.

Usage:
    1. Start the server: uv run python main.py
    2. Open browser to http://localhost:8000 (generate traffic)
    3. Run this script: uv run python scripts/latency_report.py

The script will collect metrics for 60 seconds then generate a report.
"""

import asyncio
import sys

try:
    import httpx
except ImportError:
    print("Error: httpx not installed. Run: uv add httpx")
    sys.exit(1)


# Performance targets (microseconds)
TARGETS = {
    "parse_json": {
        "p99": 1000,  # <1ms
        "name": "JSON Parse",
        "description": "msgspec decode time",
    },
    "api_ws_push": {
        "p99": 10000,  # <10ms
        "name": "WebSocket Push",
        "description": "send_bytes() latency",
    },
    "orderbook_update": {
        "p99": 100,  # <100µs
        "name": "Order Book Update",
        "description": "Apply depth diff",
    },
    "ws_network": {
        "p99": 200000,  # <200ms (network latency to exchange)
        "name": "Network Latency",
        "description": "Exchange → receive",
    },
}


async def fetch_metrics(base_url: str) -> dict | None:
    """Fetch metrics from the server."""
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.get(f"{base_url}/api/metrics")
            resp.raise_for_status()
            return resp.json()
    except httpx.ConnectError:
        print(f"Error: Cannot connect to {base_url}")
        print("Make sure the HFT server is running: uv run python main.py")
        return None
    except Exception as e:
        print(f"Error fetching metrics: {e}")
        return None


def print_report(metrics: dict) -> None:
    """Print formatted latency report."""
    print()
    print("=" * 70)
    print("HFT Platform Latency Report")
    print("=" * 70)
    print()

    # Print all metrics
    print("LATENCY METRICS (microseconds)")
    print("-" * 70)

    for name, data in metrics.items():
        count = data.get("count", 0)
        if count > 0:
            print(f"\n  {name}:")
            print(f"    Samples:  {count:>12,}")
            print(f"    p50:      {data.get('p50_us', 0):>12.1f} µs")
            print(f"    p95:      {data.get('p95_us', 0):>12.1f} µs")
            print(f"    p99:      {data.get('p99_us', 0):>12.1f} µs")
            print(f"    mean:     {data.get('mean_us', 0):>12.1f} µs")
            print(f"    min:      {data.get('min_us', 0):>12.1f} µs")
            print(f"    max:      {data.get('max_us', 0):>12.1f} µs")

    print()
    print("=" * 70)

    # Performance vs targets
    print("\nPERFORMANCE vs TARGETS")
    print("-" * 70)

    all_pass = True
    for key, target in TARGETS.items():
        if key in metrics and metrics[key].get("count", 0) > 0:
            p99 = metrics[key].get("p99_us", 0)
            target_p99 = target["p99"]
            passed = p99 < target_p99
            status = "PASS" if passed else "FAIL"
            symbol = "✓" if passed else "✗"

            if not passed:
                all_pass = False

            print(
                f"  {symbol} {target['name']:<20} "
                f"p99={p99:>10.1f}µs  "
                f"(target <{target_p99}µs)  "
                f"[{status}]"
            )
        else:
            print(f"  - {target['name']:<20} No data")

    print()
    print("=" * 70)

    # Summary
    if all_pass:
        print("\n  Overall: All targets met!")
    else:
        print("\n  Overall: Some targets not met - review results above")

    print()


async def main() -> None:
    """Main entry point."""
    base_url = "http://localhost:8000"
    wait_time = 60

    print("=" * 70)
    print("HFT Platform Latency Report Generator")
    print("=" * 70)
    print()

    # First check if server is running
    print("Checking server connection...")
    initial = await fetch_metrics(base_url)
    if initial is None:
        sys.exit(1)

    initial_count = sum(m.get("count", 0) for m in initial.values())
    print(f"Connected! Current sample count: {initial_count:,}")
    print()

    # Option 1: Quick report (if we already have data)
    if initial_count > 1000:
        print("Sufficient data available. Generating report now...")
        print_report(initial)
        return

    # Option 2: Wait for data collection
    print(f"Collecting metrics for {wait_time} seconds...")
    print("Make sure the frontend is open at http://localhost:8000 to generate traffic.")
    print()

    # Show progress
    for i in range(wait_time):
        remaining = wait_time - i
        print(f"\r  Waiting... {remaining:2d}s remaining", end="", flush=True)
        await asyncio.sleep(1)

    print("\r" + " " * 40 + "\r", end="")  # Clear line

    # Fetch final metrics
    print("Fetching final metrics...")
    metrics = await fetch_metrics(base_url)

    if metrics is None:
        print("Failed to fetch metrics after waiting.")
        sys.exit(1)

    final_count = sum(m.get("count", 0) for m in metrics.values())
    new_samples = final_count - initial_count
    print(f"Collected {new_samples:,} new samples")

    if new_samples < 100:
        print()
        print("Warning: Low sample count. Results may not be accurate.")
        print("Make sure the frontend is generating WebSocket traffic.")
        print()

    # Print report
    print_report(metrics)


if __name__ == "__main__":
    asyncio.run(main())
