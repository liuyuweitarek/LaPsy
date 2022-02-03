import pathlib
from util import *
from logger import SystemLog
from cfg import SysPaths, SysMsg, Agent

class ChatBrain:
    def __init__(self, agentid):
        self.Log = SystemLog(self.__class__.__name__, commit=agentid)  
        
        # Built/Load Agent 
        self.agent_data_path = '{0}{1}/'.format(SysPaths.USER_DATA_STORE_PATH, agentid)        
        self.agent = self.build_agent(agentid)

        self.load_script()
        
    
    def build_agent(self, agentid):
        if not pathlib.Path(self.agent_data_path).exists():
            self.Log.info(SysMsg.WELLCOME_MSG)
            pathlib.Path(self.agent_data_path).mkdir(parents=True, exist_ok=True)
            u = Agent(agentid)
            util_obj2file(u, self.agent_data_path + 'userconfig.json')
        
        else:
            self.Log.info(SysMsg.WELLCOME_BACK_MSG)
            u = util_file2obj(self.agent_data_path + 'userconfig.json')
            u.update()
            util_obj2file(u, self.agent_data_path + 'userconfig.json')
        return u
    
    def load_script(self):
        if not pathlib.Path(SysPaths.SCRIPT_FOLDER).exists():
            pathlib.Path(SysPaths.SCRIPT_FOLDER).mkdir(parents=True, exist_ok=True)

        isEmpty = not any(pathlib.Path(SysPaths.SCRIPT_FOLDER).iterdir())

        if isEmpty:
            self.Log.info(SysMsg.NO_SCRIPT_MSG)
        else:
            pass