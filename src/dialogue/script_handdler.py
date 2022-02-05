import pathlib
import pandas as pd
from util import *
from logger import SystemLog
from cfg import SysPaths, SysMsg
from dialogue.flags import Flags

class TwoPath_Handdler:
    def __init__(self, use_scripts, agent_data_path, log="TEST"):
        self.Log = SystemLog(self.__class__.__name__, commit=log)
        self.use_scripts = use_scripts
        self.agent_data_path = agent_data_path
        
        # Load Scripts
        self.scripts_df = self.load_scripts()
        # States
        self.isDuringScript = False
        
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
        for sn in self.use_scripts:
            self.scripts_df.loc[self.scripts_df.QNAME==sn].to_csv(self.agent_data_path + 'scripts/' + sn)
        return