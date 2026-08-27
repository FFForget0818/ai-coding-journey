import pytest
from support_ticket_manager_models import SupportAgent, Ticket
from support_ticket_manager_services import find_ticket_by_id, count_open_tickets, find_highest_priority_ticket, \
    get_tickets_by_agent, calculate_average_priority


def test_find_ticket_by_id() -> None:
    ticket1 = Ticket(1001, "Payment failed", 5, "open")
    ticket2 = Ticket(1002, "Cannot login", 4, "open")
    ticket3 = Ticket(1003, "Refund delayed", 3, "closed")
    tickets = [ticket1, ticket2, ticket3]

    result = find_ticket_by_id(tickets, 1002)

    assert result is ticket2


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


# @pytest.mark.parametrize(
#     "ticket_id, ticket",
#     [
#         (1001, Ticket(1001, "Payment failed", 5, "open")),  # 实在不知道怎么写了：第二个字段不用Ticket，而是expected_title就行了
#     ],
# )
# def test_find_ticket_by_id(ticket_id: int, ticket: Ticket) -> None:
#     ticket1 = Ticket(1001, "Payment failed", 5, "open")
#     ticket2 = Ticket(1002, "Cannot login", 4, "open")
#     ticket3 = Ticket(1003, "Refund delayed", 3, "closed")
#     tickets = [ticket1, ticket2, ticket3]
#
#     assert find_ticket_by_id(tickets, ticket_id) == Ticket


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
    ticket2 = Ticket(1002, "Cannot login", 5, "open")  # 这里要体现【并列最高分返回第一个】的规则
    ticket3 = Ticket(1003, "Refund delayed", 3, "closed")
    tickets = [ticket1, ticket2, ticket3]

    highest_priority_ticket = find_highest_priority_ticket(tickets)

    assert highest_priority_ticket is ticket1


def test_find_highest_priority_ticket_empty_list() -> None:
    tickets = []

    with pytest.raises(ValueError):
        find_highest_priority_ticket(tickets)


def test_get_tickets_by_agent() -> None:
    agent1 = SupportAgent("Alice", "Payments")
    agent2 = SupportAgent("Bob", "Account")

    ticket1 = Ticket(1001, "Payment failed", 5, "open", agent1)
    ticket2 = Ticket(1002, "Cannot login", 4, "open", agent2)
    ticket3 = Ticket(1003, "Refund delayed", 3, "closed", agent1)
    tickets = [ticket1, ticket2, ticket3]

    result = get_tickets_by_agent(tickets, "Alice")

    assert result == [ticket1, ticket3]


def test_get_tickets_by_agent_no_this_agent() -> None:
    agent1 = SupportAgent("Alice", "Payments")
    agent2 = SupportAgent("Bob", "Account")

    ticket1 = Ticket(1001, "Payment failed", 5, "open", agent1)
    ticket2 = Ticket(1002, "Cannot login", 4, "open", agent2)
    ticket3 = Ticket(1003, "Refund delayed", 3, "closed", agent1)
    tickets = [ticket1, ticket2, ticket3]

    result = get_tickets_by_agent(tickets, "David")

    assert result == []


def test_get_tickets_by_agent_all_is_none() -> None:
    ticket1 = Ticket(1001, "Payment failed", 5, "open")
    ticket2 = Ticket(1002, "Cannot login", 4, "open")
    ticket3 = Ticket(1003, "Refund delayed", 3, "closed")
    tickets = [ticket1, ticket2, ticket3]

    result = get_tickets_by_agent(tickets, "David")

    assert result == []


def test_get_tickets_by_agent_empty_list() -> None:
    tickets = []

    result = get_tickets_by_agent(tickets, "David")

    assert result == []


def test_get_tickets_by_agent_with_unassigned_in_middle() -> None:
    alice = SupportAgent("Alice", "Payments")
    ticket1 = Ticket(1001, "A", 5, "open", alice)
    ticket2 = Ticket(1002, "B", 3, "open")
    ticket3 = Ticket(1003, "C", 4, "open", alice)
    tickets = [ticket1, ticket2, ticket3]

    result = get_tickets_by_agent(tickets, "Alice")

    assert result == [ticket1, ticket3]


def test_calculate_average_priority() -> None:
    ticket1 = Ticket(1001, "Payment failed", 5, "open")
    ticket2 = Ticket(1002, "Cannot login", 4, "open")
    ticket3 = Ticket(1003, "Refund delayed", 3, "closed")
    tickets = [ticket1, ticket2, ticket3]

    result = calculate_average_priority(tickets)

    assert result == 4.0


def test_calculate_average_priority_empty_list() -> None:
    tickets = []
    with pytest.raises(ValueError):
        calculate_average_priority(tickets)
