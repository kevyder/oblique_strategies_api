"""
InMemoryStrategyProvider implementation.
Stores and provides access to strategies in memory.
"""

import random
from typing import List, Optional

from .base import Strategy, StrategyProvider
from .data import DEFAULT_STRATEGIES


class InMemoryStrategyProvider(StrategyProvider):
    def __init__(self, strategies: List[Strategy] = None):
        self._strategies = strategies or DEFAULT_STRATEGIES

    def get_all(self) -> List[Strategy]:
        return self._strategies

    def get_by_id(self, id: int) -> Optional[Strategy]:
        strategy_dict = {s.id: s for s in self._strategies}
        return strategy_dict.get(id)

    def get_random(self) -> Strategy:
        """Return a random strategy"""
        strategies = self.get_all()
        return random.choice(strategies)
