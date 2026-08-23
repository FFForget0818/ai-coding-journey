from dataclasses import dataclass


@dataclass
class Department:
    name: str
    manager: str


@dataclass
class Employee:
    name: str
    department: Department
    score: int
    active: bool = True

    def __post_init__(self) -> None:
        if self.score < 0 or self.score > 100:
            raise ValueError("Score must be between 0 and 100")

        if self.name.strip() == "":
            raise ValueError("Name must not be blank")

    def is_pass(self) -> bool:
        return self.score >= 60

    def update_score(self, new_score: int) -> None:
        if new_score < 0 or new_score > 100:
            raise ValueError("Score must be between 0 and 100")

        self.score = new_score

    def deactivate(self) -> None:
        self.active = False

    def get_grade(self) -> str:
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "F"


def calculate_average_score(employees: list[Employee]) -> float:
    if len(employees) == 0:
        raise ValueError("Employees must not be empty")

    total_score = 0

    for employee in employees:
        total_score += employee.score

    return total_score / len(employees)


def find_highest_score_employee(
    employees: list[Employee]
) -> Employee:
    if len(employees) == 0:
        raise ValueError("Employees must not be empty")
    highest_employee = employees[0]

    for employee in employees[1:]:
        if employee.score > highest_employee.score:
            highest_employee = employee

    return highest_employee

