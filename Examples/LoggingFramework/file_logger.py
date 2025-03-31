from log_observer import LogObserver

class FileLogger(LogObserver):
  def log(self, message: str):
    print(f"File message: {message}")