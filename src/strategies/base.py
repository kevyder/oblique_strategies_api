from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class Strategy:
    id: int
    translations: Dict[str, str]

    def get_text(self, lang: str = "en") -> str:
        return self.translations.get(lang, self.translations["en"])


class StrategyProvider(ABC):
    @abstractmethod
    def get_all(self) -> List[Strategy]:
        """Return all available strategies"""
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Strategy]:
        """Return a specific strategy by ID"""
        pass

    def get_random(self) -> Optional[Strategy]:
        """Return a random strategy"""
        pass
