# Part 1 — enumerate + unpacking
import pytest

from ticket_analytics import Ticket, create_ticket_labels, build_priority_updates, find_highest_priority_ticket, \
    sort_tickets_by_priority, get_open_ticket_titles, build_ticket_index, get_all_tags, has_urgent_open_ticket, \
    are_all_tickets_closed, build_mapping, get_top_open_ticket_titles


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
    ticket1 = Ticket(101, "Login issue", 5, "open", "Alice", ["auth", "urgent"])
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
    ticket1 = Ticket(101, "Login issue", 5, "open", "Alice", ["auth", "urgent"])
    ticket2 = Ticket(102, "Export fails", 3, "open", "Bob", ["export"])
    ticket3 = Ticket(103, "Password reset", 2, "closed", "Alice", ["auth"])
    ticket4 = Ticket(104, "Slow dashboard", 4, "open", None, ["performance", "urgent"])
    ticket5 = Ticket(105, "Billing question", 3, "closed", "Cara", ["billing"])
    tickets = [ticket1, ticket2, ticket3, ticket4, ticket5]

    result = sort_tickets_by_priority(tickets)

    assert result == [ticket1, ticket4, ticket2, ticket5, ticket3]
    assert tickets == [ticket1, ticket2, ticket3, ticket4, ticket5]


def test_sort_tickets_by_priority_tie() -> None:
    ticket1 = Ticket(101, "Login issue", 5, "open", "Alice", ["auth", "urgent"])
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
def test_get_open_ticket_titles() -> None:
    ticket1 = Ticket(101, "Login issue", 5, "open", "Alice", ["auth", "urgent"])
    ticket2 = Ticket(102, "Export fails", 3, "open", "Bob", ["export"])
    ticket3 = Ticket(103, "Password reset", 2, "closed", "Alice", ["auth"])
    ticket4 = Ticket(104, "Slow dashboard", 5, "open", None, ["performance", "urgent"])
    ticket5 = Ticket(105, "Billing question", 3, "closed", "Cara", ["billing"])
    tickets = [ticket1, ticket2, ticket3, ticket4, ticket5]

    assert get_open_ticket_titles(tickets) == ["Login issue",
                                               "Export fails",
                                               "Slow dashboard"]


def test_get_open_ticket_titles_no_open_ticket() -> None:
    ticket1 = Ticket(101, "Login issue", 5, "closed", "Alice", ["auth", "urgent"])
    ticket2 = Ticket(102, "Export fails", 3, "closed", "Bob", ["export"])
    ticket3 = Ticket(103, "Password reset", 2, "closed", "Alice", ["auth"])
    ticket4 = Ticket(104, "Slow dashboard", 5, "closed", None, ["performance", "urgent"])
    ticket5 = Ticket(105, "Billing question", 3, "closed", "Cara", ["billing"])
    tickets = [ticket1, ticket2, ticket3, ticket4, ticket5]

    assert get_open_ticket_titles(tickets) == []


def test_get_open_ticket_titles_empty_list() -> None:
    tickets = []

    assert get_open_ticket_titles(tickets) == []


def test_build_ticket_index() -> None:
    ticket1 = Ticket(101, "Login issue", 5, "open", "Alice", ["auth", "urgent"])
    ticket2 = Ticket(102, "Export fails", 3, "open", "Bob", ["export"])
    ticket3 = Ticket(103, "Password reset", 2, "closed", "Alice", ["auth"])
    ticket4 = Ticket(104, "Slow dashboard", 5, "open", None, ["performance", "urgent"])
    ticket5 = Ticket(105, "Billing question", 3, "closed", "Cara", ["billing"])
    tickets = [ticket1, ticket2, ticket3, ticket4, ticket5]

    assert build_ticket_index(tickets) == {101: ticket1,
                                           102: ticket2,
                                           103: ticket3,
                                           104: ticket4,
                                           105: ticket5}


