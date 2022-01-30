import os, rpyc, random, argparse
from logger import SystemLog

class AutoLoop:
    def __init__(self, args):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.record_path = args.record_path
        return
    
    def main(self):
        return self.record_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--record_path', type=str, default=".", help="Record would be stored in here.")
    args = parser.parse_args()
    loop = AutoLoop(args)