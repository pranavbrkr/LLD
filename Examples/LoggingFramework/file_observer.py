from log_observer import LogObserver

class FileObserver(LogObserver):
  def log(self, message: str):
    print(f"File message: {message}")