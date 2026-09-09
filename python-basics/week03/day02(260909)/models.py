from dataclasses import dataclass


@dataclass
class DeploymentTask:
    task_id: int
    title: str
    priority: int
    status: str = "pending"
    assignee: str | None = None


# Part 2：什么时候应该 raise ValueError
    # 第一次写的时候忘记缩进了，死活不对
    def __post_init__(self) -> None:

        if self.task_id <= 0:
            raise ValueError("task_id must higher than 0!")

        if self.title.strip() == "":  # 这里strip忘记写()了
            raise ValueError("title must not be empty!")

        if self.priority < 1 or self.priority > 5:
            raise ValueError("priority must between 1 and 5!")

        if self.status != "pending" and self.status != "in_progress" and self.status != "completed":
            raise ValueError("status must be pending or in_progress or completed!")
