from log_observer import LogObserver

class ConsoleLogger(LogObserver):
  def log(self, message: str):
    print(f"Console message: {message}")