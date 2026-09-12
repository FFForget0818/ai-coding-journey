from models import DeploymentTask
from services import find_task_by_id, get_pending_tasks, find_highest_priority_task, complete_task, assign_task
import pytest
from exceptions import TaskNotFoundError, InvalidTaskOperationError


# Part 1：什么时候返回 None、[]，什么时候正常返回值
def test_find_task_by_id() -> None:
    task1 = DeploymentTask(
                            task_id=1,
                            title="Deploy login service",
                            priority=3,
                            status="pending",
                            assignee=None
                          )
    task2 = DeploymentTask(
                            task_id=2,
                            title="Fix payment bug",
                            priority=5,
                            status="in_progress",
                            assignee="Alice"
                          )
    task3 = DeploymentTask(
                            task_id=3,
                            title="Update database schema",
                            priority=4,
                            status="pending",
                            assignee=None
                          )
    task4 = DeploymentTask(
                            task_id=4,
                            title="Clean old logs",
                            priority=1,
                            status="completed",
                            assignee="Bob"
                          )
    task5 = DeploymentTask(
                            task_id=5,
                            title="Deploy recommendation service",
                            priority=5,
                            status="pending",
                            assignee=None
                          )

    tasks = [task1, task2, task3, task4, task5]

    result = find_task_by_id(tasks, 3)

    assert result is task3


def test_find_task_by_id_cant_find() -> None:
    task1 = DeploymentTask(
                            task_id=1,
                            title="Deploy login service",
                            priority=3,
                            status="pending",
                            assignee=None
                          )
    task2 = DeploymentTask(
                            task_id=2,
                            title="Fix payment bug",
                            priority=5,
                            status="in_progress",
                            assignee="Alice"
                          )
    task3 = DeploymentTask(
                            task_id=3,
                            title="Update database schema",
                            priority=4,
                            status="pending",
                            assignee=None
                          )
    task4 = DeploymentTask(
                            task_id=4,
                            title="Clean old logs",
                            priority=1,
                            status="completed",
                            assignee="Bob"
                          )
    task5 = DeploymentTask(
                            task_id=5,
                            title="Deploy recommendation service",
                            priority=5,
                            status="pending",
                            assignee=None
                          )

    tasks = [task1, task2, task3, task4, task5]

    result = find_task_by_id(tasks, 6)

    assert result is None


def test_find_task_by_id_empty_list() -> None:
    tasks = []

    result = find_task_by_id(tasks, 3)

    assert result is None


def test_get_pending_tasks() -> None:
    task1 = DeploymentTask(
                            task_id=1,
                            title="Deploy login service",
                            priority=3,
                            status="pending",
                            assignee=None
                          )
    task2 = DeploymentTask(
                            task_id=2,
                            title="Fix payment bug",
                            priority=5,
                            status="in_progress",
                            assignee="Alice"
                          )
    task3 = DeploymentTask(
                            task_id=3,
                            title="Update database schema",
                            priority=4,
                            status="pending",
                            assignee=None
                          )
    task4 = DeploymentTask(
                            task_id=4,
                            title="Clean old logs",
                            priority=1,
                            status="completed",
                            assignee="Bob"
                          )
    task5 = DeploymentTask(
                            task_id=5,
                            title="Deploy recommendation service",
                            priority=5,
                            status="pending",
                            assignee=None
                          )

    tasks = [task1, task2, task3, task4, task5]

    result = get_pending_tasks(tasks)

    assert result == [task1, task3, task5]


def test_get_pending_tasks_empty_list() -> None:
    tasks = []

    result = get_pending_tasks(tasks)

    assert result == []


def test_get_pending_no_pending_tasks() -> None:
    task1 = DeploymentTask(
                            task_id=1,
                            title="Deploy login service",
                            priority=3,
                            status="in_progress",
                            assignee=None
                          )
    task2 = DeploymentTask(
                            task_id=2,
                            title="Fix payment bug",
                            priority=5,
                            status="in_progress",
                            assignee="Alice"
                          )
    task3 = DeploymentTask(
                            task_id=3,
                            title="Update database schema",
                            priority=4,
                            status="in_progress",
                            assignee=None
                          )
    task4 = DeploymentTask(
                            task_id=4,
                            title="Clean old logs",
                            priority=1,
                            status="completed",
                            assignee="Bob"
                          )
    task5 = DeploymentTask(
                            task_id=5,
                            title="Deploy recommendation service",
                            priority=5,
                            status="completed",
                            assignee=None
                          )

    tasks = [task1, task2, task3, task4, task5]

    result = get_pending_tasks(tasks)

    assert result == []


