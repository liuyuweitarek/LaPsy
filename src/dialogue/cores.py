import pathlib
import pandas as pd
from util import *
from logger import SystemLog
from cfg import SysPaths, SysMsg
from entity.agent import Agent
from dialogue.script_handdler import TwoPath_Handdler

class ChatBrain:
    def __init__(self, agentid, scripts=[]):
        self.Log = SystemLog(self.__class__.__name__, commit=agentid)  
        
        # Built/Load Agent 
        self.agent_data_path = '{0}{1}/'.format(SysPaths.USER_DATA_STORE_PATH, agentid)        
        self.agent = self.build_agent(agentid, scripts)

        self.script_handdler = TwoPath_Handdler(
            use_scripts= scripts,
            agent_data_path=self.agent_data_path, 
            log=agentid)
        
    def build_agent(self, agentid, scripts):
        if not pathlib.Path(self.agent_data_path).exists():
            self.Log.info(SysMsg.WELLCOME_MSG)
            pathlib.Path(self.agent_data_path).mkdir(parents=True, exist_ok=True)
            u = Agent(agentid,scripts)
            util_obj2file(u, self.agent_data_path + 'userconfig.json')
        
        else:
            self.Log.info(SysMsg.WELLCOME_BACK_MSG)
            u = util_file2obj(self.agent_data_path + 'userconfig.json')
            u.update()
            util_obj2file(u, self.agent_data_path + 'userconfig.json')
        
        return u
        
    def pack_brain(self):
        # Pack Agent
        util_obj2file(self.agent, self.agent_data_path + 'userconfig.json')
        # Pack Scripts 
        self.script_handdler.pack()
        return
    
    def getText(self, input_text):
        return