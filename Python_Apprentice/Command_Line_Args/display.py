import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-display")
args = parser.parse_args()

print(args.display)