def test_find_highest_priority_task() -> None:
    task1 = DeploymentTask(
                            task_id=1,
                            title="Deploy login service",
                            priority=3,
                            status="pending",
                            assignee=None
                          )
    task2 = DeploymentTask(
                            task_id=2,
                            title="Fix payment bug",
                            priority=5,
                            status="in_progress",
                            assignee="Alice"
                          )
    task3 = DeploymentTask(
                            task_id=3,
                            title="Update database schema",
                            priority=4,
                            status="pending",
                            assignee=None
                          )
    task4 = DeploymentTask(
                            task_id=4,
                            title="Clean old logs",
                            priority=1,
                            status="completed",
                            assignee="Bob"
                          )
    task5 = DeploymentTask(
                            task_id=5,
                            title="Deploy recommendation service",
                            priority=5,
                            status="pending",
                            assignee=None
                          )

    tasks = [task1, task2, task3, task4, task5]

    result = find_highest_priority_task(tasks)

    assert result is task2


def test_find_highest_priority_task_empty_list() -> None:
    tasks = []

    result = find_highest_priority_task(tasks)

    assert result is None


# Part 2：什么时候应该 raise ValueError
def test___post_init___task_id_negative() -> None:
    with pytest.raises(ValueError):
        DeploymentTask(
                        task_id=-1,
                        title="Deploy recommendation service",
                        priority=5,
                        status="pending",
                        assignee=None
                      )


def test___post_init___task_id_zero() -> None:
    with pytest.raises(ValueError):
        DeploymentTask(
                        task_id=0,
                        title="Deploy recommendation service",
                        priority=5,
                        status="pending",
                        assignee=None
                      )


def test___post_init___title_is_empty() -> None:
    with pytest.raises(ValueError):
        DeploymentTask(
            task_id=1,
            title="",
            priority=5,
            status="pending",
            assignee=None
        )


def test___post_init___title_is_empty_2() -> None:
    with pytest.raises(ValueError):
        DeploymentTask(
            task_id=1,
            title="   ",
            priority=5,
            status="pending",
            assignee=None
        )


def test___post_init___priority_zero() -> None:
    with pytest.raises(ValueError):
        DeploymentTask(
            task_id=1,
            title="Deploy recommendation service",
            priority=0,
            status="pending",
            assignee=None
        )


def test___post_init___priority_six() -> None:
    with pytest.raises(ValueError):
        DeploymentTask(
            task_id=1,
            title="Deploy recommendation service",
            priority=6,
            status="pending",
            assignee=None
        )


def test___post_init___status_ill() -> None:
    with pytest.raises(ValueError):
        DeploymentTask(
            task_id=1,
            title="Deploy recommendation service",
            priority=3,
            status="test",
            assignee=None
        )


def test___post_init__() -> None:
    DeploymentTask(
                    task_id=1,
                    title="Deploy recommendation service",
                    priority=3,
                    status="pending",
                    assignee=None
                  )
# 这个正常创建的反而不知道怎么写了，但其实这样就可以了


# Part 3：Custom Exception——区分“数据非法”和“业务操作失败”
def test_complete_task() -> None:
    task1 = DeploymentTask(
                            task_id=1,
                            title="Deploy login service",
                            priority=3,
                            status="pending",
                            assignee=None
                          )
    task2 = DeploymentTask(
                            task_id=2,
                            title="Fix payment bug",
                            priority=5,
                            status="in_progress",
                            assignee="Alice"
                          )
    task3 = DeploymentTask(
                            task_id=3,
                            title="Update database schema",
                            priority=4,
                            status="pending",
                            assignee=None
                          )
    task4 = DeploymentTask(
                            task_id=4,
                            title="Clean old logs",
                            priority=1,
                            status="completed",
                            assignee="Bob"
                          )
    task5 = DeploymentTask(
                            task_id=5,
                            title="Deploy recommendation service",
                            priority=5,
                            status="pending",
                            assignee=None
                          )

    tasks = [task1, task2, task3, task4, task5]

    result = complete_task(tasks, 3)

    # assert result.status == "completed" 原本这个不对，没有验证修改的是 task3
    assert result is task3
    assert task3.status == "completed"


