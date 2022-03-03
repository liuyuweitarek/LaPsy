import pathlib
import pandas as pd
from util import *
from logger import SystemLog
from cfg import SysPaths, SysMsg
from dialogue.flags import Flags
from cfg import ChitChatType, NLPModel
from . import util_script

class TwoPath_Handdler:
    def __init__(self, use_scripts, use_bot, use_model, agent_data_path, log="TEST"):
        self.Log = SystemLog(self.__class__.__name__, commit=log)
        self.agentid = log
        self.use_scripts = use_scripts
        self.use_bot = use_bot
        self.use_model = use_model
        self.agent_data_path = agent_data_path

        
        # Load Judge Model:
        self.model = self.load_model(use_model)
        
        # Load Path_1: Scripts
        self.scripts_df = self.load_scripts()
        self.Flags = Flags()

        # Load Path_2: ChitChatBot
        self.bot = self.load_chitchat(use_bot)
        
        # States
        self.isDuringScript = False
        self.nextState = {}
    def getText(self, input_text):
        error = None
        result = {}
        # Distinguish Root or Branch
        # Branch
        if self.isDuringScript:
            self.Log.info("Into branch")
        # Root
        else:
            self.Log.info("Into root")
            error, available_scripts_df = util_script.db_find_available_root(self.scripts_df)
            error, most_similar_dict = util_script.db_eval_root(input_text, available_scripts_df,self.model)
            
        return most_similar_dict
    def load_model(self, nlp_model):
        if nlp_model == NLPModel.TEXTGO:
            from dialogue.model.textgo.util_textgo import TextGoModel
            return TextGoModel(log=self.agentid)

    def load_chitchat(self, chitchat_type):
        if chitchat_type == ChitChatType.GPT_2:
            from chatbot.gpt2.robot import GPT2Bot
            return GPT2Bot(log=self.agentid)
        else:
            from chatbot.echo.robot import EchoBot 
            return EchoBot(log=self.agentid)


    def load_scripts(self):
        latest_columns = [key for key,value in Flags.__dict__.items() if not key.startswith('__') and key != 'QNAME']  
        
        # Check System Scripts
        sysScriptFolderIsEmpty = not any(pathlib.Path(SysPaths.SCRIPT_FOLDER).iterdir())
        if sysScriptFolderIsEmpty:
            self.Log.info(SysMsg.NO_SCRIPT_MSG)
            return pd.DataFrame(columns=latest_columns)
        
        # New Agent: Load scripts from sys folder 
        if not pathlib.Path(self.agent_data_path+'scripts/').exists():
            self.Log.info("Load scripts from system script path.")
            # Build new folder store script records
            pathlib.Path(self.agent_data_path+'scripts/').mkdir(parents=True, exist_ok=True)
            
            # Assign system script path
            path = SysPaths.SCRIPT_FOLDER
        else:
            self.Log.info("Load scripts from agent script path.")
            # Assign agent script folder path
            path = self.agent_data_path+'scripts/'
        
        _ = {}
        script_df = {}
    
        for script_name in self.use_scripts:
            if script_name in [sn.name for sn in list(pathlib.Path(path).rglob('*.csv'))]:
                _[script_name] = pd.read_csv( 
                "{0}{1}".format(SysPaths.SCRIPT_FOLDER,script_name), 
                names=latest_columns,
                usecols=latest_columns,
                encoding = "big5",
                dtype=str,
                skip_blank_lines=True)
            _[script_name] = _[script_name].dropna(axis=0)
            _[script_name]["QNAME"] = script_name
        return pd.concat([df for __ , df in _.items()],axis=0, ignore_index=True)

    def pack(self):
        self.Log.info("Pack User Record to: {}".format(self.agent_data_path+'scripts/'))
        for sn in self.use_scripts:
            self.scripts_df.loc[self.scripts_df.QNAME==sn].to_csv(self.agent_data_path + 'scripts/' + sn)
        return