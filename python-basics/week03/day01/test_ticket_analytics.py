# Part 1 — enumerate + unpacking
import pytest

from ticket_analytics import Ticket, create_ticket_labels, build_priority_updates, find_highest_priority_ticket, \
    sort_tickets_by_priority


def test_create_ticket_labels() -> None:
    tickets = [
        Ticket(101, "Login issue", 5, "open", "Alice", ["auth", "urgent"]),
        Ticket(102, "Export fails", 3, "open", "Bob", ["export"]),
        Ticket(103, "Password reset", 2, "closed", "Alice", ["auth"]),
        Ticket(104, "Slow dashboard", 5, "open", None, ["performance", "urgent"]),
        Ticket(105, "Billing question", 3, "closed", "Cara", ["billing"]),
    ]

    assert create_ticket_labels(tickets) == ['1. #101 Login issue',
                                             '2. #102 Export fails',
                                             '3. #103 Password reset',
                                             '4. #104 Slow dashboard',
                                             '5. #105 Billing question']


def test_create_ticket_labels_empty_list() -> None:
    tickets = []

    assert create_ticket_labels(tickets) == []


# Part 2 — zip
def test_build_priority_updates() -> None:
    ticket_ids = [101, 102, 103]
    priorities = [5, 2, 4]

    assert build_priority_updates(ticket_ids, priorities) == {
                                                                101: 5,
                                                                102: 2,
                                                                103: 4,
                                                            }


def test_build_priority_updates_both_empty() -> None:
    ticket_ids = []
    priorities = []

    assert build_priority_updates(ticket_ids, priorities) == {}


def test_build_priority_updates_different_len() -> None:
    ticket_ids = [101, 102, 103]
    priorities = [5, 2]

    with pytest.raises(ValueError):
        build_priority_updates(ticket_ids, priorities)


# Part 3 — sorted / max + key
def test_find_highest_priority_ticket() -> None:
    ticket1 = Ticket(101, "Login issue", 5, "open", "Alice", ["auth", "urgent"])  # 修改的时候忘记删这里的逗号了
    ticket2 = Ticket(102, "Export fails", 3, "open", "Bob", ["export"])
    ticket3 = Ticket(103, "Password reset", 2, "closed", "Alice", ["auth"])
    ticket4 = Ticket(104, "Slow dashboard", 4, "open", None, ["performance", "urgent"])
    ticket5 = Ticket(105, "Billing question", 3, "closed", "Cara", ["billing"])
    tickets = [ticket1, ticket2, ticket3, ticket4, ticket5]

    result = find_highest_priority_ticket(tickets)

    assert result is ticket1


def test_find_highest_priority_ticket_tie() -> None:
    ticket1 = Ticket(101, "Login issue", 5, "open", "Alice", ["auth", "urgent"])  # 修改的时候忘记删这里的逗号了
    ticket2 = Ticket(102, "Export fails", 3, "open", "Bob", ["export"])
    ticket3 = Ticket(103, "Password reset", 2, "closed", "Alice", ["auth"])
    ticket4 = Ticket(104, "Slow dashboard", 5, "open", None, ["performance", "urgent"])
    ticket5 = Ticket(105, "Billing question", 3, "closed", "Cara", ["billing"])
    tickets = [ticket1, ticket2, ticket3, ticket4, ticket5]

    result = find_highest_priority_ticket(tickets)

    assert result is ticket1


def test_find_highest_priority_ticket_empty() -> None:
    tickets = []

    result = find_highest_priority_ticket(tickets)

    assert result is None


def test_sort_tickets_by_priority() -> None:
    ticket1 = Ticket(101, "Login issue", 5, "open", "Alice", ["auth", "urgent"])  # 修改的时候忘记删这里的逗号了
    ticket2 = Ticket(102, "Export fails", 3, "open", "Bob", ["export"])
    ticket3 = Ticket(103, "Password reset", 2, "closed", "Alice", ["auth"])
    ticket4 = Ticket(104, "Slow dashboard", 4, "open", None, ["performance", "urgent"])
    ticket5 = Ticket(105, "Billing question", 3, "closed", "Cara", ["billing"])
    tickets = [ticket1, ticket2, ticket3, ticket4, ticket5]

    result = sort_tickets_by_priority(tickets)

    assert result == [ticket1, ticket4, ticket2, ticket5, ticket3]
    assert tickets == [ticket1, ticket2, ticket3, ticket4, ticket5]


def test_sort_tickets_by_priority_tie() -> None:
    ticket1 = Ticket(101, "Login issue", 5, "open", "Alice", ["auth", "urgent"])  # 修改的时候忘记删这里的逗号了
    ticket2 = Ticket(102, "Export fails", 3, "open", "Bob", ["export"])
    ticket3 = Ticket(103, "Password reset", 2, "closed", "Alice", ["auth"])
    ticket4 = Ticket(104, "Slow dashboard", 5, "open", None, ["performance", "urgent"])
    ticket5 = Ticket(105, "Billing question", 3, "closed", "Cara", ["billing"])
    tickets = [ticket1, ticket2, ticket3, ticket4, ticket5]

    result = sort_tickets_by_priority(tickets)

    assert result == [ticket1, ticket4, ticket2, ticket5, ticket3]
    assert tickets == [ticket1, ticket2, ticket3, ticket4, ticket5]


def test_sort_tickets_by_priority_empty() -> None:
    tickets = []

    result = sort_tickets_by_priority(tickets)

    assert result == []


# Part 4 — List / Dict Comprehension
