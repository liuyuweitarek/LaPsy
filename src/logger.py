import logging, os

class SystemLog(object):
    def __init__(self, name):
        self.logger=logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        format = '%(asctime)s - %(levelname)s - %(name)s:%(lineno)d : %(message)s'
        formatter = logging.Formatter(format)
        
        logfile = './debug.log'
        filehandler = logging.FileHandler(logfile)
        filehandler.setFormatter(formatter)
        self.logger.addHandler(filehandler)
    def debug(self, msg):
        self.logger.debug(msg)
    def info(self, msg):
        self.logger.info(msg)
    def warning(self, msg):
        self.logger.warning(msg)
    def error(self, msg):
        self.logger.error(msg)
    def critical(self, msg):
        self.logger.critical(msg)
    def log(self, level, msg):
        self.logger.log(level, msg)
    def setLevel(self, level):
        self.logger.setLevel(level)
    def disable(self):
        logging.disable(50)