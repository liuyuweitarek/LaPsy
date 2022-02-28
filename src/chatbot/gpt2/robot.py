from logger import SystemLog
class GPT2Bot:
    def __init__(self, log="TEST"):     
        self.Log = SystemLog(self.__class__.__name__, log)
        self.Log.info("Launch GPT-2 chit-chat robot...")
    
    