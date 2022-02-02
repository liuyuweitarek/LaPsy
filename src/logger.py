import logging, os, pathlib
from datetime import datetime
from cfg import SysPaths

class SystemLog(object):
    def __init__(self, module_name, commit=None):
        if commit == None:
            now = datetime.now()
            self.commit = datetime.strftime(now,'%Y_%m_%d_%H_%M_%S')
        else:
            self.commit = commit        

        self.logger=logging.getLogger(module_name)
        self.logger.setLevel(logging.DEBUG)
        
        self.log = '{0}{1}'.format(SysPaths.LOG_PATH, self.commit)
        
        format = '%(asctime)s - %(levelname)s - %(name)s:%(lineno)d : %(message)s'
        formatter = logging.Formatter(format)
        pathlib.Path(self.log).mkdir(parents=True, exist_ok=True)

        logfile = self.log + 'history.log'
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