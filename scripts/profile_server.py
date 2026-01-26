"""Profile the HFT server under load using py-spy.

Usage:
    1. Start the server: uv run python main.py
    2. Find PID in Task Manager (Windows) or: pgrep -f "python main.py"
    3. Run py-spy:
       - Flame graph: py-spy record -o profile.svg --pid <PID> -d 60
       - Live view:   py-spy top --pid <PID>
    4. Open profile.svg in browser to analyze

What to look for:
    - Functions taking >5% CPU time in hot path
    - Unexpected allocations (__new__, list, dict in traces)
    - GC activity (gc.collect calls)
    - JSON encoding time (should be minimal with msgspec)
"""

import os
import subprocess
import sys


def main() -> None:
    """Print profiling instructions and optionally start server."""
    print("=" * 60)
    print("HFT Server Profiling Guide")
    print("=" * 60)
    print()

    print("STEP 1: Install py-spy (if not already installed)")
    print("-" * 60)
    print("  pip install py-spy")
    print("  # Or: uv add --dev py-spy")
    print()

    print("STEP 2: Start the HFT server")
    print("-" * 60)
    print("  uv run python main.py")
    print()

    print("STEP 3: Find the server PID")
    print("-" * 60)
    if sys.platform == "win32":
        print("  Windows: Open Task Manager -> Details -> find python.exe")
        print("  Or use PowerShell: Get-Process python | Select-Object Id,ProcessName")
    else:
        print("  Linux/Mac: pgrep -f 'python main.py'")
    print()

    print("STEP 4: Run py-spy profiler")
    print("-" * 60)
    print("  Option A - Record flame graph (60 seconds):")
    print("    py-spy record -o profile.svg --pid <PID> -d 60")
    print()
    print("  Option B - Live top-style view:")
    print("    py-spy top --pid <PID>")
    print()
    print("  Option C - Record with subprocesses:")
    print("    py-spy record -o profile.svg --pid <PID> -d 60 --subprocesses")
    print()

    print("STEP 5: Generate load")
    print("-" * 60)
    print("  - Open http://localhost:8000 in browser")
    print("  - Let the chart update for ~60 seconds")
    print("  - Switch symbols to test subscription handling")
    print()

    print("STEP 6: Analyze results")
    print("-" * 60)
    print("  - Open profile.svg in a web browser")
    print("  - Look for wide bars (high CPU time)")
    print("  - Check for unexpected allocations")
    print()

    print("=" * 60)
    print()

    # Ask if user wants to start server
    response = input("Start the server now? [y/N]: ").strip().lower()
    if response == "y":
        print()
        print("Starting server... (Ctrl+C to stop)")
        print()
        # Change to project root
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        os.chdir(project_root)
        subprocess.run([sys.executable, "main.py"])


if __name__ == "__main__":
    main()
