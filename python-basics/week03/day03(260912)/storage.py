# 第三块：pathlib + JSON Persistence
from models import Incident, IncidentStatus


# 这是最初写的一个版本，不太优雅
# def incident_to_dict(
#     incident: Incident
# ) -> dict:
#     if incident.status is IncidentStatus.OPEN:
#         status = "open"
#     elif incident.status is IncidentStatus.INVESTIGATING:
#         status = "investigating"
#     else:
#         status = "resolved"
#     if incident.resolved_at is None:
#         resolved = None
#     else:
#         resolved = incident.resolved_at.isoformat()
#     return {
#         "incident_id": incident.incident_id,
#         "title": incident.title,
#         "severity": incident.severity,
#         "created_at": incident.created_at.isoformat(),  # ISO是一种特定的时间格式
#         "resolved_at": resolved,
#         "status": status
#     }


def incident_to_dict(
    incident: Incident
) -> dict:
    return {
        "incident_id": incident.incident_id,
        "title": incident.title,
        "severity": incident.severity,
        "created_at": incident.created_at.isoformat(),  # ISO是一种特定的时间格式
        "resolved_at": (
            incident.resolved_at.isoformat()
            if incident.resolved_at is not None
            else None
        ),  # 居然还有这种条件表达式
        "status": incident.status.value  # 这里直接.value就行了
    }