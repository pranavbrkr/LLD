from log_observer import LogObserver

class ConsoleObserver(LogObserver):
  def log(self, message: str):
    print(f"Console message: {message}")