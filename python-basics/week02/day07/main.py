from support_ticket_manager_models import SupportAgent, Ticket
from support_ticket_manager_services import count_open_tickets, find_highest_priority_ticket, get_tickets_by_agent, \
    find_ticket_by_id, calculate_average_priority


def main() -> None:  # 又忘记这个怎么写了
    agent1 = SupportAgent("Alice", "Payments")
    agent2 = SupportAgent("Bob", "Account")
    agent3 = SupportAgent("Charlie", "Technical", active=False)

    ticket1 = Ticket(1001, "Payment failed", 5, "open", agent1)
    ticket2 = Ticket(1002, "Cannot login", 4, "open", agent2)
    ticket3 = Ticket(1003, "Refund delayed", 3, "closed", agent1)
    ticket4 = Ticket(1004, "App crashes", 5, "open", agent3)
    ticket5 = Ticket(1005, "Change email address", 2, "open")
    tickets = [ticket1, ticket2, ticket3, ticket4, ticket5]

    ticket5.assign_to(agent2)
    print(ticket5.assignee.name)

    ticket5.update_priority(1)
    print(ticket5.priority)

    ticket5.close()
    print(ticket5.status)

    print(ticket5.get_summary())

    open_tickets = count_open_tickets(tickets)
    print(open_tickets)

    highest_priority_ticket = find_highest_priority_ticket(tickets)
    print(highest_priority_ticket)

    result = get_tickets_by_agent(tickets, "Alice")
    print(result)

    wanna_found_ticket = find_ticket_by_id(tickets, 1002)
    print(wanna_found_ticket)

    average_priority = calculate_average_priority(tickets)
    print(average_priority)


if __name__ == "__main__":  # 又忘记这个怎么写了
    main()
