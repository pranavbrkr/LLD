from abc import ABC, abstractmethod

from logger_subject import LoggerSubject

class AbstractLogger(ABC):
  def __init__(self, levels: int):
    self.levels = levels
    self._next_level_logger: AbstractLogger | None = None

  def setNextLevelLogger(self, next_level_logger: 'AbstractLogger'):
    self._next_level_logger = next_level_logger
  
  def logMessage(self, levels: int, msg: str, logger_subject: 'LoggerSubject'):
    if self.levels == levels:
      self.display(msg ,logger_subject)
    if self._next_level_logger:
      self._next_level_logger.logMessage(levels, msg, logger_subject)
  
  @abstractmethod
  def display(self, msg: str, logger_subject: 'LoggerSubject'):
    pass