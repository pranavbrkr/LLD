from typing import List
from split import Split
from expense_split_strategy import ExpenseSplitStrategy

class PercentageExpenseSplit(ExpenseSplitStrategy):
  def validateSplitRequest(self, split_list: List[Split], total_amount: float):
    total_percentage: float = 0
    for split in split_list:
      total_percentage += split.getAmountOwe()
    
    if total_percentage != total_amount:
      raise ValueError("Total percentage must sum up to 100%")