def test_complete_task_not_found() -> None:
    task1 = DeploymentTask(
                            task_id=1,
                            title="Deploy login service",
                            priority=3,
                            status="pending",
                            assignee=None
                          )
    task2 = DeploymentTask(
                            task_id=2,
                            title="Fix payment bug",
                            priority=5,
                            status="in_progress",
                            assignee="Alice"
                          )
    task3 = DeploymentTask(
                            task_id=3,
                            title="Update database schema",
                            priority=4,
                            status="pending",
                            assignee=None
                          )
    task4 = DeploymentTask(
                            task_id=4,
                            title="Clean old logs",
                            priority=1,
                            status="completed",
                            assignee="Bob"
                          )
    task5 = DeploymentTask(
                            task_id=5,
                            title="Deploy recommendation service",
                            priority=5,
                            status="pending",
                            assignee=None
                          )

    tasks = [task1, task2, task3, task4, task5]

    with pytest.raises(TaskNotFoundError):
        complete_task(tasks, 6)


def test_complete_task_completed() -> None:
    task1 = DeploymentTask(
                            task_id=1,
                            title="Deploy login service",
                            priority=3,
                            status="pending",
                            assignee=None
                          )
    task2 = DeploymentTask(
                            task_id=2,
                            title="Fix payment bug",
                            priority=5,
                            status="in_progress",
                            assignee="Alice"
                          )
    task3 = DeploymentTask(
                            task_id=3,
                            title="Update database schema",
                            priority=4,
                            status="pending",
                            assignee=None
                          )
    task4 = DeploymentTask(
                            task_id=4,
                            title="Clean old logs",
                            priority=1,
                            status="completed",
                            assignee="Bob"
                          )
    task5 = DeploymentTask(
                            task_id=5,
                            title="Deploy recommendation service",
                            priority=5,
                            status="pending",
                            assignee=None
                          )

    tasks = [task1, task2, task3, task4, task5]

    with pytest.raises(InvalidTaskOperationError):
        complete_task(tasks, 4)


# Part 4：Business Rule 和 Python 默认行为不是一回事
def test_assign_task() -> None:
    task1 = DeploymentTask(
                            task_id=1,
                            title="Deploy login service",
                            priority=3,
                            status="pending",
                            assignee=None
                          )
    task2 = DeploymentTask(
                            task_id=2,
                            title="Fix payment bug",
                            priority=5,
                            status="in_progress",
                            assignee="Alice"
                          )
    task3 = DeploymentTask(
                            task_id=3,
                            title="Update database schema",
                            priority=4,
                            status="pending",
                            assignee=None
                          )
    task4 = DeploymentTask(
                            task_id=4,
                            title="Clean old logs",
                            priority=1,
                            status="completed",
                            assignee="Bob"
                          )
    task5 = DeploymentTask(
                            task_id=5,
                            title="Deploy recommendation service",
                            priority=5,
                            status="pending",
                            assignee=None
                          )

    tasks = [task1, task2, task3, task4, task5]

    result = assign_task(tasks, 5, "Bob")

    assert result is task5  # 一开始写的==，用is更好
    assert task5.status == "in_progress"
    assert task5.assignee == "Bob"


def test_assign_task_not_found() -> None:
    task1 = DeploymentTask(
                            task_id=1,
                            title="Deploy login service",
                            priority=3,
                            status="pending",
                            assignee=None
                          )
    task2 = DeploymentTask(
                            task_id=2,
                            title="Fix payment bug",
                            priority=5,
                            status="in_progress",
                            assignee="Alice"
                          )
    task3 = DeploymentTask(
                            task_id=3,
                            title="Update database schema",
                            priority=4,
                            status="pending",
                            assignee=None
                          )
    task4 = DeploymentTask(
                            task_id=4,
                            title="Clean old logs",
                            priority=1,
                            status="completed",
                            assignee="Bob"
                          )
    task5 = DeploymentTask(
                            task_id=5,
                            title="Deploy recommendation service",
                            priority=5,
                            status="pending",
                            assignee=None
                          )

    tasks = [task1, task2, task3, task4, task5]

    with pytest.raises(TaskNotFoundError):
        assign_task(tasks, 6, "Bob")


