#!/usr/bin/env python3
"""
Fyers OAuth2 Authentication Helper

Run this script to get your Fyers access token:
    uv run python scripts/fyers_auth.py

Then copy the access token to your .env file.
"""

import asyncio
import webbrowser
from urllib.parse import parse_qs, urlparse

from nanoedge.connectors.fyers.auth import generate_auth_url, get_access_token
from nanoedge.config import settings


def main():
    print("\n" + "=" * 60)
    print("FYERS OAuth2 Authentication")
    print("=" * 60)

    app_id = settings.fyers_app_id
    secret = settings.fyers_secret
    redirect_uri = settings.fyers_redirect_uri

    if not app_id or not secret:
        print("\n❌ Error: FYERS credentials not found in .env")
        print("   Set NANOEDGE_FYERS_APP_ID and NANOEDGE_FYERS_SECRET")
        return

    print(f"\nApp ID: {app_id}")
    print(f"Redirect URI: {redirect_uri}")

    # Step 1: Generate auth URL
    auth_url = generate_auth_url(app_id, redirect_uri)

    print("\n" + "-" * 60)
    print("STEP 1: Open this URL in your browser and login to Fyers:")
    print("-" * 60)
    print(f"\n{auth_url}\n")

    # Try to open browser automatically
    try:
        webbrowser.open(auth_url)
        print("(Browser opened automatically)")
    except Exception:
        print("(Please copy the URL above and open it manually)")

    # Step 2: Get the redirect URL from user
    print("\n" + "-" * 60)
    print("STEP 2: After login, Fyers will redirect you to:")
    print(f"        {redirect_uri}?auth_code=XXXXX&state=sample")
    print("-" * 60)
    print("\nPaste the FULL redirect URL here (or just the auth_code):")

    user_input = input("> ").strip()

    # Extract auth_code
    if "auth_code=" in user_input:
        # Parse from full URL
        parsed = urlparse(user_input)
        params = parse_qs(parsed.query)
        auth_code = params.get("auth_code", [None])[0]
    else:
        # Assume they pasted just the code
        auth_code = user_input

    if not auth_code:
        print("\n❌ Error: Could not extract auth_code")
        return

    print(f"\nAuth code: {auth_code[:20]}...")

    # Step 3: Exchange for access token
    print("\n" + "-" * 60)
    print("STEP 3: Exchanging auth_code for access_token...")
    print("-" * 60)

    try:
        access_token = asyncio.run(get_access_token(app_id, secret, auth_code))

        print("\n✅ SUCCESS! Access token obtained.")
        print("\n" + "=" * 60)
        print("Add this to your .env file:")
        print("=" * 60)
        print(f"\nNANOEDGE_FYERS_ACCESS_TOKEN={access_token}\n")

        # Also print just the token for easy copy
        print("-" * 60)
        print("Access Token (copy this):")
        print("-" * 60)
        print(f"\n{access_token}\n")

    except Exception as e:
        print(f"\n❌ Error getting access token: {e}")
        print("\nMake sure:")
        print("  1. The auth_code is fresh (they expire quickly)")
        print("  2. Your app credentials are correct")
        print("  3. The redirect_uri matches what's registered with Fyers")


if __name__ == "__main__":
    main()
