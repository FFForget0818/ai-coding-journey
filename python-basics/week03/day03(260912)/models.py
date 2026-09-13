# 第一块：Enum —— 不再到处手写状态字符串
from enum import Enum
from dataclasses import dataclass
from datetime import datetime


class IncidentStatus(Enum):
    OPEN = "open"
    INVESTIGATING = "investigating"
    RESOLVED = "resolved"


@dataclass
class Incident:
    incident_id: int
    title: str
    severity: int
    created_at: datetime
    resolved_at: datetime | None = None
    status: IncidentStatus = IncidentStatus.OPEN

    def __post_init__(self) -> None:
        if self.incident_id <= 0:
            raise ValueError("Incident_id must > 0!")

        if self.title.strip() == "":
            raise ValueError("Title must not be empty!")

        if self.severity < 1 or self.severity > 5:
            raise ValueError("Severity must between 1 and 5!")

