from incident_review import Incident, create_incident_labels, build_severity_updates, find_highest_severity_incident, \
    sort_incidents, get_open_incident_titles, build_incident_index, get_all_tags, has_urgent_open_incident, \
    are_all_incidents_resolved, get_top_urgent_incident_titles
import pytest


# ① enumerate + unpacking：先把最基础的捡回来
def test_create_incident_labels() -> None:
    incident1 = Incident(201, "Login failure", 5, "open", "Alice", ["auth", "urgent"])
    incident2 = Incident(202, "Export timeout", 3, "open", "Bob", ["export", "performance"])
    incident3 = Incident(203, "Password reset", 2, "resolved", "Alice", ["auth"])
    incident4 = Incident(204, "Payment error", 5, "open", None, ["payment", "urgent"])
    incident5 = Incident(205, "Dashboard lag", 3, "resolved", "Cara", ["performance"])

    incidents = [incident1, incident2, incident3, incident4, incident5]

    result = create_incident_labels(incidents)

    assert result == [
                        "1. #201 Login failure",
                        "2. #202 Export timeout",
                        "3. #203 Password reset",
                        "4. #204 Payment error",
                        "5. #205 Dashboard lag",
                     ]


def test_create_incident_labels_empty() -> None:
    incidents = []

    result = create_incident_labels(incidents)

    assert result == []


# ② zip：重点回忆 silent truncation
def test_build_severity_updates() -> None:
    incident_ids = [201, 202, 203]
    severities = [5, 4, 2]

    result = build_severity_updates(incident_ids, severities)

    assert result == {
                        201: 5,
                        202: 4,
                        203: 2,
                     }


def test_build_severity_updates_both_empty() -> None:
    incident_ids = []
    severities = []

    result = build_severity_updates(incident_ids, severities)

    assert result == {}


def test_build_severity_different_length() -> None:
    incident_ids = [201, 202, 203]
    severities = [5, 4]

    with pytest.raises(ValueError):
        build_severity_updates(incident_ids, severities)


# ③ max / sorted + key：这是今天最值得重新练的一块
def test_find_highest_severity_incident() -> None:
    incident1 = Incident(201, "Login failure", 5, "open", "Alice", ["auth", "urgent"])
    incident2 = Incident(202, "Export timeout", 3, "open", "Bob", ["export", "performance"])
    incident3 = Incident(203, "Password reset", 2, "resolved", "Alice", ["auth"])
    incident4 = Incident(204, "Payment error", 5, "open", None, ["payment", "urgent"])
    incident5 = Incident(205, "Dashboard lag", 3, "resolved", "Cara", ["performance"])

    incidents = [incident1, incident2, incident3, incident4, incident5]

    result = find_highest_severity_incident(incidents)

    assert result is incident1
    assert incidents == [incident1, incident2, incident3, incident4, incident5]


def test_find_highest_severity_incident_empty() -> None:
    incidents = []

    result = find_highest_severity_incident(incidents)

    assert result is None


def test_sort_incidents() -> None:
    incident1 = Incident(201, "Login failure", 5, "open", "Alice", ["auth", "urgent"])
    incident2 = Incident(202, "Export timeout", 3, "open", "Bob", ["export", "performance"])
    incident3 = Incident(203, "Password reset", 2, "resolved", "Alice", ["auth"])
    incident4 = Incident(204, "Payment error", 5, "open", None, ["payment", "urgent"])
    incident5 = Incident(205, "Dashboard lag", 3, "resolved", "Cara", ["performance"])

    incidents = [incident1, incident2, incident3, incident4, incident5]

    result = sort_incidents(incidents)

    assert result == [incident1, incident4, incident2, incident5, incident3]


def test_sort_incidents_empty() -> None:
    incidents = []

    result = sort_incidents(incidents)

    assert result == []


# ④ Comprehension：不要为了短而短
def test_get_open_incident_titles() -> None:
    incident1 = Incident(201, "Login failure", 5, "open", "Alice", ["auth", "urgent"])
    incident2 = Incident(202, "Export timeout", 3, "open", "Bob", ["export", "performance"])
    incident3 = Incident(203, "Password reset", 2, "resolved", "Alice", ["auth"])
    incident4 = Incident(204, "Payment error", 5, "open", None, ["payment", "urgent"])
    incident5 = Incident(205, "Dashboard lag", 3, "resolved", "Cara", ["performance"])

    incidents = [incident1, incident2, incident3, incident4, incident5]

    result = get_open_incident_titles(incidents)

    assert result == [
                        "Login failure",
                        "Export timeout",
                        "Payment error",
                     ]


def test_get_open_incident_titles_no_open() -> None:
    incident1 = Incident(201, "Login failure", 5, "resolved", "Alice", ["auth", "urgent"])
    incident2 = Incident(202, "Export timeout", 3, "resolved", "Bob", ["export", "performance"])
    incident3 = Incident(203, "Password reset", 2, "resolved", "Alice", ["auth"])
    incident4 = Incident(204, "Payment error", 5, "resolved", None, ["payment", "urgent"])
    incident5 = Incident(205, "Dashboard lag", 3, "resolved", "Cara", ["performance"])

    incidents = [incident1, incident2, incident3, incident4, incident5]

    result = get_open_incident_titles(incidents)

    assert result == []


