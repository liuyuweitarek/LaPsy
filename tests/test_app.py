import os, rpyc, random, argparse
from app import AutoLoop



def test_main(recordPath):
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--record_path', type=str, default=recordPath, help="Record would be stored in here.")
    args = parser.parse_args()
    loop = AutoLoop(args)
    assert loop.main() == "."


