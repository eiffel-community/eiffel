# EiffelTestExecutionRecipeCollectionCreatedEvent
The EiffelTestExecutionRecipeCollectionCreatedEvent declares that a collection of test execution recipes has been created. In order to clarify what that means, several concepts need to be explained.

Just as Eiffel is an opinionated protocol, EiffelTestExecutionRecipeCollectionCreatedEvent is an opinionated event, and to a certain extent that opinion goes against the grain of traditional test management. This event assumes that activity configurations and test scope definitions are two separate things. To exemplify, when one's CI server triggers the Acceptance Test activity in the pipeline, there is nothing in that activity that says which tests to execute where or with what parameters: that is a separate concern. Instead, it will query a test selection service for that information. This information is encapsulated by the EiffelTestExecutionRecipeCollectionCreatedEvent, which contains all the information needed to configure and execute the tests.

How the test selection service generates the recipe collection is, from the point of view of the Eiffel protocol, irrelevant. It may very well be from a statically defined list of test cases, or from an elaborate test selection algorithm weighing together a host of factors to determine the optimal set of test cases to execute at any particular time, or a combination of the two.

The __data__ object consists of two main parts. __data.selectionStrategy__ identifies the strategy used to select the test cases and generate the recipe collection, while __data.batches__ is an array of batches of recipes. Batches are used to control the order of execution of test cases. Every batch has a priority to let the test executor order them in sequence, but within each batch no assumptions are made as to the execution order the test cases. This way the recipe collection can either allow the executor a high degree of freedom in scheduling the test executions, and/or prescribe the exact sequential order in which they must be executed.

Finally, each recipe (__data.batches.recipes__) consists of two parts: the test case to execute, and the constraints of that execution. The EiffelTestExecutionRecipeCollectionCreatedEvent does not explicitly include those contraints as part of the event syntax, for two reasons. First, such constraints can be very comprehensive, resulting in very large events, particularly for collections of thousands of recipes. Second, the nature of the constraints are highly dependent on technology domain and test execution framework. There are three questions that typically need to be answered, however: what is the item under test, in what kind of environment is it to be tested, and what are the test parameters? Note the distinction between test case and test execution: it is perfectly legal for a single test case to appear multiple times within the same EiffelTestExecutionRecipeCollectionCreatedEvent, but (presumably) with different constraints.

## Data Members
### data.selectionStrategy
__Type:__ Object  
__Required:__ Yes  
__Description:__ The strategy used to select the test cases and generate the recipe collection.

#### data.selectionStrategy.tracker
__Type:__ String  
__Required:__ No  
__Description:__ The name of the selection strategy that generated the test execution recipe collection.

#### data.selectionStrategy.id
__Type:__ String  
__Required:__ Yes  
__Description:__ The unique identity of the selection strategy that generated the test execution recipe collection.

#### data.selectionStrategy.uri
__Type:__ String  
__Required:__ No  
__Description:__ The URI at which the the selection strategy that generated the test execution recipe collection can be retrieved.

### data.batches
__Type:__ Object[]  
__Required:__ Yes  
__Description:__ A list of batches of recipes.

#### data.batches.name
__Type:__ String  
__Required:__ No  
__Description:__ The name of the recipe batch.

#### data.batches.priority
__Type:__ Integer  
__Required:__ Yes  
__Description:__ The execution priority of the batch, as compared to other batches in the collection. A lower value SHALL be interpreted as a higher priority.

#### data.batches.recipes
__Type:__ Object[]  
__Required:__ Yes  
__Description:__ The collection of test execution recipes within the batch.

##### data.batches.recipes.testCase
__Type:__ Object  
__Required:__ Yes  
__Description:__ The test case to be executed in this execution recipe.

###### data.batches.recipes.testCase.tracker
__Type:__ String  
__Required:__ No  
__Description:__ The name of the test case tracker - typically a test management system.

###### data.batches.recipes.testCase.id
__Type:__ String  
__Required:__ Yes  
__Description:__ The unique identity of the test case.

###### data.batches.recipes.testCase.uri
__Type:__ String  
__Required:__ No  
__Description:__ A location where a description of the test case can be retrieved.

##### data.batches.recipes.constraints
__Type:__ String  
__Required:__ Yes  
__Description:__ A URI identifying the constraints of the test execution recipe. Eiffel does not prescribe the format of the constraints document, but recognizes that the nature and syntax of such a document varies with technology domains and test execution frameworks. That being said, there are three questions that typically need to be answered in such a document: what is the item under test, in what kind of environment is it to be tested, and what are the test parameters?

## Version History
| Version   | Introducing Commit |
| --------- | ------------------ |
| 1.0.0     | _Current version_  |

## Examples
* [Simple example](../examples/events/EiffelTestExecutionRecipeCollectionCreatedEvent/simple.json)