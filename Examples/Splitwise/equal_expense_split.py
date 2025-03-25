from typing import List
from split import Split
from expense_split_strategy import ExpenseSplitStrategy

class EqualExpenseSplit(ExpenseSplitStrategy):
  def validateSplitRequest(self, split_list: List[Split], total_amount: float):
    amount_should_be_present: float = total_amount / len(split_list)
    for split in split_list:
      if split.getAmountOwe() != amount_should_be_present:
        raise ValueError("Each person should have equal split")