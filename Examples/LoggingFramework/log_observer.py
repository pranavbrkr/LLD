from abc import ABC, abstractmethod

class LogObserver(ABC):
  @abstractmethod
  def log(self, message: str):
    pass