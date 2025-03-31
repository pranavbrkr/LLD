from info_logger import InfoLogger
from error_logger import ErrorLogger
from debug_logger import DebugLogger
from logger_subject import LoggerSubject
from console_logger import ConsoleLogger
from file_logger import FileLogger

class LogManager:
  @staticmethod
  def doChaining() -> InfoLogger:
    info_logger = InfoLogger(1)
    error_logger = ErrorLogger(2)
    debug_logger = DebugLogger(3)

    info_logger.setNextLevelLogger(error_logger)
    error_logger.setNextLevelLogger(debug_logger)

    return info_logger

  @staticmethod
  def addObservers() -> LoggerSubject:
    logger_subject = LoggerSubject()
    console_logger = ConsoleLogger()
    logger_subject.addObserver(1, console_logger)
    logger_subject.addObserver(2, console_logger)
    logger_subject.addObserver(3, console_logger)

    file_logger = FileLogger()
    logger_subject.addObserver(2, file_logger)

    return logger_subject