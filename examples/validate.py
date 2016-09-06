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
    examples.append((path, o["meta"]["type"], o["meta"]["id"], o))
  return examples, badExampleFiles
    
def validateExamples(examples, schemas):
  failures = []
  numberOfSuccessfulValidations = 0
  unchecked = []
  
  for path, type, id, json in examples:
    if type in schemas:
      try:
        validate(json, schemas[type])
        numberOfSuccessfulValidations += 1
      except Exception as e:
        failures.append((path, type, id, e))
    else:
      unchecked.append((path, type, id, json))
      
  return failures, unchecked, numberOfSuccessfulValidations

def report(unchecked,failures,badSchemaFiles,badExampleFiles,numberOfSuccessfulValidations):
  for path, type, id, o in unchecked:
    print("WARNING: Missing schema for " + id + "(" + type + ") in " + path + ".")

  for badSchemaFile in badSchemaFiles:
    print("ERROR: Failed to load schema from file", badSchemaFile)

  for badExampleFile in badExampleFiles:
    print("ERROR: Failed to load example from file", badExampleFile)

  for path, type, id, e in failures:
    print("ERROR: Validation failed for " + id + "(" + type + ") in " + path + ": " + str(e))
    
  print("")
  print("===SUMMARY===")
  print("Bad schema files:        ", len(badSchemaFiles))
  print("Bad example files:       ", len(badExampleFiles))
  print("Successful validations:  ", numberOfSuccessfulValidations)
  print("Failed validations:      ", len(failures))
  print("Unchecked examples:      ", len(unchecked))
  print("=============")
 
schemas, badSchemaFiles = loadSchemas()
print("Loaded", len(schemas), "schemas.")

examples, badExampleFiles = loadExamples()
print("Loaded", len(examples), "examples.")

failures, unchecked, numberOfSuccessfulValidations = validateExamples(examples, schemas)

report(unchecked, failures, badSchemaFiles, badExampleFiles, numberOfSuccessfulValidations)

if len(badSchemaFiles) > 0 or len(badExampleFiles) > 0 or len(failures) > 0:
  sys.exit("Validation failed.")