from support_ticket_manager_models import SupportAgent, Ticket


def find_ticket_by_id(tickets: list[Ticket], ticket_id: int) -> Ticket | None:
    for ticket in tickets:
        if ticket.ticket_id == ticket_id:
            return ticket
    return None


def count_open_tickets(tickets: list[Ticket]) -> int:
    open_tickets = 0
    for ticket in tickets:
        if ticket.status == "open":
            open_tickets += 1
    return open_tickets


def find_highest_priority_ticket(tickets: list[Ticket]) -> Ticket:
    if len(tickets) == 0:
        raise ValueError("The list is empty!")
    highest_priority_ticket = tickets[0]
    for ticket in tickets[1:]:
        if ticket.priority > highest_priority_ticket.priority:
            highest_priority_ticket = ticket
    return highest_priority_ticket


def get_tickets_by_agent(tickets: list[Ticket], agent: str) -> list[Ticket]:
    results = []
    for ticket in tickets:
        if ticket.assignee is None:
            continue  # 这里应该是continue，而不是break，continue是跳过当前ticket，而break是结束当前循环
        elif ticket.assignee.name == agent:
            results.append(ticket)
    return results


def calculate_average_priority(tickets: list[Ticket]) -> float:
    if len(tickets) == 0:
        raise ValueError("The list is empty!")
    total_value = 0
    for ticket in tickets:
        total_value += ticket.priority
    return total_value / len(tickets)
