import json
import uuid
import time
import getopt
import sys
import random

def generateGenericMeta(type, t, v):
  return {"type": type, "id": str(uuid.uuid4()), "time": t, "domainId": "example.domain", "version": v}

def link(source, target, name):
  if not target:
    return

  source["links"][name] = target["meta"]["id"]

def linka(source, target, name):
  if not target:
    return
  if not name in source["links"]:
    source["links"][name] = []

  source["links"][name].append(target["meta"]["id"])

def generateGenericMessage(type, t, v, name, iteration):
  meta = generateGenericMeta(type, t, v)
  data = {"optionalParameters": [{"name": "name", "value": name}, {"name": "iteration", "value": iteration}]}
  links = {}
  msg = {}
  msg["meta"] = meta
  msg["data"] = data
  msg["links"] = links
  return msg

def findLatestPrevious(iterationsMap, currentIteration, name):
  for it in range(currentIteration - 1, -1, -1):
    if it in iterationsMap:
      if name in iterationsMap[it]:
        return iterationsMap[it][name]

def randomizeVerdict(chanceOfSuccess):
  if random.random() < chanceOfSuccess:
    return "SUCCESS"
  else:
    return "FAILURE"

def getOutcomeValuesFromVerdicts(testCaseFinishedEventsArray, positiveName, negativeName):
  for tcfEvent in testCaseFinishedEventsArray:
    if tcfEvent["data"]["outcome"]["verdict"] != "SUCCESS":
      return negativeName

  return positiveName

