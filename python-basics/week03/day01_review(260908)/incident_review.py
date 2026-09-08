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


# ③ max / sorted + key：这是今天最值得重新练的一块
def find_highest_severity_incident(
    incidents: list[Incident]
) -> Incident | None:
    if len(incidents) == 0:
        return None
    return max(incidents, key=lambda incident: incident.severity)  # 这个我忘记了
    # key=lambda其实就是在获取这些incident的severity，相当于是提供了一个规则。然后通过max(incidents, key=……)才是获得最大值的部分


def sort_incidents(
    incidents: list[Incident]
) -> list[Incident]:
    return sorted(incidents, key=lambda incident: (-incident.severity, incident.incident_id))


# ④ Comprehension：不要为了短而短
def get_open_incident_titles(
    incidents: list[Incident]
) -> list[str]:
    return [
        incident.title
        for incident in incidents
        if incident.status == "open"
    ]


def build_incident_index(
    incidents: list[Incident]
) -> dict[int, Incident]:
    return {
        incident.incident_id: incident
        for incident in incidents
    }


# ⑤ set comprehension：重新练一次两层遍历
def get_all_tags(
    incidents: list[Incident]
) -> set[str]:
    return {
        tag
        for incident in incidents
        for tag in incident.tags
    }  # 这个不太记得了，为什么直接是去重的？
# set 这个数据结构本身就不允许重复元素


# ⑥ any / all：重点是 Python 默认行为 ≠ 业务规则
def has_urgent_open_incident(
    incidents: list[Incident]
) -> bool:
    return any(
        incident.status == "open" and "urgent" in incident.tags
        for incident in incidents
    )  # 这个也不咋记得了


def are_all_incidents_resolved(
    incidents: list[Incident]
) -> bool:
    if len(incidents) == 0:
        return False
    return all(
        incident.status == "resolved"
        for incident in incidents
    )


# 最后的综合题
def get_top_urgent_incident_titles(
    incidents: list[Incident],
    limit: int
) -> list[str]:
    new_incidents = [
        incident
        for incident in incidents
        if incident.status == "open" and "urgent" in incident.tags
    ]
    sorted_incidents = sorted(
        new_incidents, key=lambda incident: (-incident.severity, incident.incident_id)
    )
    return [
        incident.title
        for index, incident in enumerate(sorted_incidents)
        if index < limit
    ]
# 在第一次测试的时候报错，发现都没有用new_incidents、sorted_incidents，而是用的原始的incidents
# 不建议写：for index, incident in enumerate(sorted_incidents)，而是：
# if limit <= 0:
#     return []
#
# return [
#     incident.title
#     for incident in sorted_incidents[:limit]
# ]