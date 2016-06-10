# The Meta Object
The __meta__ object contains meta-information describing the event: when it was created, where it came from, its type et cetera. The __meta__ object contains the same members regardless of __meta.type__<sup>[1](#footnote1)</sup>, with the caveat that certain members are optional and the tendency to use them may vary with event type.

## Meta Members
### meta.id
__Type:__ String  
__Format:__ [UUID](http://tools.ietf.org/html/rfc4122)  
__Required:__ Yes  
__Description:__ The unique identity of the event, generated at event creation.

### meta.type
__Type:__ String  
__Format:__ An event type name  
__Required:__ Yes  
__Description:__ The type of event. This field is required by the recipient of the event, as each event type has a specific meaning and a specific set of members in the __data__ and __links__ objects.

### meta.version
__Type:__ String  
__Format:__ Semantic version excluding PATCH.  
__Required:__ Yes  
__Description:__ The version of the event type. This field is required by the recipient of the event to interpret the contents.

### meta.time
__Type:__ Integer  
__Format:__ Milliseconds since epoch.  
__Required:__ Yes  
__Description:__ The event creation timestamp.

### meta.tags
__Type:__ String[]  
__Format:__ Free text  
__Required:__ No  
__Description:__ Any tags or keywords associated with the events, for searchability purposes.

### meta.source
__Type:__ Object  
__Format:__  
__Required:__ Yes
__Description:__ A description of the event sender. Primarily for traceability purposes.

#### meta.source.domainId
__Type:__ String  
__Format:__ Free text  
__Required:__ Yes  
__Description:__ Identifies the domain that produced an event. A domain is an infrastructure topological concept, which may or may not corresponds to an organization or product structures. A good example would be Java packages notation, ex. com.mycompany.product.component or mycompany.site.division. Also, keep in mind, that division names, as well as product/component names, tends to change. That is why it might be a good idea to pick coded names that do not directly reflect current naming in the organization. Think of flower names as names for sites or simply site1, site2, site3 instead of Sweden, Denmark, Norway.

#### meta.source.host
__Type:__ String  
__Format:__ Hostname  
__Required:__ No  
__Description:__ The hostname of the event sender.

#### meta.source.name
__Type:__ String  
__Format:__ Free text  
__Required:__ No  
__Description:__ The name of the event sender.

#### meta.source.serializer
__Type:__ Object  
__Format:__   
__Required:__ No  
__Description:__ The [GAV](https://maven.apache.org/guides/mini/guide-naming-conventions.html) coordinates of the serializer software used to construct the event.

##### meta.source.serializer.groupId
__Type:__ String  
__Format:__ groupId  
__Required:__ Yes  
__Description:__ The groupId of the serializer software.

##### meta.source.serializer.artifactId
__Type:__ String  
__Format:__ artifactId  
__Required:__ Yes  
__Description:__ The artifactId of the serializer software.

##### meta.source.serializer.version
__Type:__ String  
__Format:__ version  
__Required:__ Yes  
__Description:__ The version of the serializer software.

#### meta.source.uri
__Type:__ String  
__Format:__ URI  
__Required:__ No  
__Description:__ The URI of, related to or describing the event sender.


&nbsp;
&nbsp;

------------------
&nbsp;

<a name="footnote1">1</a>: Event types are versioned independently from one another. There are three important consequences of this. First, any change to __meta__ requires all events to be updated. Second, any schema of a specific version of an event must also include the __meta__ object – specifically as it is defined for that version of the event. Third, consumers should be prepared to receive events of varying __meta__ contents. The exception to this are the __meta.type__ and __meta.version__ fields, which are always assumed to be present change. 
