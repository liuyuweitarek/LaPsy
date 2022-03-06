import os, rpyc, random, argparse, sys
from logger import SystemLog
from dialogue.cores import ChatBrain
from cfg import RobotType, ChitChatType

class SpecSignals:
    EXIT = 'EXIT'

class AutoLoop:
    def __init__(self, args):
        self.Log = SystemLog(self.__class__.__name__, commit=args.agentid)
        self.agentid = args.agentid
        self.scriptlist = args.scriptlist
        self.spec_signal = "NONE"
        
        '''
        Case 1: Single Agent / Single Robot
        '''
        # Load Agent
        self.chatbrain = ChatBrain(args.agentid, args.scriptlist, args.chitchatbot)
        # Load Robot and AutoAction
        self.load_robot(args.robot)
    
    def load_robot(self, robot_type):
        if robot_type == RobotType.Zenbo:
            from robot.Zenbo.API.api import ZenboAPI
            from robot.Zenbo.action import ZenboAutoAction
            
            self.robot = ZenboAPI(log=self.agentid)
            self.action = ZenboAutoAction(self.robot)

        elif robot_type == RobotType.Kebbi:
            from robot.Kebbi.API.api import KebbiAPI
            from robot.Kebbi.action import KebbiAutoAction
            
            self.robot = KebbiAPI(log=self.agentid)
            self.action = KebbiAutoAction(self.robot)
        
        else:
            from robot.Fake.API.api import FakeAPI
            from robot.Fake.action import FakeAutoAction
            
            self.robot = FakeAPI(deafmode=False, log=self.agentid)
            self.action = FakeAutoAction(self.robot)

    def main(self):
        try:
            self.Log.info("Begin AutoLoop...")
            reply = self.action.execute(self.action.START)
            while True:
                self.Log.debug("----------Start NewLoop------------")
                if reply.text not in self.action.unrecognized_signal:
                    self.Log.debug("Recog: {0}".format(reply.text))
                    
                    brain_reply = self.chatbrain.getText(reply.text)
                    self.spec_signal = brain_reply['SPEC_PRIORITY']
                    reply = self.action.execute(brain_reply)
                else:
                    self.Log.debug("Unrecog: {0}".format(heardText))
                    heardText = input("[最外層沒聽到聲音]"+ random.choice(self.action.nosoundList) + ",請回復:")

                # Check if launching autoProcess succeed
                if not self.robot.autochat_ready():
                    self.Log.info("AutoChat Process is ready...")
                    self.robot.autochat_ready(True)  
                
                #Close window when signaled by main thread
                if self.robot.autochat_close() or self.spec_signal == SpecSignals.EXIT: 
                    self.Log.info("Close...Bye~")       
                    self.chatbrain.pack_brain()
                    break
            self.end()
            return
        except KeyboardInterrupt:
            self.chatbrain.pack_brain()
            self.Log.info("KeyInterrupt!")
            self._exit()
        except Exception as err:
            self.chatbrain.pack_brain()
            self.Log.exception("####### Exception TraceBack #######")
            self._exit()
    def end(self):
        self.chatbrain.pack_brain()
        return

    def _exit(self):
        print("Bye!~")
        try:
            sys.exit(1)
        except:
            os._exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--agentid', type=str, default="TEST", help="<String> You could find log at \'LOG/\{agentid\}\' and data at \'AGENTS/\{agentid\}\'.")
    parser.add_argument('--scriptlist', type=list, default=["basic_sequence.csv"], help="Add scripts at \'SCRIPTS/\' with the instruction in the gitbook.")
    parser.add_argument('--robot', type=str, default='fake')
    parser.add_argument('--chitchatbot', type=str, default='echo')
    args = parser.parse_args()
    loop = AutoLoop(args)
    loop.main()
