"""
tests/e2e/helpers/net_inspector.py
Inspection utilities for Netlify live deployment endpoints, CDN assets, and headers.
"""
import ssl
import urllib.error
import urllib.request
from typing import Any, Dict, Optional

def _get_ssl_context() -> ssl.SSLContext:
    """Returns a standard SSL context with certificate validation."""
    return ssl.create_default_context()

def check_live_endpoint(url: str, expected_status: int = 200, timeout: float = 10.0) -> Dict[str, Any]:
    """Queries live deployment endpoint and returns status code, headers, and body metrics."""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) E2ETestRunner/1.0"}
    )
    ctx = _get_ssl_context()

    try:
        with urllib.request.urlopen(req, context=ctx, timeout=timeout) as resp:
            status = resp.status
            headers = dict(resp.headers)
            body = resp.read().decode("utf-8", errors="ignore")

            server_header = headers.get("Server", headers.get("server", ""))
            cache_header = headers.get("Cache-Control", headers.get("cache-control", ""))
            hsts_header = headers.get("Strict-Transport-Security", headers.get("strict-transport-security", ""))

            return {
                "status": status,
                "is_success": status == expected_status,
                "server": server_header,
                "is_netlify": "Netlify" in server_header or "netlify" in server_header,
                "cache_control": cache_header,
                "has_hsts": bool(hsts_header),
                "has_title": "<title>" in body and "ACIE 2027" in body,
                "has_root_div": 'id="root"' in body,
                "error": None
            }
    except urllib.error.HTTPError as e:
        return {
            "status": e.code,
            "is_success": False,
            "server": e.headers.get("Server", ""),
            "is_netlify": "Netlify" in e.headers.get("Server", ""),
            "cache_control": "",
            "has_hsts": False,
            "has_title": False,
            "has_root_div": False,
            "error": f"HTTPError {e.code}: {e.reason}"
        }
    except Exception as e:
        return {
            "status": 0,
            "is_success": False,
            "server": "",
            "is_netlify": False,
            "cache_control": "",
            "has_hsts": False,
            "has_title": False,
            "has_root_div": False,
            "error": f"Exception: {str(e)}"
        }

def check_live_asset_stream(url: str, min_size: int = 1000, timeout: float = 10.0) -> Dict[str, Any]:
    """Checks live CDN asset for status 200, content-type, and non-empty byte stream."""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) E2ETestRunner/1.0"}
    )
    ctx = _get_ssl_context()

    try:
        with urllib.request.urlopen(req, context=ctx, timeout=timeout) as resp:
            status = resp.status
            content_type = resp.headers.get("Content-Type", "")
            raw_len = resp.headers.get("Content-Length")
            content_length = int(raw_len) if raw_len and raw_len.isdigit() else 0

            # Read head to confirm streamable bytes
            sample_bytes = resp.read(1024)
            is_valid_size = content_length >= min_size or len(sample_bytes) > 0

            return {
                "status": status,
                "is_success": status == 200 and is_valid_size,
                "content_type": content_type,
                "content_length": content_length,
                "sample_header": sample_bytes[:16],
                "error": None
            }
    except Exception as e:
        return {
            "status": 0,
            "is_success": False,
            "content_type": "",
            "content_length": 0,
            "sample_header": b"",
            "error": str(e)
        }
