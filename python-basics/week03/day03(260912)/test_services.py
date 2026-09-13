from models import IncidentStatus, Incident
import pytest
from services import find_incident, resolve_incident, get_recent_incidents
from exceptions import IncidentNotFoundError, InvalidIncidentOperationError
from datetime import datetime, timedelta


def test_incident___post_init___normal() -> None:
    incident1 = Incident(
        incident_id=1,
        title="Payment service unavailable",
        severity=3,
        created_at=datetime(2026, 9, 13, 9, 30)
    )

    assert incident1.incident_id == 1
    assert incident1.title == "Payment service unavailable"
    assert incident1.severity == 3


def test_incident___post_init___incident_id_zero() -> None:
    with pytest.raises(ValueError):
        Incident(
                    incident_id=0,
                    title="Payment service unavailable",
                    severity=5,
                    created_at=datetime(2026, 9, 13, 9, 30)
                )


def test_incident___post_init___incident_id_negative() -> None:
    with pytest.raises(ValueError):
        Incident(
                    incident_id=-1,
                    title="Payment service unavailable",
                    severity=5,
                    created_at=datetime(2026, 9, 13, 9, 30)
                )


def test_incident___post_init___title_empty() -> None:
    with pytest.raises(ValueError):
        Incident(
                    incident_id=1,
                    title="",
                    severity=5,
                    created_at=datetime(2026, 9, 13, 9, 30)
                )


def test_incident___post_init___title_space() -> None:
    with pytest.raises(ValueError):
        Incident(
                    incident_id=1,
                    title="   ",
                    severity=5,
                    created_at=datetime(2026, 9, 13, 9, 30)
                )


def test_incident___post_init___severity_negative() -> None:
    with pytest.raises(ValueError):
        Incident(
                    incident_id=1,
                    title="Payment service unavailable",
                    severity=-1,
                    created_at=datetime(2026, 9, 13, 9, 30)
                )


def test_incident___post_init___severity_below() -> None:
    with pytest.raises(ValueError):
        Incident(
                    incident_id=1,
                    title="Payment service unavailable",
                    severity=0,
                    created_at=datetime(2026, 9, 13, 9, 30)
                )


def test_incident___post_init___severity_lower_line() -> None:
    incident1 = Incident(
        incident_id=1,
        title="Payment service unavailable",
        severity=1,
        created_at=datetime(2026, 9, 13, 9, 30)
    )

    assert incident1.severity == 1


def test_incident___post_init___severity_upper_line() -> None:
    incident1 = Incident(
        incident_id=1,
        title="Payment service unavailable",
        severity=5,
        created_at=datetime(2026, 9, 13, 9, 30)
    )

    assert incident1.severity == 5


def test_incident___post_init___severity_above() -> None:
    with pytest.raises(ValueError):
        Incident(
                    incident_id=1,
                    title="Payment service unavailable",
                    severity=6,
                    created_at=datetime(2026, 9, 13, 9, 30)
                )


# 第二块：datetime / timedelta —— application 里的时间
def test_find_incident() -> None:
    incident1 = Incident(
        incident_id=1,
        title="Payment service unavailable",
        severity=5,
        created_at=datetime(2026, 9, 13, 9, 30)
    )

    incident2 = Incident(
        incident_id=2,
        title="Login response is slow",
        severity=3,
        created_at=datetime(2026, 9, 12, 14, 20),
        status=IncidentStatus.INVESTIGATING
    )

    incident3 = Incident(
        incident_id=3,
        title="Internal dashboard error",
        severity=2,
        created_at=datetime(2026, 9, 10, 11, 0),
        resolved_at=datetime(2026, 9, 10, 13, 30),
        status=IncidentStatus.RESOLVED
    )

    incident4 = Incident(
        incident_id=4,
        title="Database connection timeout",
        severity=4,
        created_at=datetime(2026, 9, 8, 18, 45)
    )

    incident5 = Incident(
        incident_id=5,
        title="Minor UI issue",
        severity=1,
        created_at=datetime(2026, 9, 1, 10, 0)
    )

    incidents = [
        incident1,
        incident2,
        incident3,
        incident4,
        incident5
    ]

    assert find_incident(incidents, 3) is incident3


def test_find_incident_empty() -> None:
    incidents = []

    assert find_incident(incidents, 3) is None