def test_get_open_incident_titles_empty() -> None:
    incidents = []

    result = get_open_incident_titles(incidents)

    assert result == []


def test_build_incident_index() -> None:
    incident1 = Incident(201, "Login failure", 5, "open", "Alice", ["auth", "urgent"])
    incident2 = Incident(202, "Export timeout", 3, "open", "Bob", ["export", "performance"])
    incident3 = Incident(203, "Password reset", 2, "resolved", "Alice", ["auth"])
    incident4 = Incident(204, "Payment error", 5, "open", None, ["payment", "urgent"])
    incident5 = Incident(205, "Dashboard lag", 3, "resolved", "Cara", ["performance"])

    incidents = [incident1, incident2, incident3, incident4, incident5]

    result = build_incident_index(incidents)

    assert result[201] is incident1


def test_build_incident_index_repetition() -> None:
    incident1 = Incident(201, "Login failure", 5, "open", "Alice", ["auth", "urgent"])
    incident2 = Incident(201, "Export timeout", 3, "open", "Bob", ["export", "performance"])
    incident3 = Incident(203, "Password reset", 2, "resolved", "Alice", ["auth"])
    incident4 = Incident(204, "Payment error", 5, "open", None, ["payment", "urgent"])
    incident5 = Incident(205, "Dashboard lag", 3, "resolved", "Cara", ["performance"])

    incidents = [incident1, incident2, incident3, incident4, incident5]

    result = build_incident_index(incidents)

    assert result[201] is incident2  # 第一个被覆盖了，保留的是第二个
    assert len(result) == 4


# ⑤ set comprehension：重新练一次两层遍历
def test_get_all_tags() -> None:
    incident1 = Incident(201, "Login failure", 5, "open", "Alice", ["auth", "urgent"])
    incident2 = Incident(202, "Export timeout", 3, "open", "Bob", ["export", "performance"])
    incident3 = Incident(203, "Password reset", 2, "resolved", "Alice", ["auth"])
    incident4 = Incident(204, "Payment error", 5, "open", None, ["payment", "urgent"])
    incident5 = Incident(205, "Dashboard lag", 3, "resolved", "Cara", ["performance"])

    incidents = [incident1, incident2, incident3, incident4, incident5]

    result = get_all_tags(incidents)

    assert result == {
                        "auth",
                        "urgent",
                        "export",
                        "performance",
                        "payment",
                     }


def test_get_all_tags_empty() -> None:
    incidents = []

    result = get_all_tags(incidents)

    assert result == set()  # set()和{}是不同的


# ⑥ any / all：重点是 Python 默认行为 ≠ 业务规则
def test_has_urgent_open_incident() -> None:
    incident1 = Incident(201, "Login failure", 5, "open", "Alice", ["auth", "urgent"])
    incident2 = Incident(202, "Export timeout", 3, "open", "Bob", ["export", "performance"])
    incident3 = Incident(203, "Password reset", 2, "resolved", "Alice", ["auth"])
    incident4 = Incident(204, "Payment error", 5, "open", None, ["payment", "urgent"])
    incident5 = Incident(205, "Dashboard lag", 3, "resolved", "Cara", ["performance"])

    incidents = [incident1, incident2, incident3, incident4, incident5]

    result = has_urgent_open_incident(incidents)

    assert result is True


def test_has_urgent_open_incident_false() -> None:
    incident1 = Incident(201, "Login failure", 5, "open", "Alice", ["auth"])
    incident2 = Incident(202, "Export timeout", 3, "open", "Bob", ["export", "performance"])
    incident3 = Incident(203, "Password reset", 2, "resolved", "Alice", ["auth"])
    incident4 = Incident(204, "Payment error", 5, "resolved", None, ["payment", "urgent"])
    incident5 = Incident(205, "Dashboard lag", 3, "resolved", "Cara", ["performance"])

    incidents = [incident1, incident2, incident3, incident4, incident5]

    result = has_urgent_open_incident(incidents)

    assert result is False


def test_has_urgent_open_incident_empty() -> None:
    incidents = []

    result = has_urgent_open_incident(incidents)

    assert result is False


def test_are_all_incidents_resolved() -> None:
    incident1 = Incident(201, "Login failure", 5, "open", "Alice", ["auth", "urgent"])
    incident2 = Incident(202, "Export timeout", 3, "open", "Bob", ["export", "performance"])
    incident3 = Incident(203, "Password reset", 2, "resolved", "Alice", ["auth"])
    incident4 = Incident(204, "Payment error", 5, "open", None, ["payment", "urgent"])
    incident5 = Incident(205, "Dashboard lag", 3, "resolved", "Cara", ["performance"])

    incidents = [incident1, incident2, incident3, incident4, incident5]

    result = are_all_incidents_resolved(incidents)

    assert result is False