def generateSCC1(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelSourceChangeCreatedEvent", t, "1.0", "SCC1", iteration)
  link(msg, findLatestPrevious(iterationsMap, iteration, "SCS1"), "base")

  msg["data"]["gitIdentifier"] = {"commitId": "fd090b60a4aedc5161da9c035a49b14a319829c5", "branch": "topic-branch-" + str(iteration), "repoName": "myRepo", "repoUri": "https://repo.com"}
  msg["data"]["author"] = {"name": "John Doe", "email": "john.doe@company.com", "id": "johnxxx", "group": "Team Gophers"}
  msg["data"]["change"] = {"files": "https://filelist.com/" + str(iteration), "insertions": random.randint(10, 500), "deletions": random.randint(10, 500)}

  return msg

def generateSCS1(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelSourceChangeSubmittedEvent", t, "1.0", "SCS1", iteration)
  linka(msg, findLatestPrevious(iterationsMap, iteration, "SCS1"), "previousVersions")
  if "SCC1" in iterationsMap[iteration]:
    link(msg, iterationsMap[iteration]["SCC1"], "change")

  msg["data"]["gitIdentifier"] = {"commitId": "fd090b60a4aedc5161da9c035a49b14a319829b4", "branch": "master", "repoName": "myRepo", "repoUri": "https://repo.com"}
  msg["data"]["submitter"] = {"name": "John Doe", "email": "john.doe@company.com", "id": "johnxxx", "group": "Team Gophers"}

  return msg

def generateEDef1(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelEnvironmentDefinedEvent", t, "1.0", "EDef1", iteration)
  return msg

def generateEDef2(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelEnvironmentDefinedEvent", t, "1.0", "EDef2", iteration)
  return msg

def generateArtC3(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelArtifactCreatedEvent", t, "1.0", "ArtC3", iteration)
  msg["data"]["gav"] = {"groupId": "com.othercompany.library", "artifactId": "third-party-library", "version": "3.2.4"}
  msg["data"]["fileInformation"] = [{"classifier": "", "extension": "jar"}]
  return msg

def generateCDef1(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelCompositionDefinedEvent", t, "1.0", "CDef1", iteration)
  linka(msg, findLatestPrevious(iterationsMap, iteration, "CDef1"), "previousVersions")
  linka(msg, iterationsMap[iteration]["CLM2"], "causes")
  linka(msg, iterationsMap[iteration]["ArtC2"], "elements")
  linka(msg, iterationsMap[0]["ArtC3"], "elements")
  return msg

def generateCDef2(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelCompositionDefinedEvent", t, "1.0", "CDef2", iteration)
  linka(msg, findLatestPrevious(iterationsMap, iteration, "CDef2"), "previousVersions")
  link(msg, iterationsMap[iteration]["ActT4"], "context")
  linka(msg, findLatestPrevious(iterationsMap, iteration + 1, "ArtCC1"), "elements")
  linka(msg, findLatestPrevious(iterationsMap, iteration + 1, "ArtCC2"), "elements")
  linka(msg, findLatestPrevious(iterationsMap, iteration + 1, "ArtCC3"), "elements")
  return msg

def generateCDef3(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelCompositionDefinedEvent", t, "1.0", "CDef3", iteration)
  linka(msg, findLatestPrevious(iterationsMap, iteration, "CDef3"), "previousVersions")
  linka(msg, iterationsMap[iteration]["SCS1"], "elements")
  return msg

def generateArtC1(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelArtifactCreatedEvent", t, "1.0", "ArtC1", iteration)
  link(msg, iterationsMap[iteration]["CDef1"], "composition")
  link(msg, iterationsMap[0]["EDef1"], "environment")
  linka(msg, iterationsMap[iteration]["CDef1"], "causes")
  linka(msg, findLatestPrevious(iterationsMap, iteration, "ArtC1"), "previousVersions")
  msg["data"]["gav"] = {"groupId": "com.mycompany.myproduct", "artifactId": "complete-system", "version": "1." + str(iteration) + ".0"}
  msg["data"]["fileInformation"] = [{"classifier": "", "extension": "jar"}]
  return msg

def generateArtC2(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelArtifactCreatedEvent", t, "1.0", "ArtC2", iteration)
  link(msg, iterationsMap[iteration]["CDef2"], "composition")
  link(msg, iterationsMap[0]["EDef2"], "environment")
  linka(msg, findLatestPrevious(iterationsMap, iteration, "ArtC2"), "previousVersions")
  link(msg, iterationsMap[iteration]["ActT4"], "context")
  msg["data"]["gav"] = {"groupId": "com.mycompany.myproduct", "artifactId": "sub-system", "version": "1." + str(iteration) + ".0"}
  msg["data"]["fileInformation"] = [{"classifier": "", "extension": "jar"}]
  return msg

def generateArtCC1(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelArtifactCreatedEvent", t, "1.0", "ArtCC1", iteration)
  link(msg, iterationsMap[iteration]["CDef3"], "composition")
  linka(msg, iterationsMap[iteration]["CDef3"], "causes")
  linka(msg, findLatestPrevious(iterationsMap, iteration, "ArtCC1"), "previousVersions")
  msg["data"]["gav"] = {"groupId": "com.mycompany.myproduct", "artifactId": "component-1", "version": "1." + str(iteration) + ".0"}
  msg["data"]["fileInformation"] = [{"classifier": "", "extension": "jar"}]
  return msg

def generateArtCC2(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelArtifactCreatedEvent", t, "1.0", "ArtCC2", iteration)
  link(msg, iterationsMap[iteration]["CDef3"], "composition")
  linka(msg, iterationsMap[iteration]["CDef3"], "causes")
  linka(msg, findLatestPrevious(iterationsMap, iteration, "ArtCC2"), "previousVersions")
  msg["data"]["gav"] = {"groupId": "com.mycompany.myproduct", "artifactId": "component-2", "version": "1." + str(iteration) + ".0"}
  msg["data"]["fileInformation"] = [{"classifier": "", "extension": "jar"}]
  return msg

def generateArtCC3(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelArtifactCreatedEvent", t, "1.0", "ArtCC3", iteration)
  link(msg, iterationsMap[iteration]["CDef3"], "composition")
  linka(msg, iterationsMap[iteration]["CDef3"], "causes")
  linka(msg, findLatestPrevious(iterationsMap, iteration, "ArtCC3"), "previousVersions")
  msg["data"]["gav"] = {"groupId": "com.mycompany.myproduct", "artifactId": "component-3", "version": "1." + str(iteration) + ".0"}
  msg["data"]["fileInformation"] = [{"classifier": "", "extension": "jar"}]
  return msg

def generateArtP1(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelArtifactPublishedEvent", t, "1.0", "ArtP1", iteration)
  link(msg, iterationsMap[iteration]["ArtC1"], "artifact")
  linka(msg, iterationsMap[iteration]["ArtC1"], "causes")
  msg["data"]["locations"] =  [{"type": "PLAIN", "uri": "https://myrepository.com/myCompleteSystemArtifact"}]
  return msg

def generateArtP2(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelArtifactPublishedEvent", t, "1.0", "ArtP2", iteration)
  link(msg, iterationsMap[iteration]["ArtC2"], "artifact")
  link(msg, iterationsMap[iteration]["ActT4"], "context")
  msg["data"]["locations"] =  [{"type": "PLAIN", "uri": "https://myrepository.com/mySubSystemArtifact"}]
  return msg

def generateActT3(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelActivityTriggeredEvent", t, "1.0", "ActT3", iteration)
  linka(msg, iterationsMap[iteration]["ArtP2"], "causes")
  msg["data"]["name"] = "Act3"
  msg["data"]["category"] = "Sub-system Test Activity"
  msg["data"]["triggers"] = [{"type": "EIFFEL_EVENT"}],
  msg["data"]["executionType"] = "AUTOMATED"
  return msg

def generateActS3(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelActivityStartedEvent", t, "1.0", "ActS3", iteration)
  link(msg, iterationsMap[iteration]["ActT3"], "activityExecution")
  return msg

def generateActF3(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelActivityFinishedEvent", t, "1.0", "ActF3", iteration)
  link(msg, iterationsMap[iteration]["ActT3"], "activityExecution")
  msg["data"]["outcome"] = {"conclusion": getOutcomeValuesFromVerdicts([iterationsMap[iteration]["TSF1"]], "SUCCESSFUL", "UNSUCCESSFUL")}

  return msg

def generateActT4(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelActivityTriggeredEvent", t, "1.0", "ActT4", iteration)
  if "ArtCC1" in iterationsMap[iteration]:
    linka(msg,  iterationsMap[iteration]["ArtCC1"], "causes")
  if "ArtCC2" in iterationsMap[iteration]:
    linka(msg,  iterationsMap[iteration]["ArtCC2"], "causes")
  if "ArtCC3" in iterationsMap[iteration]:
    linka(msg,  iterationsMap[iteration]["ArtCC3"], "causes")
  msg["data"]["name"] = "Act4"
  msg["data"]["category"] = "Sub-system Build Activity"
  msg["data"]["triggers"] = [{"type": "EIFFEL_EVENT"}],
  msg["data"]["executionType"] = "AUTOMATED"
  return msg

def generateActS4(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelActivityStartedEvent", t, "1.0", "ActS4", iteration)
  link(msg, iterationsMap[iteration]["ActT4"], "activityExecution")
  return msg

def generateActF4(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelActivityFinishedEvent", t, "1.0", "ActF4", iteration)
  link(msg, iterationsMap[iteration]["ActT4"], "activityExecution")
  if "ArtC2" in iterationsMap[iteration]:
    msg["data"]["outcome"] = {"conclusion": "SUCCESSFUL"}
  else:
    msg["data"]["outcome"] = {"conclusion": "UNSUCCESSFUL"}

  return msg

def generateActT1(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelActivityTriggeredEvent", t, "1.0", "ActT1", iteration)
  linka(msg, iterationsMap[iteration]["ArtP1"], "causes")
  msg["data"]["name"] = "Act1"
  msg["data"]["category"] = "Test Activity"
  msg["data"]["triggers"] = [{"type": "EIFFEL_EVENT"}],
  msg["data"]["executionType"] = "AUTOMATED"
  return msg

def generateActS1(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelActivityStartedEvent", t, "1.0", "ActS1", iteration)
  link(msg, iterationsMap[iteration]["ActT1"], "activityExecution")
  return msg

def generateActF1(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelActivityFinishedEvent", t, "1.0", "ActF1", iteration)
  link(msg, iterationsMap[iteration]["ActT1"], "activityExecution")
  msg["data"]["outcome"] = {"conclusion": getOutcomeValuesFromVerdicts([iterationsMap[iteration]["TCF1"], iterationsMap[iteration]["TCF2"]], "SUCCESSFUL", "UNSUCCESSFUL")}

  return msg

def generateTCS1(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelTestCaseStartedEvent", t, "1.0", "TCS1", iteration)
  link(msg, iterationsMap[iteration]["ActT1"], "context")
  link(msg, iterationsMap[iteration]["ArtC1"], "iut")
  return msg

def generateTCF1(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelTestCaseFinishedEvent", t, "1.0", "TCF1", iteration)
  link(msg, iterationsMap[iteration]["TCS1"], "testCaseExecution")
  msg["data"]["outcome"] = {"verdict": randomizeVerdict(0.95)}
  return msg

def generateTCS2(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelTestCaseStartedEvent", t, "1.0", "TCS2", iteration)
  link(msg, iterationsMap[iteration]["ActT1"], "context")
  link(msg, iterationsMap[iteration]["ArtC1"], "iut")
  return msg

def generateTCF2(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelTestCaseFinishedEvent", t, "1.0", "TCF2", iteration)
  link(msg, iterationsMap[iteration]["TCS2"], "testCaseExecution")
  msg["data"]["outcome"] = {"verdict": randomizeVerdict(0.95)}
  return msg

def generateActT2(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelActivityTriggeredEvent", t, "1.0", "ActT2", iteration)
  linka(msg, iterationsMap[iteration]["ArtP1"], "causes")
  msg["data"]["name"] = "Act2"
  msg["data"]["category"] = "Test Activity"
  msg["data"]["triggers"] = [{"type": "EIFFEL_EVENT"}],
  msg["data"]["executionType"] = "AUTOMATED"
  return msg

def generateActS2(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelActivityStartedEvent", t, "1.0", "ActS2", iteration)
  link(msg, iterationsMap[iteration]["ActT2"], "activityExecution")
  return msg

def generateActF2(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelActivityFinishedEvent", t, "1.0", "ActF2", iteration)
  link(msg, iterationsMap[iteration]["ActT2"], "activityExecution")
  msg["data"]["outcome"] = {"conclusion": getOutcomeValuesFromVerdicts([iterationsMap[iteration]["TCF3"], iterationsMap[iteration]["TCF4"]], "SUCCESSFUL", "UNSUCCESSFUL")}
  return msg

def generateTCS3(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelTestCaseStartedEvent", t, "1.0", "TCS3", iteration)
  link(msg, iterationsMap[iteration]["ActT2"], "context")
  link(msg, iterationsMap[iteration]["ArtC1"], "iut")
  return msg

def generateTCF3(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelTestCaseFinishedEvent", t, "1.0", "TCF3", iteration)
  link(msg, iterationsMap[iteration]["TCS3"], "testCaseExecution")
  msg["data"]["outcome"] = {"verdict": randomizeVerdict(0.99)}
  return msg

def generateTCS4(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelTestCaseStartedEvent", t, "1.0", "TCS4", iteration)
  link(msg, iterationsMap[iteration]["ActT2"], "context")
  link(msg, iterationsMap[iteration]["ArtC1"], "iut")
  return msg

def generateTCF4(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelTestCaseFinishedEvent", t, "1.0", "TCF4", iteration)
  link(msg, iterationsMap[iteration]["TCS4"], "testCaseExecution")
  msg["data"]["outcome"] = {"verdict": randomizeVerdict(0.90)}
  return msg

def generateTCS5(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelTestCaseStartedEvent", t, "1.0", "TCS5", iteration)
  link(msg, iterationsMap[iteration]["TSS1"], "context")
  link(msg, iterationsMap[iteration]["ArtC2"], "iut")
  return msg

def generateTCF5(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelTestCaseFinishedEvent", t, "1.0", "TCF5", iteration)
  link(msg, iterationsMap[iteration]["TCS5"], "testCaseExecution")
  msg["data"]["outcome"] = {"verdict": randomizeVerdict(0.98)}
  return msg

def generateTCS6(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelTestCaseStartedEvent", t, "1.0", "TCS6", iteration)
  link(msg, iterationsMap[iteration]["TSS1"], "context")
  link(msg, iterationsMap[iteration]["ArtC2"], "iut")
  return msg

def generateTCF6(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelTestCaseFinishedEvent", t, "1.0", "TCF6", iteration)
  link(msg, iterationsMap[iteration]["TCS6"], "testCaseExecution")
  msg["data"]["outcome"] = {"verdict": randomizeVerdict(0.98)}
  return msg

def generateTCS7(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelTestCaseStartedEvent", t, "1.0", "TCS7", iteration)
  link(msg, iterationsMap[iteration]["TSS1"], "context")
  link(msg, iterationsMap[iteration]["ArtC2"], "iut")
  return msg

def generateTCF7(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelTestCaseFinishedEvent", t, "1.0", "TCF7", iteration)
  link(msg, iterationsMap[iteration]["TCS7"], "testCaseExecution")
  msg["data"]["outcome"] = {"verdict": randomizeVerdict(0.98)}
  return msg

def generateTSS1(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelTestSuiteStartedEvent", t, "1.0", "TSS1", iteration)
  link(msg, iterationsMap[iteration]["ActT3"], "context")
  msg["data"]["name"] = "My functional test suite"
  msg["data"]["category"] = "Pre system integration tests"
  msg["data"]["type"] = "FUNCTIONAL"
  return msg

def generateTSF1(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelTestSuiteFinishedEvent", t, "1.0", "TSF1", iteration)
  msg["data"]["outcome"] = {"verdict": getOutcomeValuesFromVerdicts([iterationsMap[iteration]["TCF5"], iterationsMap[iteration]["TCF6"], iterationsMap[iteration]["TCF7"]], "SUCCESS", "FAILURE")}
  link(msg, iterationsMap[iteration]["TSS1"], "testSuiteExecution")
  return msg

def generateCLM1(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelConfidenceLevelModifiedEvent", t, "1.0", "CLM1", iteration)
  linka(msg, iterationsMap[iteration]["ArtC1"], "subjects")
  linka(msg, iterationsMap[iteration]["TCF1"], "causes")
  linka(msg, iterationsMap[iteration]["TCF2"], "causes")
  linka(msg, iterationsMap[iteration]["TCF3"], "causes")
  linka(msg, iterationsMap[iteration]["TCF4"], "causes")
  msg["data"]["name"] = "readyForRelease"
  msg["data"]["value"] = getOutcomeValuesFromVerdicts([iterationsMap[iteration]["TCF1"], iterationsMap[iteration]["TCF2"], iterationsMap[iteration]["TCF3"], iterationsMap[iteration]["TCF4"]], "SUCCESS", "FAILURE")
  return msg

def generateCLM2(iterationsMap, iteration, t):
  msg = generateGenericMessage("EiffelConfidenceLevelModifiedEvent", t, "1.0", "CLM2", iteration)
  msg["data"]["name"] = "readyForSystemIntegration"
  msg["data"]["value"] = getOutcomeValuesFromVerdicts([iterationsMap[iteration]["TSF1"]], "SUCCESS", "FAILURE")
  linka(msg, iterationsMap[iteration]["TSF1"], "causes")
  linka(msg, iterationsMap[iteration]["ArtC2"], "subjects")
  return msg

def buildMsgArrayFromiterationsMap(iterationsMap):
  globalArray = []
  for key, itMap in iterationsMap.items():
    if itMap:
      globalArray.extend(buildMsgArrayFromIterationMap(itMap))

  return globalArray

def buildMsgArrayFromIterationMap(iterationMap):
  msgArray = []
  for msg in iterationMap.values():
    msgArray.append(msg)

  return msgArray

def generateIterationZeroMessages(iterationsMap, t):
  iterationsMap[0] = {}
  iterationsMap[0]["SCS1"] = generateSCS1(iterationsMap, 0, t)
  t += 1
  iterationsMap[0]["EDef1"] = generateEDef1(iterationsMap, 0, t)
  t += 1
  iterationsMap[0]["EDef2"] = generateEDef2(iterationsMap, 0, t)
  t += 1
  iterationsMap[0]["ArtC3"] = generateArtC3(iterationsMap, 0, t)
  t += 1
  iterationsMap[0]["CDef3"] = generateCDef3(iterationsMap, 0, t)
  t += 1
  iterationsMap[0]["ArtCC1"] = generateArtCC1(iterationsMap, 0, t)
  t += 1
  iterationsMap[0]["ArtCC2"] = generateArtCC2(iterationsMap, 0, t)
  t += 1
  iterationsMap[0]["ArtCC3"] = generateArtCC3(iterationsMap, 0, t)

  return t

def generateComponentBuildEvents(iterationsMap, iteration, t):
  t += 1
  iterationsMap[iteration]["SCC1"] = generateSCC1(iterationsMap, iteration, t)
  t += 1
  iterationsMap[iteration]["SCS1"] = generateSCS1(iterationsMap, iteration, t)
  t += 100
  iterationsMap[iteration]["CDef3"] = generateCDef3(iterationsMap, iteration, t)

  if random.random() < 0.5:
    t += 200000
    iterationsMap[iteration]["ArtCC1"] = generateArtCC1(iterationsMap, iteration, t)

  if random.random() < 0.5:
    t += 35000
    iterationsMap[iteration]["ArtCC2"] = generateArtCC2(iterationsMap, iteration, t)

  t += 1000
  iterationsMap[iteration]["ArtCC3"] = generateArtCC3(iterationsMap, iteration, t)

  return t

def generateSubSystemBuildEvents(iterationsMap, iteration, t):
  t += 100
  iterationsMap[iteration]["ActT4"] = generateActT4(iterationsMap, iteration, t)
  t += 1
  iterationsMap[iteration]["ActS4"] = generateActS4(iterationsMap, iteration, t)
  t += 100
  iterationsMap[iteration]["CDef2"] = generateCDef2(iterationsMap, iteration, t)

  if random.random() < 0.95:
    t += 100
    iterationsMap[iteration]["ArtC2"] = generateArtC2(iterationsMap, iteration, t)
    t += 30000
    iterationsMap[iteration]["ArtP2"] = generateArtP2(iterationsMap, iteration, t)

  t += 50
  iterationsMap[iteration]["ActF4"] = generateActF4(iterationsMap, iteration, t)

  return t

def generateSubSystemTestEvents(iterationsMap, iteration, t):
  t += 2000
  iterationsMap[iteration]["ActT3"] = generateActT3(iterationsMap, iteration, t)
  t += 3
  iterationsMap[iteration]["ActS3"] = generateActS3(iterationsMap, iteration, t)
  t += 2000
  iterationsMap[iteration]["TSS1"] = generateTSS1(iterationsMap, iteration, t)
  t += 100
  iterationsMap[iteration]["TCS5"] = generateTCS5(iterationsMap, iteration, t)
  t += 2
  iterationsMap[iteration]["TCS6"] = generateTCS6(iterationsMap, iteration, t)
  t += 1
  iterationsMap[iteration]["TCS7"] = generateTCS7(iterationsMap, iteration, t)
  t += 10000
  iterationsMap[iteration]["TCF5"] = generateTCF5(iterationsMap, iteration, t)
  t += 3000
  iterationsMap[iteration]["TCF6"] = generateTCF6(iterationsMap, iteration, t)
  t += 5000
  iterationsMap[iteration]["TCF7"] = generateTCF7(iterationsMap, iteration, t)
  t += 50
  iterationsMap[iteration]["TSF1"] = generateTSF1(iterationsMap, iteration, t)
  t += 3
  iterationsMap[iteration]["ActF3"] = generateActF3(iterationsMap, iteration, t)
  t += 300
  iterationsMap[iteration]["CLM2"] = generateCLM2(iterationsMap, iteration, t)

  return t

def generateSystemIntegrationEvents(iterationsMap, iteration, t):
  t += 300
  iterationsMap[iteration]["CDef1"] = generateCDef1(iterationsMap, iteration, t)
  t += 1000
  iterationsMap[iteration]["ArtC1"] = generateArtC1(iterationsMap, iteration, t)
  t += 1000
  iterationsMap[iteration]["ArtP1"] = generateArtP1(iterationsMap, iteration, t)
  t += 1000
  iterationsMap[iteration]["ActT1"] = generateActT1(iterationsMap, iteration, t)
  t += 2
  iterationsMap[iteration]["ActS1"] = generateActS1(iterationsMap, iteration, t)
  t += 50
  iterationsMap[iteration]["ActT2"] = generateActT2(iterationsMap, iteration, t)
  t += 1000
  iterationsMap[iteration]["TCS1"] = generateTCS1(iterationsMap, iteration, t)
  t += 100
  iterationsMap[iteration]["TCS2"] = generateTCS2(iterationsMap, iteration, t)
  t += 50000
  iterationsMap[iteration]["TCF2"] = generateTCF2(iterationsMap, iteration, t)
  t += 3000
  iterationsMap[iteration]["TCF1"] = generateTCF1(iterationsMap, iteration, t)
  t += 100
  iterationsMap[iteration]["ActF1"] = generateActF1(iterationsMap, iteration, t)
  t += 100000
  iterationsMap[iteration]["ActS2"] = generateActS2(iterationsMap, iteration, t)
  t += 200
  iterationsMap[iteration]["TCS3"] = generateTCS3(iterationsMap, iteration, t)
  t += 10000
  iterationsMap[iteration]["TCF3"] = generateTCF3(iterationsMap, iteration, t)
  t += 100
  iterationsMap[iteration]["TCS4"] = generateTCS4(iterationsMap, iteration, t)
  t += 120000
  iterationsMap[iteration]["TCF4"] = generateTCF4(iterationsMap, iteration, t)
  t += 20
  iterationsMap[iteration]["ActF2"] = generateActF2(iterationsMap, iteration, t)
  t += 2500
  iterationsMap[iteration]["CLM1"] = generateCLM1(iterationsMap, iteration, t)

  return t

def generateIterationMessages(iterationsMap, iteration, t):
  iterationsMap[iteration] = {}
  t = generateComponentBuildEvents(iterationsMap, iteration, t)
  t = generateSubSystemBuildEvents(iterationsMap, iteration, t)

  if "ArtC2" in iterationsMap[iteration]:
    t = generateSubSystemTestEvents(iterationsMap, iteration, t)
    if iterationsMap[iteration]["CLM2"]["data"]["value"] == "SUCCESS":
      t = generateSystemIntegrationEvents(iterationsMap, iteration, t)

  return t

def main(iterations):
  t = int(time.time() * 1000)

  iterationsMap = {}

  t = generateIterationZeroMessages(iterationsMap, t)

  for iteration in range(1, iterations + 1):
    t += 10000
    t = generateIterationMessages(iterationsMap, iteration, t)

  out = buildMsgArrayFromiterationsMap(iterationsMap)

  out.sort(key=lambda x: x["meta"]["time"], reverse=False)
  print(json.dumps(out, indent=2, separators=(",", ": ")))

def usage():
  print("-h, --help")
  print("    Print this text.")
  print("-i ..., --iterations=...")
  print("    Specify the number of iterations to create.")
  print("    Default: 1")

try:
  opts, args = getopt.getopt(sys.argv[1:], "hi:", ["help", "iterations="])
except getopt.GetoptError:
  usage()
  sys.exit(2)

iterations = 1

for opt, arg in opts:
  if opt in ("-h", "--help"):
    usage()
    sys.exit()
  elif opt in ("-i", "--iterations"):
    iterations = int(arg)

main(iterations)
