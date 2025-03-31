from collections import defaultdict
from typing import Dict, List
from log_observer import LogObserver

class LoggerSubject:
  def __init__(self):
    self.log_observers: Dict[int, List[LogObserver]] = defaultdict(list)
  
  def addObserver(self, level: int, log_observer: LogObserver):
    self.log_observers[level].append(log_observer)
  
  def removeObserver(self, log_observer: LogObserver):
    for observers in self.log_observers.values():
      if log_observer in observers:
        observers.remove(log_observer)
  
  def notifyAllObservers(self, level: int, message: str):
    for lvl, observers in self.log_observers.items():
      if level == lvl:
        for observer in observers:
          observer.log(message)