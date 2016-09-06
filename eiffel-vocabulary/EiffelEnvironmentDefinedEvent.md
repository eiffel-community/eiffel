# EiffelEnvironmentDefinedEvent
The EiffelEnvironmentDefinedEvent declares an environment which may be referenced from other events in order to secure traceability to the conditions under which an artifact was created or a test was executed. Depending on the technology domain, the nature of an environment varies greatly however: it may be a virtual image, a complete mechatronic system of millions of independent parts, or anything in between. Consequently, a concise yet complete and generic syntax for describing any environment is futile.

From Eiffel's point of view, however, the prioritized concern is not _description_ of the environment, but rather unambiguous _identification_ of it. Consequently, the EiffelEnvironmentDefinedEvent syntax offers several alternatives to be selected from depending on the use case at hand: an environment may be described using __data.image__, __data.host__ or __data.uri__. Exactly one of these properties SHOULD be included in any one event. In certain situations where an actual description of the environment is deemed redundant or its nature is implicit, the event MAY be used without any of these properties; it should be noted, however, that _explicit_ practices are always encouraged over _implicit_ ones.

## Data Members
### data.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the environment.

### data.version
__Type:__ String  
__Required:__ No  
__Description:__ The version of the environment, if any. This is in a sense redundant, as relationships between compositions can be tracked via the __PREVIOUS_VERSION__ link type, but can be used for improved clarity and semantics.

### data.image
__Type:__ String  
__Required:__ No  
__Description:__ A string identifying e.g. a [Docker](https://www.docker.com/) image. While not a perfect description of an environment, in many cases it is both sufficient and conducive.

### data.host
__Type:__ Object  
__Required:__ No  
__Description:__ An object identifying a host. This object is included for pragmatic reasons, as this method of environment identification is often used in practice. It is discouraged, however, as it is highly unreliable both in terms of consistency and traceability. Consistency because consecutive executions on the same host may produce different results, as there are no inherent guarantees that it will stay the same over time. Traceability because when analyzing the historical record you want a static description of the environment _as it was at the time of execution_, not a pointer to a dynamic entity which may or may not have changed since then (and may or may not have changed again the next time you inspect it).

#### data.host.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The hostname.

#### data.host.user
__Type:__ String  
__Required:__ Yes  
__Description:__ The user name on the host.

### data.uri
__Type:__ String  
__Required:__ No  
__Description:__ A URI identifying the environment description. This is the catch-all method of environment descriptions. Eiffel does not concern itself with the format or nature of the description, but merely points to its location.

## Examples
* [URI example](../examples/events/EiffelEnvironmentDefinedEvent/uri.json)
* [Host example](../examples/events/EiffelEnvironmentDefinedEvent/host.json)
* [Image example](../examples/events/EiffelEnvironmentDefinedEvent/image.json)