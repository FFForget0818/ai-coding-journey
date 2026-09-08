from incident_review import Incident, create_incident_labels, build_severity_updates
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