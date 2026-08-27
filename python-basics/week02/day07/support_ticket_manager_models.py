from dataclasses import dataclass


@dataclass
class SupportAgent:
    name: str
    team: str
    active: bool = True

    def __post_init__(self) -> None:
        if self.name.strip() == "":
            raise ValueError("Name must not be space!")


@dataclass
class Ticket:
    ticket_id: int
    title: str
    priority: int
    status: str
    assignee: SupportAgent | None = None

    def __post_init__(self) -> None:
        if self.ticket_id <= 0:
            raise ValueError("Ticket_id must greater than 0.")
        if self.title.strip() == "":
            raise ValueError("Ticket title must not be space.")
        if self.priority < 1 or self.priority > 5:
            raise ValueError("Priority must between 1 and 5.")
        if self.status != "open" and self.status != "closed":  # 这里一开始写的是or，搞错了
            raise ValueError("Status must be open or closed.")
        # 这里本来还想验证一下assignee的类型，但是不知道怎么写
        # if self.assignee is not None and not isinstance(
        #     self.assignee, SupportAgent
        # ):

    # 分配负责人
    def assign_to(self, agent: SupportAgent) -> None:
        self.assignee = agent

    # 关闭工单
    def close(self) -> None:
        self.status = "closed"

    # 修改优先级
    def update_priority(self, new_priority: int) -> None:
        if new_priority < 1 or new_priority > 5:
            raise ValueError("Priority must between 1 and 5.")
        self.priority = new_priority

    # 生成 summary
    def get_summary(self) -> str:
        if self.assignee is None:
            return f"# {self.ticket_id} {self.title} | priority={self.priority} | " \
                   f"status={self.status} | assignee=Unassigned"
        return f"# {self.ticket_id} {self.title} | priority={self.priority} | " \
               f"status={self.status} | assignee={self.assignee.name}"

