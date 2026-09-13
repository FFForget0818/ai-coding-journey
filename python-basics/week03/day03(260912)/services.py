# 第二块：datetime / timedelta —— application 里的时间
from models import Incident, IncidentStatus
from exceptions import IncidentNotFoundError, InvalidIncidentOperationError
from datetime import datetime, timedelta


def find_incident(
    incidents: list[Incident],
    incident_id: int
) -> Incident | None:
    if len(incidents) == 0:
        return None
    for incident in incidents:
        if incident.incident_id == incident_id:
            return incident
    return None


def resolve_incident(
    incidents: list[Incident],
    incident_id: int
) -> Incident:
    wanna_find_incident = find_incident(incidents, incident_id)
    if wanna_find_incident is None:
        raise IncidentNotFoundError("Can not find the Incident!")
    if wanna_find_incident.status == IncidentStatus.RESOLVED:
        raise InvalidIncidentOperationError("The Incident is already solved!")
    wanna_find_incident.status = IncidentStatus.RESOLVED
    wanna_find_incident.resolved_at = datetime.now()
    return wanna_find_incident


def get_recent_incidents(
    incidents: list[Incident],
    days: int
) -> list[Incident]:
    if days <= 0:
        raise ValueError("Days must be higher than 0!")
    return [
        incident  # 这里一开始写成Incident了，其实应该是写incident
        for incident in incidents
        if incident.created_at >= datetime.now() - timedelta(days=days)  # 时间不能直接加减，要用timedelta
    ]
