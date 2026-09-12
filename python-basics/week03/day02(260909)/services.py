from models import DeploymentTask
from exceptions import TaskNotFoundError, InvalidTaskOperationError


# Part 1：什么时候返回 None、[]，什么时候正常返回值
def find_task_by_id(
    tasks: list[DeploymentTask],
    task_id: int
) -> DeploymentTask | None:
    if len(tasks) == 0:
        return None
    for task in tasks:
        if task.task_id == task_id:
            return task
    return None


def get_pending_tasks(
    tasks: list[DeploymentTask]
) -> list[DeploymentTask]:
    return [
        task
        for task in tasks
        if task.status == "pending"
    ]


def find_highest_priority_task(
    tasks: list[DeploymentTask]
) -> DeploymentTask | None:
    if len(tasks) == 0:
        return None
    return max(
        tasks, key=lambda task: task.priority
    )
# max在有多个最大值时，返回第一个
# 如果是空列表，max会raise错误


# Part 3：Custom Exception——区分“数据非法”和“业务操作失败”
def complete_task(
    tasks: list[DeploymentTask],
    task_id: int
) -> DeploymentTask:
    wanna_find_task = find_task_by_id(tasks, task_id)
    if wanna_find_task is None:
        raise TaskNotFoundError('Task not found!')
    if wanna_find_task.status == "completed":
        raise InvalidTaskOperationError("Task is completed!")
    wanna_find_task.status = "completed"
    return wanna_find_task


# Part 4：Business Rule 和 Python 默认行为不是一回事
def assign_task(
    tasks: list[DeploymentTask],
    task_id: int,
    assignee: str
) -> DeploymentTask:
    wanna_find_task = find_task_by_id(tasks, task_id)
    if wanna_find_task is None:
        raise TaskNotFoundError('Task not found!')
    if assignee.strip() == "":  # 这个strip()又忘记写()了
        raise ValueError("assignee is empty!")
    if wanna_find_task.status == "completed":
        raise InvalidTaskOperationError("Task is completed!")
    if wanna_find_task.assignee is not None:
        raise InvalidTaskOperationError("Task has a assignee!")
    wanna_find_task.status = "in_progress"
    wanna_find_task.assignee = assignee
    return wanna_find_task

