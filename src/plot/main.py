import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Input filename")
args = parser.parse_args()

data = []

with open(args.filename, "r") as in_file:
    for line in in_file.readlines():
        data.append(json.loads(line))

print(data)