def test_find_incident_not_found() -> None:
    incident1 = Incident(
        incident_id=1,
        title="Payment service unavailable",
        severity=5,
        created_at=datetime(2026, 9, 13, 9, 30)
    )

    incident2 = Incident(
        incident_id=2,
        title="Login response is slow",
        severity=3,
        created_at=datetime(2026, 9, 12, 14, 20),
        status=IncidentStatus.INVESTIGATING
    )

    incident3 = Incident(
        incident_id=3,
        title="Internal dashboard error",
        severity=2,
        created_at=datetime(2026, 9, 10, 11, 0),
        resolved_at=datetime(2026, 9, 10, 13, 30),
        status=IncidentStatus.RESOLVED
    )

    incident4 = Incident(
        incident_id=4,
        title="Database connection timeout",
        severity=4,
        created_at=datetime(2026, 9, 8, 18, 45)
    )

    incident5 = Incident(
        incident_id=5,
        title="Minor UI issue",
        severity=1,
        created_at=datetime(2026, 9, 1, 10, 0)
    )

    incidents = [
        incident1,
        incident2,
        incident3,
        incident4,
        incident5
    ]

    assert find_incident(incidents, 6) is None


def test_resolve_incident() -> None:
    incident1 = Incident(
        incident_id=1,
        title="Payment service unavailable",
        severity=5,
        created_at=datetime(2026, 9, 13, 9, 30)
    )

    incident2 = Incident(
        incident_id=2,
        title="Login response is slow",
        severity=3,
        created_at=datetime(2026, 9, 12, 14, 20),
        status=IncidentStatus.INVESTIGATING
    )

    incident3 = Incident(
        incident_id=3,
        title="Internal dashboard error",
        severity=2,
        created_at=datetime(2026, 9, 10, 11, 0),
        resolved_at=datetime(2026, 9, 10, 13, 30),
        status=IncidentStatus.RESOLVED
    )

    incident4 = Incident(
        incident_id=4,
        title="Database connection timeout",
        severity=4,
        created_at=datetime(2026, 9, 8, 18, 45)
    )

    incident5 = Incident(
        incident_id=5,
        title="Minor UI issue",
        severity=1,
        created_at=datetime(2026, 9, 1, 10, 0)
    )

    incidents = [
        incident1,
        incident2,
        incident3,
        incident4,
        incident5
    ]

    assert resolve_incident(incidents, 4) is incident4
    assert incident4.status is IncidentStatus.RESOLVED
    assert incident4.resolved_at is not None


def test_resolve_incident_not_found() -> None:
    incident1 = Incident(
        incident_id=1,
        title="Payment service unavailable",
        severity=5,
        created_at=datetime(2026, 9, 13, 9, 30)
    )

    incident2 = Incident(
        incident_id=2,
        title="Login response is slow",
        severity=3,
        created_at=datetime(2026, 9, 12, 14, 20),
        status=IncidentStatus.INVESTIGATING
    )

    incident3 = Incident(
        incident_id=3,
        title="Internal dashboard error",
        severity=2,
        created_at=datetime(2026, 9, 10, 11, 0),
        resolved_at=datetime(2026, 9, 10, 13, 30),
        status=IncidentStatus.RESOLVED
    )

    incident4 = Incident(
        incident_id=4,
        title="Database connection timeout",
        severity=4,
        created_at=datetime(2026, 9, 8, 18, 45)
    )

    incident5 = Incident(
        incident_id=5,
        title="Minor UI issue",
        severity=1,
        created_at=datetime(2026, 9, 1, 10, 0)
    )

    incidents = [
        incident1,
        incident2,
        incident3,
        incident4,
        incident5
    ]

    with pytest.raises(IncidentNotFoundError):
        resolve_incident(incidents, 6)


def test_resolve_incident_empty_list() -> None:  # 感觉这个是不是不用写了，因为find_incident函数已经测试过了：是的，不用写了
    incidents = []

    with pytest.raises(IncidentNotFoundError):
        resolve_incident(incidents, 6)


