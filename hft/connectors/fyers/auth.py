"""Fyers OAuth2 authentication helpers."""

import hashlib
from urllib.parse import urlencode

import httpx
import structlog

from hft.connectors.fyers.types import token_decoder
from hft.core.exceptions import ExchangeError

logger = structlog.get_logger(__name__)

FYERS_AUTH_URL = "https://api-t1.fyers.in/api/v3/generate-authcode"
FYERS_TOKEN_URL = "https://api-t1.fyers.in/api/v3/validate-authcode"
FYERS_REFRESH_URL = "https://api-t1.fyers.in/api/v3/validate-refresh-token"


def generate_app_id_hash(app_id: str, secret: str) -> str:
    """
    Generate appIdHash for Fyers API authentication.

    Args:
        app_id: Fyers app ID
        secret: Fyers app secret

    Returns:
        SHA-256 hash of "app_id:secret"
    """
    return hashlib.sha256(f"{app_id}:{secret}".encode()).hexdigest()


def generate_auth_url(
    app_id: str,
    redirect_uri: str,
    state: str = "sample",
) -> str:
    """
    Generate OAuth2 authorization URL for user login.

    User must visit this URL, login, and get the auth_code from redirect.

    Args:
        app_id: Fyers app ID
        redirect_uri: Redirect URI registered with Fyers
        state: State parameter for CSRF protection

    Returns:
        Authorization URL for user to visit
    """
    params = {
        "client_id": app_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "state": state,
    }
    return f"{FYERS_AUTH_URL}?{urlencode(params)}"


async def get_access_token(
    app_id: str,
    secret: str,
    auth_code: str,
) -> str:
    """
    Exchange auth_code for access_token.

    Args:
        app_id: Fyers app ID
        secret: Fyers app secret
        auth_code: Authorization code from redirect

    Returns:
        Access token for API calls

    Raises:
        ExchangeError: If authentication fails
    """
    app_id_hash = generate_app_id_hash(app_id, secret)

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                FYERS_TOKEN_URL,
                json={
                    "grant_type": "authorization_code",
                    "appIdHash": app_id_hash,
                    "code": auth_code,
                },
            )
            response.raise_for_status()

            data = token_decoder.decode(response.content)

            if data.s != "ok":
                raise ExchangeError(
                    f"Fyers auth failed: {data.message}",
                    code=data.code or -1,
                )

            if not data.access_token:
                raise ExchangeError("No access token in response", code=-1)

            logger.info("fyers_auth_success", app_id=app_id)
            return data.access_token

        except httpx.HTTPStatusError as e:
            logger.error(
                "fyers_auth_http_error",
                status=e.response.status_code,
                body=e.response.text[:500],
            )
            raise ExchangeError(
                f"Fyers auth HTTP error: {e.response.status_code}",
                code=e.response.status_code,
            ) from e


async def refresh_access_token(
    app_id: str,
    secret: str,
    refresh_token: str,
    pin: str,
) -> str:
    """
    Refresh access token using refresh token.

    Note: Refresh token has 15-day validity.

    Args:
        app_id: Fyers app ID
        secret: Fyers app secret
        refresh_token: Refresh token from previous auth
        pin: User's Fyers PIN (required for token refresh)

    Returns:
        New access token

    Raises:
        ExchangeError: If refresh fails
    """
    app_id_hash = generate_app_id_hash(app_id, secret)

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                FYERS_REFRESH_URL,  # Use correct refresh endpoint
                json={
                    "grant_type": "refresh_token",
                    "appIdHash": app_id_hash,
                    "refresh_token": refresh_token,
                    "pin": pin,  # Required for refresh
                },
            )
            response.raise_for_status()

            data = token_decoder.decode(response.content)

            if data.s != "ok":
                raise ExchangeError(
                    f"Fyers token refresh failed: {data.message}",
                    code=data.code or -1,
                )

            if not data.access_token:
                raise ExchangeError("No access token in refresh response", code=-1)

            logger.info("fyers_token_refreshed", app_id=app_id)
            return data.access_token

        except httpx.HTTPStatusError as e:
            logger.error(
                "fyers_refresh_http_error",
                status=e.response.status_code,
            )
            raise ExchangeError(
                f"Fyers refresh HTTP error: {e.response.status_code}",
                code=e.response.status_code,
            ) from e
