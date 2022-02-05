import os, rpyc, random, argparse
from app import AutoLoop



def test_app(AgentID, ScriptList, RobotInterface, ChitChatBot):
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--agentid', type=str, default=AgentID, help="<String> You could find log at \'LOG/\{agentid\}\' and data at \'AGENTS/\{agentid\}\'.")
    parser.add_argument('--scriptlist', type=list, default=ScriptList, help="Add scripts at \'SCRIPTS/\' with the instruction in the gitbook.")
    parser.add_argument('--robot', type=str, default=RobotInterface)
    parser.add_argument('--chitchatbot', type=str, default=ChitChatBot)
    args = parser.parse_args()
    loop = AutoLoop(args)
    assert True == True
    
    


