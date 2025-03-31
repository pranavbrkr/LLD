from log_manager import LogManager

class Logger:
  _instance = None
  _chain_of_logger = None
  _logger_subject = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(Logger, cls).__new__(cls)
      cls.initialize()
    return cls._instance
  
  @classmethod
  def initialize(cls):
    cls._chain_of_logger = LogManager.doChaining()
    cls._logger_subject = LogManager.addObservers()
  
  def _createLog(self, level: int, message: str):
    self._chain_of_logger.logMessage(level, message, self._logger_subject)

  def info(self, message: str):
    self._createLog(1, message)

  def error(self, message: str):
    self._createLog(2, message)

  def debug(self, message: str):
    self._createLog(3, message)