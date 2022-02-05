import os, rpyc, random, argparse
from logger import SystemLog
from dialogue.cores import ChatBrain
from cfg import RobotType, ChitChatType

class AutoLoop:
    def __init__(self, args):
        self.Log = SystemLog(self.__class__.__name__, commit=args.agentid)
        self.agentid = args.agentid
        self.scriptlist = args.scriptlist
        # Case 1: Single Agent / Single Robot
        # Load Agent
        self.brain = ChatBrain(args.agentid, args.scriptlist)

        # Load Robot and AutoAction
        self.load_robot(args.robot)
        
        # Load Chit Chat Bot
        self.load_chitchat(args.chitchatbot)
    
    def load_robot(self, robot_type):
        if robot_type == RobotType.Zenbo:
            from robot.Zenbo.API.api import ZenboAPI
            from robot.Zenbo.action import ZenboAutoAction
            
            self.robot = ZenboAPI(log=self.agentid)
            self.action = ZenboAutoAction()

        elif robot_type == RobotType.Kebbi:
            from robot.Kebbi.API.api import KebbiAPI
            from robot.Kebbi.action import KebbiAutoAction
            
            self.robot = KebbiAPI(log=self.agentid)
            self.action = KebbiAutoAction(self.robot)
        
        else:
            from robot.Fake.API.api import FakeAPI
            from robot.Fake.action import FakeAutoAction
            
            self.robot = FakeAPI(deafmode=False, log=self.agentid)
            self.action = FakeAutoAction()

    def load_chitchat(self, chitchat_type):
        if chitchat_type == ChitChatType.GPT_2:
            from chatbot.gpt2.robot import GPT2Bot
            return GPT2Bot(log=self.agentid)
        else:
            from chatbot.echo.robot import EchoBot 
            return EchoBot(log=self.agentid)

    def main(self):
        self.Log.info("Begin AutoLoop...")

        while True:
            self.Log.debug("----------Start NewLoop------------")
            text = input("please type:")
            if text == "q":
                self.robot.autochat_close(True) 

            # Check if launching autoProcess succeed
            if not self.robot.autochat_ready():
                self.Log.info("AutoChat Process is ready...")
                self.robot.autochat_ready(True)  
            
            #Close window when signaled by main thread
            if self.robot.autochat_close(): 
                self.Log.info("Close...Bye~")       
                self.brain.pack_brain()
                break
        self.end()
        return 

    def end(self):
        self.brain.pack_brain()
        return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--agentid', type=str, default="TEST", help="<String> You could find log at \'LOG/\{agentid\}\' and data at \'AGENTS/\{agentid\}\'.")
    parser.add_argument('--scriptlist', type=list, default=["basic_sequence.csv"], help="Add scripts at \'SCRIPTS/\' with the instruction in the gitbook.")
    parser.add_argument('--robot', type=str, default='fake')
    parser.add_argument('--chitchatbot', type=str, default='echo')
    args = parser.parse_args()
    loop = AutoLoop(args)
    loop.main()