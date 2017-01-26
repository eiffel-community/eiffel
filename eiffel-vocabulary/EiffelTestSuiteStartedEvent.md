# EiffelTestSuiteStartedEvent (TSS)
The EiffelTestSuiteStartedEvent declares that the execution of a test suite has started. This can either be declared stand-alone or as part of an activity or other test suite, using either a __CAUSE__ or a __CONTEXT__ link type, respectively. 

In Eiffel, a test suite is nothing more or less than a collection of test case executions (see [EiffelTestCaseStartedEvent](./EiffelTestCaseStartedEvent.md)) and/or other test suite executions. The executed test suite may be an ad-hoc transient grouping of test cases that were executed at a particular time or place or for a particular purpose or a persistent entity tracked in a test management system - Eiffel makes no distinction or assumptions either way.

## Data Members
### data.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the test suite. Uniqueness is not required or checked, but is useful.

### data.categories
__Type:__ String[]  
__Required:__ No  
__Description:__ The category or categories of the test suite. This can be used to group multiple similar test suites for analysis and visualization purposes. Example usage is to categorize test suites required before release as "Pre-release tests".

### data.types
__Type:__ String[]  
__Required:__ No  
__Legal values:__ ACCESSIBILITY, BACKUP_RECOVERY, COMPATIBILITY, CONVERSION, DISASTER_RECOVERY, FUNCTIONAL, INSTALLABILITY, INTEROPERABILITY, LOCALIZATION, MAINTAINABILITY, PERFORMANCE, PORTABILITY, PROCEDURE, RELIABILITY, SECURITY, STABILITY, USABILITY  
__Description:__ The type or types of testing performed by the test suite, as [defined by ISO 29119](http://www.softwaretestingstandard.org).

### data.liveLogs
__Type:__ Object[]  
__Required:__ No  
__Description:__ An array of live log files available during execution. These shall not be presumed to be stored persistently; in other words, once the test suite has finished there is no guarantee that these links are valid. Persistently stored logs shall be (re-)declared by [EiffelTestSuiteFinishedEvent](./EiffelTestSuiteFinishedEvent.md).

#### data.liveLogs.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the log file.

#### data.liveLogs.uri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI at which the log can be retrieved.

## Version History
| Version   | Introducing Commit |
| --------- | ------------------ |
| 1.0.0     | _Current version_  |

## Examples
* [Simple example](../examples/events/EiffelTestSuiteStartedEvent/simple.json)