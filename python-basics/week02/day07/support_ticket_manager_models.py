from dataclasses import dataclass


@dataclass
class SupportAgent:
    name: str
    team: str
    active: bool = True


@dataclass
class Ticket:
    ticket_id: int
    title: str
    priority: int
    status: str
    assignee: SupportAgent | None

    def __post_init__(self) -> None:
        if self.priority < 1 or self.priority > 5:
            raise ValueError("Priority must between 1 and 5.")
        if self.status != "open" and self.status != "closed":  # 这里一开始写的是or，搞错了
            raise ValueError("Status must be open or closed.")

    # 分配负责人
    def assign_to(self, agent: SupportAgent) -> None:
        self.assignee = agent

    # 关闭工单
    def close(self) -> None:
        self.status = "closed"

    # 修改优先级
    # def update_priority(self, new_priority: int) -> None: