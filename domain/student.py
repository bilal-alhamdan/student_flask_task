from typing import Any, Dict

from domain.base_entity import BaseEntity


class Student(BaseEntity):
    def __init__(self, name: str, age: int, grade: str) -> None:
        super().__init__()
        self.name: str = name
        self.age: int = age
        self.grade: str = grade

    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id,
                'name': self.name,
                'age': self.age,
                'grade': self.grade}
