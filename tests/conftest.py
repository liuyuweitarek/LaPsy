from pytest import fixture

def pytest_addoption(parser):
    parser.addoption(
        '--agentid',
        default='TEST',
        action='store'
    )

    parser.addoption(
        '--scriptlist',
        default=['basic_sequence.csv'],
        action='store'
    )

    parser.addoption(
        '--robot',
        default='fake',
        action='store'
    )

    parser.addoption(
        '--chitchatbot',
        default='echo',
        action='store'
    )
    
@fixture()
def AgentID(request):
    return request.config.getoption('--agentid')

@fixture()
def ScriptList(request):
    return request.config.getoption('--scriptlist')

@fixture()
def RobotInterface(request):
    return request.config.getoption('--robot')

@fixture()
def ChitChatBot(request):
    return request.config.getoption('--chitchatbot')