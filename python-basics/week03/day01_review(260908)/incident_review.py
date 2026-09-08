from dataclasses import dataclass


@dataclass
class Incident:
    incident_id: int
    title: str
    severity: int
    status: str
    owner: str | None
    tags: list[str]


# ① enumerate + unpacking：先把最基础的捡回来
def create_incident_labels(
    incidents: list[Incident]
) -> list[str]:
    result = []
    for index, incident in enumerate(incidents, start=1):
        result.append(f'{index}. #{incident.incident_id} {incident.title}')
    return result


# ② zip：重点回忆 silent truncation
def build_severity_updates(
    incident_ids: list[int],
    severities: list[int]
) -> dict[int, int]:
    if len(incident_ids) != len(severities):
        raise ValueError('incident_ids and severities must have the same length')
    result = {}
    for incident_id, severity in zip(incident_ids, severities):
        result[incident_id] = severity
    return result