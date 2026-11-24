from datetime import datetime, timezone
import time
import requests
from src.models import EndpointResult

def check_endpoint(url: str) -> EndpointResult:
    """Checks the availability and response time for a given endpoint URL."""
    timestamp = datetime.now(timezone.utc).isoformat()
    start = time.perf_counter()

    try: 
        response = requests.get(url, timeout=5)
        response_time = (time.perf_counter() - start) * 1000  # Convert to milliseconds
        status_code = response.status_code
        is_up = response.ok

    except requests.RequestException:
        response_time = None
        status_code = None
        is_up = False

    return EndpointResult(
        timestamp=timestamp,
        url=url,
        response_time=response_time,
        status_code=status_code,
        is_up=is_up
    )