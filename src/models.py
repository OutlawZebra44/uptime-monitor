from dataclasses import dataclass

@dataclass
class SystemMetric:
    timestamp: str
    cpu_percent: float
    memory_percent: float
    disk_percent: float

@dataclass
class EndpointResult:
    timestamp: str
    url: str
    status_code: int | None
    response_time: float | None
    is_up: bool