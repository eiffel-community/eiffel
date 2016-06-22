#!/usr/bin/env python
from __future__ import print_function
import fnmatch
import os
import json
import sys

print("Search for json files...")
files = []
for root, dirnames, filenames in os.walk('.'):
    for filename in fnmatch.filter(filenames, '*.json'):
        files.append(os.path.join(root, filename))

for file in files:
  print("Validating {}... ".format(file), end="")
  with open(file, 'r') as myfile:
    data=myfile.read()#.replace('\n', '')
  try:
    json.loads(data)
  except Exception as e:
    print("\n{}".format(data))
    print(e)
    sys.exit(1)
  print("Ok")