def test_assign_task_empty_assignee() -> None:
    task1 = DeploymentTask(
                            task_id=1,
                            title="Deploy login service",
                            priority=3,
                            status="pending",
                            assignee=None
                          )
    task2 = DeploymentTask(
                            task_id=2,
                            title="Fix payment bug",
                            priority=5,
                            status="in_progress",
                            assignee="Alice"
                          )
    task3 = DeploymentTask(
                            task_id=3,
                            title="Update database schema",
                            priority=4,
                            status="pending",
                            assignee=None
                          )
    task4 = DeploymentTask(
                            task_id=4,
                            title="Clean old logs",
                            priority=1,
                            status="completed",
                            assignee="Bob"
                          )
    task5 = DeploymentTask(
                            task_id=5,
                            title="Deploy recommendation service",
                            priority=5,
                            status="pending",
                            assignee=None
                          )

    tasks = [task1, task2, task3, task4, task5]

    with pytest.raises(ValueError):
        assign_task(tasks, 5, "")


def test_assign_task_empty_assignee2() -> None:
    task1 = DeploymentTask(
                            task_id=1,
                            title="Deploy login service",
                            priority=3,
                            status="pending",
                            assignee=None
                          )
    task2 = DeploymentTask(
                            task_id=2,
                            title="Fix payment bug",
                            priority=5,
                            status="in_progress",
                            assignee="Alice"
                          )
    task3 = DeploymentTask(
                            task_id=3,
                            title="Update database schema",
                            priority=4,
                            status="pending",
                            assignee=None
                          )
    task4 = DeploymentTask(
                            task_id=4,
                            title="Clean old logs",
                            priority=1,
                            status="completed",
                            assignee="Bob"
                          )
    task5 = DeploymentTask(
                            task_id=5,
                            title="Deploy recommendation service",
                            priority=5,
                            status="pending",
                            assignee=None
                          )

    tasks = [task1, task2, task3, task4, task5]

    with pytest.raises(ValueError):
        assign_task(tasks, 5, "   ")


def test_assign_task_empty_completed() -> None:
    task1 = DeploymentTask(
                            task_id=1,
                            title="Deploy login service",
                            priority=3,
                            status="pending",
                            assignee=None
                          )
    task2 = DeploymentTask(
                            task_id=2,
                            title="Fix payment bug",
                            priority=5,
                            status="in_progress",
                            assignee="Alice"
                          )
    task3 = DeploymentTask(
                            task_id=3,
                            title="Update database schema",
                            priority=4,
                            status="pending",
                            assignee=None
                          )
    task4 = DeploymentTask(
                            task_id=4,
                            title="Clean old logs",
                            priority=1,
                            status="completed",
                            assignee="Bob"
                          )
    task5 = DeploymentTask(
                            task_id=5,
                            title="Deploy recommendation service",
                            priority=5,
                            status="pending",
                            assignee=None
                          )

    tasks = [task1, task2, task3, task4, task5]

    with pytest.raises(InvalidTaskOperationError):
        assign_task(tasks, 4, "Bob")


def test_assign_task_empty_assigned() -> None:
    task1 = DeploymentTask(
                            task_id=1,
                            title="Deploy login service",
                            priority=3,
                            status="pending",
                            assignee=None
                          )
    task2 = DeploymentTask(
                            task_id=2,
                            title="Fix payment bug",
                            priority=5,
                            status="in_progress",
                            assignee="Alice"
                          )
    task3 = DeploymentTask(
                            task_id=3,
                            title="Update database schema",
                            priority=4,
                            status="pending",
                            assignee=None
                          )
    task4 = DeploymentTask(
                            task_id=4,
                            title="Clean old logs",
                            priority=1,
                            status="completed",
                            assignee="Bob"
                          )
    task5 = DeploymentTask(
                            task_id=5,
                            title="Deploy recommendation service",
                            priority=5,
                            status="pending",
                            assignee=None
                          )

    tasks = [task1, task2, task3, task4, task5]

    with pytest.raises(InvalidTaskOperationError):
        assign_task(tasks, 2, "Bob")
