from abc import ABC, abstractmethod
from typing import List
from split import Split

class ExpenseSplitStrategy(ABC):
  @abstractmethod
  def validateSplitRequest(self, split_list: List[Split], total_amount: float):
    pass