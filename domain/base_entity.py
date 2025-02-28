from abc import ABC
from typing import Optional


class BaseEntity(ABC):
    def __init__(self) -> None:
        self.id: Optional[int] = None
