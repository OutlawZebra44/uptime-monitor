from datetime import datetime, timezone
import psutil
from src.models import SystemMetric


def collect_system_metrics() -> SystemMetric:
    """ Collects system metrics such as CPU, memory, and disk usage."""
    timestamp = datetime.now(timezone.utc).isoformat()
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent

    return SystemMetric(
        timestamp=timestamp,
        cpu_percent=cpu_percent,
        memory_percent=memory_percent,
        disk_percent=disk_percent
    )



if __name__ == "__main__":
    metrics = collect_system_metrics()
    print(f"[{metrics.timestamp}] CPU: {metrics.cpu_percent}% | RAM: {metrics.memory_percent}% | Disk: {metrics.disk_percent}%")
