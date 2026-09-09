from models import DeploymentTask


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


