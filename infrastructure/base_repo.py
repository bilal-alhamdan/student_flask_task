from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, List, Optional, TypeVar

from domain.base_entity import BaseEntity  # Import the new base entity


# Define a base class or protocol that requires an 'id' attribute
class Identifiable(ABC):
    @property
    @abstractmethod
    def id(self) -> int:
        pass

    @id.setter
    @abstractmethod
    def id(self, value: int) -> None:
        pass


T = TypeVar('T', bound=BaseEntity)


class BaseRepository(Generic[T]):
    def __init__(self) -> None:
        self.data: Dict[int, T] = {}
        self._next_id: int = 1

    def get_all(self) -> List[T]:
        return list(self.data.values())

    def get_by_id(self, entity_id: int) -> Optional[T]:
        return self.data.get(entity_id)

    def add(self, entity: T) -> T:
        entity.id = self._next_id
        self.data[self._next_id] = entity
        self._next_id += 1
        return entity

    def update(self, entity_id: int,
               update_data: Dict[str, Any]) -> Optional[T]:
        entity = self.data.get(entity_id)
        if entity:
            for key, value in update_data.items():
                setattr(entity, key, value)
            return entity
        return None

    def delete(self, entity_id: int) -> Optional[T]:
        return self.data.pop(entity_id, None)
