from abc import ABC, abstractmethod
from typing import Any, Optional, Dict


class Handler(ABC):
    def __init__(self, successor: Optional['Handler'] = None):
        self._successor = successor

    def set_next(self, handler: 'Handler') -> 'Handler':
        self._successor = handler
        return handler

    @abstractmethod
    def handle(self, request: Dict[str, Any]) -> Optional[str]:
        if self._successor:
            return self._successor.handle(request)
        return None


class Request:
    def __init__(self, type: str, data: Dict, metadata: Dict):
        self.type = type
        self.data = data or {}
        self.metadata = metadata or {}
        self._current_handler = None

    def add_metadata(self, key: str, value: Any):
        self.metadata[key] = value
