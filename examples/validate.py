#!/usr/bin/env python
import sys
import json
import os
import fnmatch
import zipfile
import random
import string
import shutil
import time
import getopt
from jsonschema import validate

def extractArchives():
  extractionPaths = []
  for root, dirNames, fileNames in os.walk("."):
    for fileName in fnmatch.filter(fileNames, "*.zip"):
      archivePath = os.path.join(root, fileName)
      extractionPath = os.path.join("examples", "".join(random.choice(string.ascii_lowercase) for i in range(16)))
      extractionPaths.append(extractionPath)
      print("Extracting " + archivePath + " to " + extractionPath + " ...", flush=True)
      with zipfile.ZipFile(archivePath) as zf:
        zf.extractall(extractionPath)
  
  return extractionPaths
  
def cleanExtractionPaths(extractionPaths):
  for extractionPath in extractionPaths:
    print("Deleting " + extractionPath + " ...", flush=True)
    shutil.rmtree(extractionPath)

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
        print(e, flush=True)
        badFiles.append(path)
       
  return objects, badFiles
   
def loadSchemas():
  schemaTuples, badSchemaFiles = loadAllJsonObjects("schemas")
  schemas = {}
  for path, fileName, o in schemaTuples:
    schemaName = os.path.basename(os.path.dirname(path))
    versionName = fileName[:-5]
    schemas[schemaName + "-" + versionName] = o
  
  return schemas, badSchemaFiles
    
def loadExamples():
  exampleTuples, badExampleFiles = loadAllJsonObjects("examples")
  examples = []
  for path, fileName, o in exampleTuples:
    examples.append((path, o["meta"]["type"], o["meta"]["version"], o["meta"]["id"], o))

  return examples, badExampleFiles
    
def validateExamples(examples, schemas, maxExamples, shuffle):
  failures = []
  numberOfSuccessfulValidations = 0
  unchecked = []

  numChecked = 0
  latestReportTime = time.clock()
  
  if shuffle:
    random.shuffle(examples)
  for path, type, version, id, json in examples:
    schemaKey = type + "-" + version
    if schemaKey in schemas:
      try:
        validate(json, schemas[schemaKey])
        numberOfSuccessfulValidations += 1
      except Exception as e:
        failures.append((path, type, id, e))
    else:
      unchecked.append((path, type, id, json))
    
    numChecked += 1
    
    if maxExamples > 0 and numChecked >= maxExamples:
      print("Reached limit of " + str(maxExamples) + " examples to validate. Breaking.")
      break
      
    if time.clock() - latestReportTime > 5:
      print("Checked " + str(numChecked) + " / " + str(len(examples)) + " examples.", flush=True)
      latestReportTime = time.clock()
      
  return failures, unchecked, numberOfSuccessfulValidations

def report(unchecked,failures,badSchemaFiles,badExampleFiles,numberOfSuccessfulValidations):
  for path, type, id, o in unchecked:
    print("WARNING: Missing schema for " + id + "(" + type + ") in " + path + ".", flush=True)

  for badSchemaFile in badSchemaFiles:
    print("ERROR: Failed to load schema from file", badSchemaFile, flush=True)

  for badExampleFile in badExampleFiles:
    print("ERROR: Failed to load example from file", badExampleFile, flush=True)

  for path, type, id, e in failures:
    print("ERROR: Validation failed for " + id + "(" + type + ") in " + path + ": " + str(e), flush=True)
    
  print("")
  print("===SUMMARY===")
  print("Bad schema files:        ", len(badSchemaFiles))
  print("Bad example files:       ", len(badExampleFiles))
  print("Successful validations:  ", numberOfSuccessfulValidations)
  print("Failed validations:      ", len(failures))
  print("Unchecked examples:      ", len(unchecked))
  print("=============", flush=True)
 
def main(maxExamples, includeArchives, shuffle):
  if includeArchives:
    extractionPaths = extractArchives()

  schemas, badSchemaFiles = loadSchemas()
  print("Loaded", len(schemas), "schemas.", flush=True)

  examples, badExampleFiles = loadExamples()
  print("Loaded", len(examples), "examples.", flush=True)

  failures, unchecked, numberOfSuccessfulValidations = validateExamples(examples, schemas, maxExamples, shuffle)

  if includeArchives:
    cleanExtractionPaths(extractionPaths)

  report(unchecked, failures, badSchemaFiles, badExampleFiles, numberOfSuccessfulValidations)

  if len(badSchemaFiles) > 0 or len(badExampleFiles) > 0 or len(failures) > 0:
    sys.exit("Validation failed.")

def usage():
  print("Usage:")
  print("    This script will validate .json files in the examples directory.")
  print("")
  print("Arguments:")
  print("    -m, --max-examples <number>")
  print("        Limit the maximum number of examples to validate.")
  print("    -a, --archives")
  print("        Include any archives in the validation.")
  print("        Any .zip in the examples directory will be unzipped,")
  print("        and any .json in it included in the validation.")
  print("    -s, --shuffle")
  print("        Shuffle the list of examples to validate.")
  print("        This is particularly useful when limiting the maximum")
  print("        number of examples to validate.")
  print("    -h, --help")
  print("        Print this text.")
  
maxExamples = 0
includeArchives = False
shuffle = False

try:
  opts, args = getopt.getopt(sys.argv[1:], "hm:as", ["help", "max-examples", "archives", "shuffle"])
except getopt.GetoptError:
  usage()
  sys.exit(1)
    
for opt, arg in opts:
  if opt in ("-h", "--help"):
    usage()
    sys.exit(0)
  elif opt in ("-m", "--max-examples"):
    maxExamples = int(arg)
  elif opt in ("-a", "--archives"):
    includeArchives = True
  elif opt in ("-s", "--shuffle"):
    shuffle = True
 
main(maxExamples, includeArchives, shuffle)