def test_build_ticket_index_repetition() -> None:
    ticket1 = Ticket(101, "Login issue", 5, "open", "Alice", ["auth", "urgent"])
    ticket2 = Ticket(101, "Export fails", 3, "open", "Bob", ["export"])
    ticket3 = Ticket(103, "Password reset", 2, "closed", "Alice", ["auth"])
    ticket4 = Ticket(104, "Slow dashboard", 5, "open", None, ["performance", "urgent"])
    ticket5 = Ticket(105, "Billing question", 3, "closed", "Cara", ["billing"])
    tickets = [ticket1, ticket2, ticket3, ticket4, ticket5]

    result = build_ticket_index(tickets)

    assert result == {101: ticket2,  # dict 不能同时保存两个相同的 key, 如果有两个key都是101，则只会存在一个key，且值是后面那个
                      103: ticket3,
                      104: ticket4,
                      105: ticket5}
    assert result[101] is ticket2  # 再确认一下最后保存的确实就是原来的 ticket2 object
    assert len(result) == 4

# Part 5 — set
def test_get_all_tags() -> None:
    ticket1 = Ticket(101, "Login issue", 5, "open", "Alice", ["auth", "urgent"])
    ticket2 = Ticket(102, "Export fails", 3, "open", "Bob", ["export"])
    ticket3 = Ticket(103, "Password reset", 2, "closed", "Alice", ["auth"])
    ticket4 = Ticket(104, "Slow dashboard", 5, "open", None, ["performance", "urgent"])
    ticket5 = Ticket(105, "Billing question", 3, "closed", "Cara", ["billing"])
    tickets = [ticket1, ticket2, ticket3, ticket4, ticket5]

    assert get_all_tags(tickets) == {
                                        "auth",
                                        "urgent",
                                        "export",
                                        "performance",
                                        "billing",
                                    }


def test_get_all_tags_empty() -> None:
    tickets = []

    assert get_all_tags(tickets) == set()  # 原来set不是{}啊，就是set()


# Part 6 — any / all
def test_has_urgent_open_ticket() -> None:
    ticket1 = Ticket(101, "Login issue", 5, "open", "Alice", ["auth", "urgent"])
    ticket2 = Ticket(102, "Export fails", 3, "open", "Bob", ["export"])
    ticket3 = Ticket(103, "Password reset", 2, "closed", "Alice", ["auth"])
    ticket4 = Ticket(104, "Slow dashboard", 5, "open", None, ["performance", "urgent"])
    ticket5 = Ticket(105, "Billing question", 3, "closed", "Cara", ["billing"])
    tickets = [ticket1, ticket2, ticket3, ticket4, ticket5]

    assert has_urgent_open_ticket(tickets) is True


def test_has_urgent_open_ticket_false() -> None:
    ticket1 = Ticket(101, "Login issue", 5, "open", "Alice", ["auth"])
    ticket2 = Ticket(102, "Export fails", 3, "open", "Bob", ["export"])
    ticket3 = Ticket(103, "Password reset", 2, "closed", "Alice", ["auth"])
    ticket4 = Ticket(104, "Slow dashboard", 5, "open", None, ["performance"])
    ticket5 = Ticket(105, "Billing question", 3, "closed", "Cara", ["billing", "urgent"])
    tickets = [ticket1, ticket2, ticket3, ticket4, ticket5]

    assert has_urgent_open_ticket(tickets) is False


def test_has_urgent_open_ticket_empty() -> None:
    tickets = []

    assert has_urgent_open_ticket(tickets) is False


def test_are_all_tickets_closed() -> None:
    ticket1 = Ticket(101, "Login issue", 5, "open", "Alice", ["auth"])
    ticket2 = Ticket(102, "Export fails", 3, "open", "Bob", ["export"])
    ticket3 = Ticket(103, "Password reset", 2, "closed", "Alice", ["auth"])
    ticket4 = Ticket(104, "Slow dashboard", 5, "open", None, ["performance"])
    ticket5 = Ticket(105, "Billing question", 3, "closed", "Cara", ["billing", "urgent"])
    tickets = [ticket1, ticket2, ticket3, ticket4, ticket5]

    assert are_all_tickets_closed(tickets) is False


