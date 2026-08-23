# 数据是什么
# Exercise 1 — 拆 Models

from dataclasses import dataclass

@dataclass()
class Department:
    name: str
    manager: str

@dataclass()
class Employee:
    name: str
    department: Department
    score: int
    active: bool = True # 这里忘记先hint typing 还是先赋值了

    def __post_init__(self) -> None:
        if self.name.strip() == "":
            raise ValueError("Name must not be empty!")

        if self.score < 0 or self.score > 100:
            raise ValueError("Score mush between 0 and 100!")

    def is_pass(self) -> bool:
        return self.score >= 60

    def update_score(self, new_score: int) -> None:
        if new_score < 0 or new_score > 100:
            raise ValueError("Score mush between 0 and 100!")
        else: # 不太确定这里要不要else，好像差不多的？
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

    def get_summary(self) -> str:
        summary = f"{self.name} is worked in {self.department.name} managed by {self.department.manager} and has a score of {self.score}."
        return summary

