from logger import SystemLog
class EchoBot:
    def __init__(self, log="TEST"):     
        self.Log = SystemLog(self.__class__.__name__, log)
        self.Log.info("Launch ECHO chit-chat robot...")
    
    def query(self, inputText):
        return inputText