def test_are_all_incidents_resolved_true() -> None:
    incident1 = Incident(201, "Login failure", 5, "resolved", "Alice", ["auth", "urgent"])
    incident2 = Incident(202, "Export timeout", 3, "resolved", "Bob", ["export", "performance"])
    incident3 = Incident(203, "Password reset", 2, "resolved", "Alice", ["auth"])
    incident4 = Incident(204, "Payment error", 5, "resolved", None, ["payment", "urgent"])
    incident5 = Incident(205, "Dashboard lag", 3, "resolved", "Cara", ["performance"])

    incidents = [incident1, incident2, incident3, incident4, incident5]

    result = are_all_incidents_resolved(incidents)

    assert result is True


def test_are_all_incidents_resolved_empty() -> None:
    incidents = []

    result = are_all_incidents_resolved(incidents)

    assert result is False


# 最后的综合题
def test_get_top_urgent_incident_titles() -> None:
    incident1 = Incident(201, "Login failure", 4, "open", "Alice", ["auth", "urgent"])
    incident2 = Incident(202, "Export timeout", 3, "open", "Bob", ["export", "performance"])
    incident3 = Incident(203, "Password reset", 2, "resolved", "Alice", ["auth"])
    incident4 = Incident(204, "Payment error", 5, "open", None, ["payment", "urgent"])
    incident5 = Incident(205, "Dashboard lag", 3, "resolved", "Cara", ["performance"])

    incidents = [incident1, incident2, incident3, incident4, incident5]

    result = get_top_urgent_incident_titles(incidents, 2)

    assert result == [
                        "Payment error",
                        "Login failure",
                     ]
# 现有测试没有真正验证“severity 高的排前面”。当前两个 urgent open incident的severity是一样的，所以应该修改一下severity再测


def test_get_top_urgent_incident_titles_limit_1() -> None:
    incident1 = Incident(201, "Login failure", 5, "open", "Alice", ["auth", "urgent"])
    incident2 = Incident(202, "Export timeout", 3, "open", "Bob", ["export", "performance"])
    incident3 = Incident(203, "Password reset", 2, "resolved", "Alice", ["auth"])
    incident4 = Incident(204, "Payment error", 5, "open", None, ["payment", "urgent"])
    incident5 = Incident(205, "Dashboard lag", 3, "resolved", "Cara", ["performance"])

    incidents = [incident1, incident2, incident3, incident4, incident5]

    result = get_top_urgent_incident_titles(incidents, 1)

    assert result == [
                        "Login failure",
                     ]


def test_get_top_urgent_incident_titles_limit_0() -> None:
    incident1 = Incident(201, "Login failure", 5, "open", "Alice", ["auth", "urgent"])
    incident2 = Incident(202, "Export timeout", 3, "open", "Bob", ["export", "performance"])
    incident3 = Incident(203, "Password reset", 2, "resolved", "Alice", ["auth"])
    incident4 = Incident(204, "Payment error", 5, "open", None, ["payment", "urgent"])
    incident5 = Incident(205, "Dashboard lag", 3, "resolved", "Cara", ["performance"])

    incidents = [incident1, incident2, incident3, incident4, incident5]

    result = get_top_urgent_incident_titles(incidents, 0)

    assert result == []


def test_get_top_urgent_incident_titles_limit_negative() -> None:
    incident1 = Incident(201, "Login failure", 5, "open", "Alice", ["auth", "urgent"])
    incident2 = Incident(202, "Export timeout", 3, "open", "Bob", ["export", "performance"])
    incident3 = Incident(203, "Password reset", 2, "resolved", "Alice", ["auth"])
    incident4 = Incident(204, "Payment error", 5, "open", None, ["payment", "urgent"])
    incident5 = Incident(205, "Dashboard lag", 3, "resolved", "Cara", ["performance"])

    incidents = [incident1, incident2, incident3, incident4, incident5]

    result = get_top_urgent_incident_titles(incidents, -1)

    assert result == []


def test_get_top_urgent_incident_titles_no_urgent_open_incident() -> None:
    incident1 = Incident(201, "Login failure", 5, "open", "Alice", ["auth"])
    incident2 = Incident(202, "Export timeout", 3, "open", "Bob", ["export", "performance"])
    incident3 = Incident(203, "Password reset", 2, "resolved", "Alice", ["auth"])
    incident4 = Incident(204, "Payment error", 5, "resolved", None, ["payment", "urgent"])
    incident5 = Incident(205, "Dashboard lag", 3, "resolved", "Cara", ["performance"])

    incidents = [incident1, incident2, incident3, incident4, incident5]

    result = get_top_urgent_incident_titles(incidents, 2)

    assert result == []


def test_get_top_urgent_incident_titles_empty() -> None:
    incidents = []

    result = get_top_urgent_incident_titles(incidents, 2)

    assert result == []
