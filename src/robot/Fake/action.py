from logger import SystemLog
from robot.Fake.API.api import FakeError
from dialogue.flags import Flags
import random

class ActionReply:
    def __init__(self, **kwargs):
        for attr, val in kwargs.items():
            setattr(self, attr, val)
        

class FakeAutoAction:
    def __init__(self, client):
        self.Log = SystemLog(self.__class__.__name__, commit=client.agentid)
        
        self.client = client
        self.unrecognized_signal = FakeError.ALL()
        self.nosoundList = [
            '我好像沒聽清楚，可以麻煩你再講一次嗎',
            '對不起，我剛剛沒聽清楚',
            '回答可能可以拉長放慢一些，我能聽得更清楚喔'
        ]
        self.START = {'FROM_SCRIPT':False, 
             'SPEAK_TEXT':'你好',
             'VOLUME':100, 'SPEED':100, 'PITCH':100,
             'ACTION_TYPE':'2'}
        '''
        If you add new attrs into obj, please put their names into self.defaultKey list.
        Otherwise, they would be renewed after a new action started.
        ''' 
        self.defaultKey = ['defaultKey','client', 'unrecognized_signal','nosoundList','Log', 'START']
    
    def _deal_reply(self, reply):
        # Load keys that systems(dialogue... ) would use in the auto loop.
        allowed_keys = set([key for key,value in Flags.__dict__.items() if not key.startswith('__')])
        
        self.__dict__.update((key, False) for key in allowed_keys)
        self.__dict__.update((key, value) for key, value in reply.items() if key in allowed_keys)
    
    def _release(self):
        self.__dict__.update((key, False) for key, value in self.__dict__.items() if key not in self.defaultKey and not key.startswith('__'))
    
    def execute(self, reply):
        self._release()
        self._deal_reply(reply)
        
        if self.ACTION_TYPE == '1':
            self._only_say()
            reply = ActionReply()
            return reply
        elif self.ACTION_TYPE == '2':
            _outputText, _wavFilePath = self._say_and_listen()
            reply = ActionReply(text=_outputText, wavfile=_wavFilePath)
            return _outputText, _wavFilePath
        else:
            self.Log.debug("No action ... ?!")
            reply = ActionReply()
            return reply
    def _only_say(self):
        self.Log.debug("_only_say")
        self.client.setconfig(self.VOLUME, self.SPEED, self.PITCH)
        self.client.setexpression('DEFAULT_STILL')
        self.client.moveHead(0, 2)
        self.client.say(self.SPEAK_TEXT, listen=False)
        return 
        

    def _say_and_listen(self):
        self.Log.debug("_say_and_listen")

        def cut_response(resString):
            _res = resString.split(";")
            _outputText = _res[0]
            _wavFilePath = _res[1]
            return _outputText, _wavFilePath

        _outputText = " "
        _wavFilePath = " "

        self.client.setconfig(self.VOLUME,self.SPEED,self.PITCH)
        self.client.setexpression('DEFAULT_STILL')
        self.client.moveHead(0, 2)

        _rawResponse = self.client.say(self.SPEAK_TEXT, listen=True)
        _outputText, _wavFilePath = cut_response(_rawResponse)

        while _outputText in self.unrecognized_signal:
            self.Log.debug("Unheard Loop ... ")                
            if _outputText in self.unrecognized_signal:
                self.client.say(random.choice(self.nosoundList), listen=False)
            
            _rawResponse = self.client.say(self.SPEAK_TEXT, listen=True)
            _outputText, _wavFilePath = cut_response(_rawResponse)
            
        return _outputText, _wavFilePath
