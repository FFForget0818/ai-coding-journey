import pytest
from support_ticket_manager_models import SupportAgent, Ticket
from support_ticket_manager_services import find_ticket_by_id, count_open_tickets, find_highest_priority_ticket


def test_find_ticket_by_id() -> None:
    ticket1 = Ticket(1001, "Payment failed", 5, "open")
    ticket2 = Ticket(1002, "Cannot login", 4, "open")
    ticket3 = Ticket(1003, "Refund delayed", 3, "closed")
    tickets = [ticket1, ticket2, ticket3]

    result = find_ticket_by_id(tickets, 1002)

    assert result == ticket2


def test_find_ticket_by_id_not_found() -> None:
    ticket1 = Ticket(1001, "Payment failed", 5, "open")
    ticket2 = Ticket(1002, "Cannot login", 4, "open")
    ticket3 = Ticket(1003, "Refund delayed", 3, "closed")
    tickets = [ticket1, ticket2, ticket3]

    result = find_ticket_by_id(tickets, 1004)

    assert result is None


def test_find_ticket_by_id_empty_list() -> None:
    tickets = []

    result = find_ticket_by_id(tickets, 1004)

    assert result is None


def test_count_open_tickets() -> None:
    ticket1 = Ticket(1001, "Payment failed", 5, "open")
    ticket2 = Ticket(1002, "Cannot login", 4, "open")
    ticket3 = Ticket(1003, "Refund delayed", 3, "closed")
    tickets = [ticket1, ticket2, ticket3]

    open_tickets = count_open_tickets(tickets)

    assert open_tickets == 2


def test_count_open_tickets_empty_list() -> None:
    tickets = []

    open_tickets = count_open_tickets(tickets)

    assert open_tickets == 0


def test_find_highest_priority_ticket() -> None:
    ticket1 = Ticket(1001, "Payment failed", 5, "open")
    ticket2 = Ticket(1002, "Cannot login", 4, "open")
    ticket3 = Ticket(1003, "Refund delayed", 3, "closed")
    tickets = [ticket1, ticket2, ticket3]

    highest_priority_ticket = find_highest_priority_ticket(tickets)

    assert highest_priority_ticket == ticket1


def test_find_highest_priority_ticket_empty_list() -> None:
    tickets = []

    with pytest.raises(ValueError):
        find_highest_priority_ticket(tickets)