import pytest
from support_ticket_manager_models import SupportAgent, Ticket


# 测试新建一个SupportAgent
def test_supportagent_init_name() -> None:
    agent1 = SupportAgent("Alice", "Payment failed")

    assert agent1.name == "Alice"


def test_supportagent_init_name_ill1() -> None:
    with pytest.raises(ValueError):
        SupportAgent("", "Payment failed")


def test_supportagent_init_name_ill2() -> None:
    with pytest.raises(ValueError):
        SupportAgent("   ", "Payment failed")


# 测试新建一个Ticket
def test_ticket_init_ticket_id() -> None:
    ticket1 = Ticket(1001, "Payment failed", 3, "open")

    assert ticket1.ticket_id == 1001


def test_ticket_init_ticket_id_lower() -> None:
    with pytest.raises(ValueError):
        Ticket(1001, "Payment failed", 0, "open")


def test_ticket_init_ticket_id_below() -> None:
    with pytest.raises(ValueError):
        Ticket(1001, "Payment failed", -1, "open")


def test_ticket_init_title() -> None:
    ticket1 = Ticket(1001, "Payment failed", 3, "open")

    assert ticket1.title == "Payment failed"


def test_ticket_init_title_ill1() -> None:
    with pytest.raises(ValueError):
        Ticket(1001, "", 3, "open")


def test_ticket_init_title_ill2() -> None:
    with pytest.raises(ValueError):
        Ticket(1001, "   ", 3, "open")


def test_ticket_init_priotity() -> None:
    ticket1 = Ticket(1001, "Payment failed", 3, "open")

    assert ticket1.priority == 3


def test_ticket_init_priotity_below() -> None:
    with pytest.raises(ValueError):
        Ticket(1001, "Payment failed", 0, "open")


def test_ticket_init_priotity_above() -> None:
    with pytest.raises(ValueError):
        Ticket(1001, "Payment failed", 6, "open")


def test_ticket_init_priotity_lower() -> None:
    ticket1 = Ticket(1001, "Payment failed", 1, "open")

    assert ticket1.priority == 1


def test_ticket_init_priotity_upper() -> None:
    ticket1 = Ticket(1001, "Payment failed", 5, "open")

    assert ticket1.priority == 5


def test_ticket_init_status1() -> None:
    ticket1 = Ticket(1001, "Payment failed", 5, "open")
    assert ticket1.status == "open"


def test_ticket_init_status2() -> None:
    ticket1 = Ticket(1001, "Payment failed", 5, "closed")
    assert ticket1.status == "closed"


def test_ticket_init_status_ill() -> None:
    with pytest.raises(ValueError):
        Ticket(1001, "Payment failed", 5, "opend")


# 这里本来还想验证一下assignee的类型，但是不知道怎么写


# 测试功能函数
def test_assign_to() -> None:
    agent1 = SupportAgent("Alice", "Payments")
    ticket1 = Ticket(1001, "Payment failed", 5, "open")

    ticket1.assign_to(agent1)

    assert ticket1.assignee == agent1  # 这里一开始写成raise了


def test_close() -> None:
    ticket1 = Ticket(1001, "Payment failed", 5, "open")

    ticket1.close()

    assert ticket1.status == "closed"


def test_update_priority() -> None:
    ticket1 = Ticket(1001, "Payment failed", 5, "open")

    ticket1.update_priority(3)

    assert ticket1.priority == 3


def test_update_priority_below() -> None:
    ticket1 = Ticket(1001, "Payment failed", 5, "open")

    with pytest.raises(ValueError):
        ticket1.update_priority(0)


def test_update_priority_above() -> None:
    ticket1 = Ticket(1001, "Payment failed", 5, "open")

    with pytest.raises(ValueError):
        ticket1.update_priority(6)


def test_update_priority_lower() -> None:
    ticket1 = Ticket(1001, "Payment failed", 3, "open")

    ticket1.update_priority(1)

    assert ticket1.priority == 1


def test_update_priority_upper() -> None:
    ticket1 = Ticket(1001, "Payment failed", 3, "open")

    ticket1.update_priority(5)

    assert ticket1.priority == 5


def test_get_summary_assigned() -> None:
    agent1 = SupportAgent("Alice", "Payments")  # 一开始忘记写SupportAgent了
    ticket1 = Ticket(1001, "Payment failed", 3, "open", agent1)

    summary = ticket1.get_summary()

    assert summary == f"# 1001 Payment failed | priority=3 | status=open | assignee=Alice"


def test_get_summary_not_assigned() -> None:
    ticket1 = Ticket(1001, "Payment failed", 3, "open")

    summary = ticket1.get_summary()

    assert summary == f"# 1001 Payment failed | priority=3 | status=open | assignee=Unassigned"

