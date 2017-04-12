<!---
   Copyright 2017 Ericsson AB.
   For a full list of individual contributors, please see the commit history.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
--->

# EiffelIssueVerifiedEvent (IV)
The EiffelIssueVerifiedEvent declares that an issue, typically a requirement, has been verified by some means. It is different from [EiffelTestCaseFinishedEvent](./EiffelTestCaseFinishedEvent.md) in that multiple test case executions may serve as the basis for a single verification or, conversely, multiple issues may be verified based on a single test case execution.

## Data Members
### data.issues
__Type:__ Object[]  
__Required:__ Yes  
__Description:__ A list of verified (successfully or not) issues.

#### data.issues.type
__Type:__ String  
__Required:__ Yes  
__Legal values:__ BUG, IMPROVEMENT, FEATURE, WORK_ITEM, REQUIREMENT, OTHER  
__Description:__ The type of issue.
  
#### data.issues.tracker
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the issue tracker. This can unfortunately not be standardized, and is therefore context sensitive: though some trackers and ALM tools are more popular than others, an exhaustive enumeration is impossible, particularly when considering company specific internal solutions. Consequently one should not rely on the name as the primary method of retrieval, but rather __data.issues.uri__. __data.issues.tracker__ together with __data.issues.id__ is still useful for analysis and traceability, however, as long as it can be correctly interpreted.

#### data.issues.id
__Type:__ String  
__Required:__ Yes  
__Description:__ The identity of the issue. This is tracker dependent - most trackers have their own issue naming schemes.

#### data.issues.uri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI of the issue.

#### data.issues.value
__Type:__ String  
__Required:__ Yes  
__Legal values:__ SUCCESS, FAILURE, INCONCLUSIVE  
__Description:__ The value of the verification.  
SUCCESS signifies that the issue was successfully verified.  
FAILURE signifies that verification of the issue failed.
INCONCLUSIVE signifies that the verification of the issue was inconclusive.

## Version History
| Version   | Introduced in                                          | Changes                                 |
| --------- | ------------------------------------------------------ | --------------------------------------- |
| 1.0.0     | [edition-bordeaux](../../../tree/edition-bordeaux)     | Initial version.                        |

## Examples
* [Simple example](../examples/events/EiffelIssueVerifiedEvent/simple.json)