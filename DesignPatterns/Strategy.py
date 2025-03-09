from abc import ABC, abstractmethod

# Strategy class
class TradingStrategy(ABC):
  @abstractmethod
  def execute_trade(self, data):
    pass


# Concrete Strategies
class MovingAverageStrategy(TradingStrategy):
  def execute_trade(self, data):
    window_size = 3
    moving_average = sum(data[-window_size:]) / window_size
    return f"Executing Moving Average Trading Strategy. Moving Average: {moving_average:.2f}"

class MeanReversionStrategy(TradingStrategy):
  def execute_trade(self, data):
    mean_value = sum(data) / len(data)
    deviation = data[-1] - mean_value
    return f"Executing Mean Reversion Trading Strategy. Deviation from Mean: {deviation:.2f}"


# Context
class TradingContext:
  def __init__(self, strategy):
    self._strategy = strategy
  
  def set_strategy(self, strategy):
    self._strategy = strategy
  
  def execute_trade(self, data):
    return self._strategy.execute_trade(data)
  

# Client
if __name__ == "__main__":
  trading_data = [50, 55, 45, 60, 50]

  # Create concrete strategy objects
  moving_average_strategy = MovingAverageStrategy()
  mean_reversion_strategy = MeanReversionStrategy()

  # Create context with a default strategy
  trading_context = TradingContext(moving_average_strategy)

  # Execute default strategy
  result = trading_context.execute_trade(trading_data)
  print(result)

  # Switch to different strategy at runtime
  trading_context.set_strategy(mean_reversion_strategy)

  # Execute updated strategy
  result = trading_context.execute_trade(trading_data)
  print(result)