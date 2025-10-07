from abc import ABC, abstractmethod
from typing import Optional, Iterable, Dict, Any
class ProductRepository(ABC):
    """Abstracción del repositorio de productos (capa de dominio)."""
    @abstractmethod
    def add(self, data: Dict[str, Any]) -> str: ...
    @abstractmethod
    def get(self, id: str) -> Optional[Dict[str, Any]]: ...
    @abstractmethod
    def list(self, filters: Optional[Dict[str, Any]] = None) -> Iterable[Dict[str, Any]]: ...
