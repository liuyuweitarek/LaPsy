from logging import config
from cfg import UserConfig
import jsonpickle

def test_UserConfig_Init():
    u = UserConfig('testid')
    frozen = jsonpickle.encode(u)
    thawed = jsonpickle.decode(frozen)
    assert u.id == thawed.id
    



