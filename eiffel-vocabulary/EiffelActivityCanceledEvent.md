# EiffelActivityCanceledEvent
The EiffelActivityCanceledEvent signals that a previously triggered activity execution has been canceled _before it has started_. This is typically used in queuing situations where a queued execution is dequeued. It is recommended that __CAUSE__ links be used to indicate the reason.

## Data Members
### data.reason
__Type:__ String  
__Required:__ No  
__Description:__ Any human readable information as to the reason for dequeueing.

## Version History
| Version   | Introducing Commit |
| --------- | ------------------ |
| 1.0.0     | _Current version_  |

## Examples
* [Simple example](../examples/events/EiffelActivityCanceledEvent/simple.json)