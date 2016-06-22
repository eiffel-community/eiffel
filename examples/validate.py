#!/usr/bin/env python
import sys
import json
import os
import fnmatch
from jsonschema import validate

def applySchema(schemaFileName):
  print("  - Applying", schemaFileName, "to ...")
  global schemas
  schemas +=1
  eventTypeName = schemaFileName[:-5]
  eventTypeDirName = "examples/events/" + eventTypeName
  with open("schemas/" + schemaFileName, "r") as f:
    schema = json.load(f)
  
  for root, dirnames, filenames in os.walk(eventTypeDirName):
    for exampleFileName in fnmatch.filter(filenames, "*.json"):
      validateExample(schema, os.path.join(root, exampleFileName))
      
def validateExample(schema, exampleFilePath):
  print("    ... ", exampleFilePath)
  global examples
  examples +=1
  exception = False
  try:
    with open(exampleFilePath, "r") as f:
      example = json.load(f)
      
    validate(example, schema)
    print("         PASS")
  except Exception as e:
    global failures
    failures += 1
    print("         FAIL:", type(e).__name__)
    print("        ", e)

failures = 0
schemas = 0
examples = 0

for root, dirNames, fileNames in os.walk("schemas"):
    for schemaFileName in fnmatch.filter(fileNames, "*.json"):
      applySchema(schemaFileName)

print("Encountered", failures, "validation failures through application of", schemas, "schemas to", examples, "examples.")

if failures > 0:
  sys.exit("Validation failed.")