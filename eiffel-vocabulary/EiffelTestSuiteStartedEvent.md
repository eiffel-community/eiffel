# EiffelTestSuiteStartedEvent
The EiffelTestSuiteStartedEvent declares that a suite of tests has started. This can either be declared stand-alone or as part of an activity or other test suite, using either a __CAUSE__ or a __CONTEXT__ link type, respectively. 

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
__Description:__ An array of live log files available during execution. These shall not be presumed to be stored persistently; in other words, once the activity has finished there is no guarantee that these links are valid. Persistently stored logs shall be (re-)declared by [EiffelActivityFinishedEvent](./EiffelActivityFinishedEvent.md).

#### data.liveLogs.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the log file.

#### data.liveLogs.uri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI at which the log can be retrieved.

## Examples
* [Simple example](../examples/events/EiffelTestSuiteStartedEvent/simple.json)