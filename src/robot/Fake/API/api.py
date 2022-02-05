import random
import logging
import enum
from logger import SystemLog

class ChatMaster:
    def __init__(self):
        self.autochat_ready = False
        self.autochat_close = False

class StrEnum(str, enum.Enum):
    pass

class FakeError(StrEnum):
    CSR_ERROR = "CSR_Error"
    TIMEOUT = "TIMEOUT"

    def ALL():
        return [ e.value for e in FakeError ]  

class FakeAPI:
    def __init__(self, deafmode=False, log="TEST"):
        self.Log = SystemLog(self.__class__.__name__, log)
        self.Log.debug("Connect to pseudo test robot interface...")
        self.chatMaster = ChatMaster()
        self.deafmode = deafmode
        
        if self.deafmode:
            self.possible_heard_result = FakeError.ALL()
        else:
            self.possible_heard_result = []
        
    def setexpression(self, expression):
        self.Log.debug("Set expression: {0}".format(expression))
        return
    def setconfig(self, volume, speed, pitch):
        self.Log.debug("Set Speak Config: {0}/{1}/{2}".format(volume, speed, pitch))
        return
    def moveHead(self, angle, speed):
        self.Log.debug("Set Speak Config: {0}/{1}".format(angle, speed))        
        return
    def say(self, speakText, listen):
        self.Log.info("Robot will say: {0}".format(speakText))        
        
        _possible_heard_result=[]
        _possible_heard_result += self.possible_heard_result
        if listen:                
            heard_sentence = input("you say:")
            _possible_heard_result.append(heard_sentence)
            
            if self.deafmode:
                self.Log.debug("Random choose robot heard from {0}".format(_possible_heard_result))
            
            _reply = random.choice(_possible_heard_result)
        
            self.Log.info("Robot heard: {0}".format(_reply))
        else:
            _reply = "Not listening, keep speaking."                
        return _reply
        
    def autochat_ready(self, state=None):
        if state is not None:
            self.chatMaster.autochat_ready = state
        return self.chatMaster.autochat_ready
    def autochat_close(self, state=None):
        if state is not None:
            self.chatMaster.autochat_close = state
        return self.chatMaster.autochat_close