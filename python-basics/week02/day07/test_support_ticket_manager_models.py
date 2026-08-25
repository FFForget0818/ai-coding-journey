import pytest

from support_ticket_manager_models import SupportAgent, Ticket


# 测试新建一个Ticket
def test_ticket_init_priotity_below() -> None:
    agent1 = SupportAgent("Alice", "Payments")

    with pytest.raises(ValueError):
        ticket1 = Ticket(1001, "Payment failed", -1, "open", agent1)


def test_ticket_init_priotity_above() -> None:
    agent1 = SupportAgent("Alice", "Payments")

    with pytest.raises(ValueError):
        ticket1 = Ticket(1001, "Payment failed", 6, "open", agent1)


def test_ticket_init_priotity_lower() -> None:
    agent1 = SupportAgent("Alice", "Payments")
    ticket1 = Ticket(1001, "Payment failed", 1, "open", agent1)

    assert ticket1.priority == 1


def test_ticket_init_priotity_upper() -> None:
    agent1 = SupportAgent("Alice", "Payments")
    ticket1 = Ticket(1001, "Payment failed", 5, "open", agent1)

    assert ticket1.priority == 5