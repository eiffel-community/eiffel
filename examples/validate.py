#!/usr/bin/env python
import sys
import json
import os
import fnmatch
from jsonschema import validate

def loadAllJsonObjects(dir):
  objects = []
  badFiles = []

  for root, dirNames, fileNames in os.walk(dir):
    for fileName in fnmatch.filter(fileNames, "*.json"):
      try:
        path = os.path.join(root, fileName)
        with open(path, "r") as f:
          loadedObject = json.load(f)
          if(isinstance(loadedObject, list)):
            for o in loadedObject:
              objects.append((path, fileName, o))
          else:
            objects.append((path, fileName, loadedObject))
      except Exception as e:
        print(e)
        badFiles.append(path)
       
  return objects, badFiles
   
def loadSchemas():
  schemaTuples, badSchemaFiles = loadAllJsonObjects("schemas")
  schemas = {}
  for path, fileName, o in schemaTuples:
    schemas[fileName[:-5]] = o
  return schemas, badSchemaFiles
    
def loadExamples():
  exampleTuples, badExampleFiles = loadAllJsonObjects("examples")
  examples = []
  for path, fileName, o in exampleTuples:
    examples.append((path, o["meta"]["type"], o))
  return examples, badExampleFiles
    
def validateExamples(examples, schemas):
  failures = []
  unchecked = []
  
  for path, type, json in examples:
    if type in schemas:
      try:
        validate(json, schemas[type])
      except Exception as e:
        failures.append((path, type, e))
    else:
      unchecked.append((path, type, json))
      
  return failures, unchecked

def report(unchecked,failures,badSchemaFiles,badExampleFiles):
  for path, type, o in unchecked:
    print("WARNING: Missing schema for type",type,"in file",path)

  for badSchemaFile in badSchemaFiles:
    print("ERROR: Failed to load schema from file", badSchemaFile)

  for badExampleFile in badExampleFiles:
    print("ERROR: Failed to load example from file", badExampleFile)

  for path, type, e in failures:
    print("ERROR: Validation failed for", type, "in", path, ":", e)
    
  print("")
  print("===SUMMARY===")
  print("Bad schema files:  ", len(badSchemaFiles))
  print("Bad example files: ", len(badExampleFiles))
  print("Failed validations:", len(failures))
  print("Unchecked examples:", len(unchecked))
  print("=============")
 
schemas, badSchemaFiles = loadSchemas()
print("Loaded", len(schemas), "schemas.")

examples, badExampleFiles = loadExamples()
print("Loaded", len(examples), "examples.")

failures, unchecked = validateExamples(examples, schemas)

report(unchecked,failures,badSchemaFiles,badExampleFiles)

if len(badSchemaFiles) > 0 or len(badExampleFiles) > 0 or len(failures) > 0:
  sys.exit("Validation failed.")