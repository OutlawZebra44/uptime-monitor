from src.config import load_config
from src.system_checks import collect_system_metrics
from src.endpoint_checks import check_endpoint


def run_once() -> None:
    config = load_config()
    metrics = collect_system_metrics()
    print(f"SYSTEM | CPU: {metrics.cpu_percent}% | RAM: {metrics.memory_percent}% | Disk: {metrics.disk_percent}%")

    for url in config["endpoints"]:
        result = check_endpoint(url)
        status = "UP" if result.is_up else "DOWN"
        print(f"ENDPOINT | {status} ({result.status_code}) | {result.response_time} ms | {result.url}")


if __name__ == "__main__":
    run_once()