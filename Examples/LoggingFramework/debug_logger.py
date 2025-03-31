from abstract_logger import AbstractLogger

class DebugLogger(AbstractLogger):
  def __init__(self, levels):
    super().__init__(levels)

  def display(self, msg, logger_subject):
    logger_subject.notifyAllObservers(1, f"DEBUG: {msg}")