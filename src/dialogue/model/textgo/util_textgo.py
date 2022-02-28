from logger import SystemLog
from textgo import TextSim
class TextGoModel:
    def __init__(self, log="TEST"):
        self.Log = SystemLog(self.__class__.__name__, log)
        return