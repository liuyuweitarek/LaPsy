class SysPaths:
    USER_DATA_STORE_PATH = './AGENTS/'
    SCRIPT_FOLDER = './SCRIPTS/'
    LOG_PATH = './LOG/'
    

class SysMsg:
    WELLCOME_MSG = "New to Lapsy! Building your script..."
    WELLCOME_BACK_MSG = "Welcome back to Lapsy! Reloading your script..."

    NO_SCRIPT_MSG = "There is no script in the script folder. Please check script folder or the parameter \'SysPaths.SCRIPT_FOLDER.\'"


class DefaultAgent:
    id = "default"
    scripts = []
    
    
    

class Agent(object):
    '''
    Add
    You could add new attr with modifying \"__init__ parameters\" and \"DefaultAgent Object\".
    It would update the old agent's json config file automatically.
    
    e.g.
    
    class DefaultAgent:
        origin_attr = default_origin_attr
        ++ new_attr = default_new_attr
    
    class Agent:
        def __init__(self, origin_attr=DefaultAgent.origin_attr ++, new_attr=DefaultAgent.new_attr++):
            self.origin_attr = origin_attr
            ++ self.new_attr = new_attr


    <Origin userjson.config>
        {"py/object": "cfg.Agent", 
         "origin_attr": "something other than default_origin_attr"}
    
    <After adding new_attr and reloading the agent>
        {"py/object": "cfg.Agent", 
         "origin_attr": "something other than default_origin_attr",
         "new_attr": "default_new_attr"}
    '''

    def __init__(self, id=DefaultAgent.id, scripts=DefaultAgent.scripts):
        self.id = id
        self.scripts = scripts
    
    def update(self):
        for key,value in DefaultAgent.__dict__.items():
            if not key.startswith('__'):
                setattr(self, key, value) 
        return 

    


    
    
