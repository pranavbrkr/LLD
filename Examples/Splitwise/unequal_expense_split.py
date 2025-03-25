from typing import List
from split import Split
from expense_split_strategy import ExpenseSplitStrategy

class UnequalExpenseSplit(ExpenseSplitStrategy):
  def validateSplitRequest(self, split_list: List[Split], total_amount: float):
    total_sum: float = 0
    for split in split_list:
      total_sum += split.getAmountOwe()
    if total_sum != total_amount:
      raise ValueError("Split amounts do not match the total answer")