# Part 1 — enumerate + unpacking
from dataclasses import dataclass


@dataclass
class Ticket:
    ticket_id: int
    title: str
    priority: int
    status: str
    assignee: str | None
    tags: list[str]


def create_ticket_labels(
        tickets: list[Ticket]
) -> list[str]:
    result = []
    for index, ticket in enumerate(tickets, start=1):
        result.append(f'{index}. #{ticket.ticket_id} {ticket.title}')  # 一开始我是在这里写的 index+1
    return result


# Part 2 — zip
def build_priority_updates(
    ticket_ids: list[int],
    priorities: list[int]
) -> dict[int, int]:
    if len(ticket_ids) != len(priorities):
        raise ValueError("两个 list 长度不同!")
    result = {}
    for ticket_id, priority in zip(ticket_ids, priorities):  # 原本写的ticket_ids和priorities，不太好，需要改为单数
        result[ticket_id] = priority  # 又忘记怎么给dict加新的键值对了哈哈，然后还以为key不能直接写变量呢
    return result


# Part 3 — sorted / max + key
def find_highest_priority_ticket(
    tickets: list[Ticket]
) -> Ticket | None:
    if len(tickets) == 0:
        return None
    return max(tickets, key=lambda ticket: ticket.priority)


def sort_tickets_by_priority(
    tickets: list[Ticket]
) -> list[Ticket]:
    return sorted(tickets, key=lambda ticket: (-ticket.priority, ticket.ticket_id))  # 建议不开reverse，用负号


# Part 4 — List / Dict Comprehension
# [
#     result
#     for item in collection
#     if condition
# ]
def get_open_ticket_titles(
    tickets: list[Ticket]
) -> list[str]:
    return [
        ticket.title
        for ticket in tickets
        if ticket.status == "open"
    ]


# {
#     ticket.ticket_id: ticket
#     for ticket in tickets
# }
def build_ticket_index(
    tickets: list[Ticket]
) -> dict[int, Ticket]:
    return {
        ticket.ticket_id: ticket
        for ticket in tickets
    }
