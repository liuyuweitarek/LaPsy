from dialogue.cores import Agent
import jsonpickle

def test_UserConfig_Init():
    u = Agent('testid')
    frozen = jsonpickle.encode(u)
    thawed = jsonpickle.decode(frozen)
    assert u.id == thawed.id
    



