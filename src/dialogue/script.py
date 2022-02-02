from mimetypes import init
import pathlib
from util import *
from logger import SystemLog
from cfg import SysPaths, UserConfig

class ChatBrain:
    def __init__(self, agentid):
        self.Log = SystemLog(self.__class__.__name__, commit=agentid)  
        
        # Built/Load Agent 
        self.agent_data_path = '{0}{1}/'.format(SysPaths.USER_DATA_STORE_PATH, agentid)        
        self.agent = self.build_agent(agentid)
        
    
    def build_agent(self, agentid):
        if not pathlib.Path(self.agent_data_path).exists():
            self.Log.info("New to Lapsy! Building your script...")
            pathlib.Path(self.agent_data_path).mkdir(parents=True, exist_ok=True)
            u = UserConfig(agentid)
            util_obj2file(u, self.agent_data_path + 'userconfig.json')
        
        else:
            self.Log.info("Welcome back to Lapsy! Reloading your script...")
            u = util_file2obj(self.agent_data_path + 'userconfig.json')
        
        return u
        
        
