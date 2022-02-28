import pathlib
import pandas as pd
from util import *
from logger import SystemLog
from cfg import SysPaths, SysMsg
from entity.agent import Agent
from dialogue.script_handdler import TwoPath_Handdler

class ChatBrain:
    def __init__(self, agentid="TEST", scripts=[], chitchatbot='echo', model="textgo"):
        self.Log = SystemLog(self.__class__.__name__, commit=agentid)  
        
        # Built/Load Agent 
        self.agent_data_path = '{0}{1}/'.format(SysPaths.USER_DATA_STORE_PATH, agentid)        
        self.agent = self.build_agent(agentid, scripts)

        self.load_strategy(name="twopath", chitchatbot=chitchatbot, model=model)
        
    def load_strategy(self, **strategy):
        if strategy.get('name',"twopath") == "twopath":
            self.Log.info("Using Two path Strategy")
            self.strategy_handler = TwoPath_Handdler(
                                        use_scripts=self.agent.scripts,
                                        use_bot = strategy.get('chitchatbot', 'echo'),
                                        use_model = strategy.get('model','textgo'),
                                        agent_data_path=self.agent_data_path, 
                                        log=self.agent.id)

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
        self.strategy_handler.pack()
        return
    
    def getText(self, input_text):
        self.strategy_handler.getText(input_text)
        return