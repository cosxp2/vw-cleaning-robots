from abc import ABC, abstractmethod
from domain.position import Position

class WorkspaceShape(ABC):
    @abstractmethod
    def is_valid_position(self, position: Position) -> bool:
        """Check if a position is inside the workspace boundaries"""
        pass