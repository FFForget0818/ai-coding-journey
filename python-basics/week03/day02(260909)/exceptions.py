# Part 3：Custom Exception——区分“数据非法”和“业务操作失败”


class TaskNotFoundError(Exception):
    pass


class InvalidTaskOperationError(Exception):
    pass