def test_resolve_incident_solved() -> None:
    incident1 = Incident(
        incident_id=1,
        title="Payment service unavailable",
        severity=5,
        created_at=datetime(2026, 9, 13, 9, 30)
    )

    incident2 = Incident(
        incident_id=2,
        title="Login response is slow",
        severity=3,
        created_at=datetime(2026, 9, 12, 14, 20),
        status=IncidentStatus.INVESTIGATING
    )

    incident3 = Incident(
        incident_id=3,
        title="Internal dashboard error",
        severity=2,
        created_at=datetime(2026, 9, 10, 11, 0),
        resolved_at=datetime(2026, 9, 10, 13, 30),
        status=IncidentStatus.RESOLVED
    )

    incident4 = Incident(
        incident_id=4,
        title="Database connection timeout",
        severity=4,
        created_at=datetime(2026, 9, 8, 18, 45)
    )

    incident5 = Incident(
        incident_id=5,
        title="Minor UI issue",
        severity=1,
        created_at=datetime(2026, 9, 1, 10, 0)
    )

    incidents = [
        incident1,
        incident2,
        incident3,
        incident4,
        incident5
    ]

    with pytest.raises(InvalidIncidentOperationError):
        resolve_incident(incidents, 3)


def test_get_recent_incidents() -> None:
    incident1 = Incident(
        incident_id=1,
        title="Payment service unavailable",
        severity=5,
        created_at=datetime.now() - timedelta(hours=2)  # 测试数据最好别写死，不然过几天这个测试就会报错
    )

    incident2 = Incident(
        incident_id=2,
        title="Login response is slow",
        severity=3,
        created_at=datetime.now() - timedelta(days=1),
        status=IncidentStatus.INVESTIGATING
    )

    incident3 = Incident(
        incident_id=3,
        title="Internal dashboard error",
        severity=2,
        created_at=datetime(2026, 9, 10, 11, 0),
        resolved_at=datetime(2026, 9, 10, 13, 30),
        status=IncidentStatus.RESOLVED
    )

    incident4 = Incident(
        incident_id=4,
        title="Database connection timeout",
        severity=4,
        created_at=datetime(2026, 9, 8, 18, 45)
    )

    incident5 = Incident(
        incident_id=5,
        title="Minor UI issue",
        severity=1,
        created_at=datetime(2026, 9, 1, 10, 0)
    )

    incidents = [
        incident1,
        incident2,
        incident3,
        incident4,
        incident5
    ]

    assert get_recent_incidents(incidents, 3) == [incident1, incident2]


def test_get_recent_incidents_days_zero() -> None:
    incident1 = Incident(
        incident_id=1,
        title="Payment service unavailable",
        severity=5,
        created_at=datetime(2026, 9, 13, 9, 30)
    )

    incident2 = Incident(
        incident_id=2,
        title="Login response is slow",
        severity=3,
        created_at=datetime(2026, 9, 12, 14, 20),
        status=IncidentStatus.INVESTIGATING
    )

    incident3 = Incident(
        incident_id=3,
        title="Internal dashboard error",
        severity=2,
        created_at=datetime(2026, 9, 10, 11, 0),
        resolved_at=datetime(2026, 9, 10, 13, 30),
        status=IncidentStatus.RESOLVED
    )

    incident4 = Incident(
        incident_id=4,
        title="Database connection timeout",
        severity=4,
        created_at=datetime(2026, 9, 8, 18, 45)
    )

    incident5 = Incident(
        incident_id=5,
        title="Minor UI issue",
        severity=1,
        created_at=datetime(2026, 9, 1, 10, 0)
    )

    incidents = [
        incident1,
        incident2,
        incident3,
        incident4,
        incident5
    ]

    with pytest.raises(ValueError):
        get_recent_incidents(incidents, 0)


def test_get_recent_incidents_days_negative() -> None:
    incident1 = Incident(
        incident_id=1,
        title="Payment service unavailable",
        severity=5,
        created_at=datetime(2026, 9, 13, 9, 30)
    )

    incident2 = Incident(
        incident_id=2,
        title="Login response is slow",
        severity=3,
        created_at=datetime(2026, 9, 12, 14, 20),
        status=IncidentStatus.INVESTIGATING
    )

    incident3 = Incident(
        incident_id=3,
        title="Internal dashboard error",
        severity=2,
        created_at=datetime(2026, 9, 10, 11, 0),
        resolved_at=datetime(2026, 9, 10, 13, 30),
        status=IncidentStatus.RESOLVED
    )

    incident4 = Incident(
        incident_id=4,
        title="Database connection timeout",
        severity=4,
        created_at=datetime(2026, 9, 8, 18, 45)
    )

    incident5 = Incident(
        incident_id=5,
        title="Minor UI issue",
        severity=1,
        created_at=datetime(2026, 9, 1, 10, 0)
    )

    incidents = [
        incident1,
        incident2,
        incident3,
        incident4,
        incident5
    ]

    with pytest.raises(ValueError):
        get_recent_incidents(incidents, -1)