def test_are_all_tickets_closed_all_closed() -> None:
    ticket1 = Ticket(101, "Login issue", 5, "closed", "Alice", ["auth"])
    ticket2 = Ticket(102, "Export fails", 3, "closed", "Bob", ["export"])
    ticket3 = Ticket(103, "Password reset", 2, "closed", "Alice", ["auth"])
    ticket4 = Ticket(104, "Slow dashboard", 5, "closed", None, ["performance"])
    ticket5 = Ticket(105, "Billing question", 3, "closed", "Cara", ["billing", "urgent"])
    tickets = [ticket1, ticket2, ticket3, ticket4, ticket5]

    assert are_all_tickets_closed(tickets) is True


def test_are_all_tickets_closed_empty() -> None:
    tickets = []

    assert are_all_tickets_closed(tickets) is False


# Final Challenge
# Challenge 1 — 找 silent bug
def test_build_mapping() -> None:
    names = ["Alice", "Bob", "Carlie"]
    scores = [95, 80, 72]

    result = build_mapping(names, scores)

    assert result == {
        "Alice": 95,
        "Bob": 80,
        "Carlie": 72
    }


def test_build_mapping_diff_len() -> None:
    names = ["Alice", "Bob", "Carlie"]
    scores = [95, 80]

    with pytest.raises(ValueError):
        build_mapping(names, scores)


def test_build_mapping_repetition_name() -> None:
    names = ["Alice", "Alice", "Carlie"]
    scores = [95, 80, 72]

    result = build_mapping(names, scores)

    assert result == {
        "Alice": 80,
        "Carlie": 72
    }
    assert len(result) == 2


def test_build_mapping_empty() -> None:
    names = []
    scores = []

    result = build_mapping(names, scores)

    assert result == {}


# Challenge 4 — 综合函数
def test_get_top_open_ticket_titles() -> None:
    ticket1 = Ticket(101, "Login issue", 5, "open", "Alice", ["auth"])
    ticket2 = Ticket(102, "Export fails", 3, "open", "Bob", ["export"])
    ticket3 = Ticket(103, "Password reset", 2, "closed", "Alice", ["auth"])
    ticket4 = Ticket(104, "Slow dashboard", 5, "open", None, ["performance"])
    ticket5 = Ticket(105, "Billing question", 3, "closed", "Cara", ["billing", "urgent"])
    tickets = [ticket1, ticket2, ticket3, ticket4, ticket5]
    limit = 2

    assert get_top_open_ticket_titles(tickets, limit) == [
                                                    "Login issue",
                                                    "Slow dashboard",
                                                  ]


def test_get_top_open_ticket_titles_negative_limit() -> None:
    ticket1 = Ticket(101, "Login issue", 5, "open", "Alice", ["auth"])
    ticket2 = Ticket(102, "Export fails", 3, "open", "Bob", ["export"])
    ticket3 = Ticket(103, "Password reset", 2, "closed", "Alice", ["auth"])
    ticket4 = Ticket(104, "Slow dashboard", 5, "open", None, ["performance"])
    ticket5 = Ticket(105, "Billing question", 3, "closed", "Cara", ["billing", "urgent"])
    tickets = [ticket1, ticket2, ticket3, ticket4, ticket5]
    limit = -2

    assert get_top_open_ticket_titles(tickets, limit) == []


def test_get_top_open_ticket_titles_zero_limit() -> None:
    ticket1 = Ticket(101, "Login issue", 5, "open", "Alice", ["auth"])
    ticket2 = Ticket(102, "Export fails", 3, "open", "Bob", ["export"])
    ticket3 = Ticket(103, "Password reset", 2, "closed", "Alice", ["auth"])
    ticket4 = Ticket(104, "Slow dashboard", 5, "open", None, ["performance"])
    ticket5 = Ticket(105, "Billing question", 3, "closed", "Cara", ["billing", "urgent"])
    tickets = [ticket1, ticket2, ticket3, ticket4, ticket5]
    limit = 0

    assert get_top_open_ticket_titles(tickets, limit) == []