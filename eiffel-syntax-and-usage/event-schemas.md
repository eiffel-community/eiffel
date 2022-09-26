<!---
   Copyright 2022 Axis Communications AB.
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

# Event Schemas

Eiffel events are defined using [JSON schemas](https://json-schema.org/) and stored in this repository along with their documentation. Each schema version gets its own file so you can access all schemas from a single source code tree. Schema files have predictable paths based on the event name and its version, e.g. [schemas/EiffelCompositionDefinedEvent/3.2.0.json](../schemas/EiffelCompositionDefinedEvent/3.2.0.json).

The documentation of each event is available in a Markdown file that covers the latest version of the event, e.g. [eiffel-vocabulary/EiffelCompositionDefinedEvent.md](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md).

Both schemas and documentation files are generated from _schema definition files_; YAML files with a custom schema based on the JSON schema specification. Like the schema files themselves there's one file per event and version, e.g. [definitions/EiffelCompositionDefinedEvent/3.2.0.yml](../definitions/EiffelCompositionDefinedEvent/3.2.0.yml). The main difference between these files and normal JSON schema files, apart from the YAML representation, is an additional set of keys with an underscore prefix that contains additional metadata that can't be part of the JSON schema itself. Those keys are used when generating the documentation and are simply ignored when the schema definition files are turned into schema files. The following table describes these additional top-level keys.

| Key             | Description             |
| --------------- | ----------------------- |
| `_abbrev`       | The abbreviation of the event name, e.g. "CD" for EiffelCompositionDefinedEvent. |
| `_description`  | An overall description of the event. |
| `_links`        | An object describing the valid link types for the event. |
| `_links.<link type>.description`  | A description of the link type. |
| `_links.<link type>.required`     | A boolean value indicating whether a link of this type is required. Optional, default false. |
| `_links.<link type>.multiple`     | A boolean value indicating whether multiple links of this type is allowed. Optional, default false. |
| `_links.<link type>.targets.any_type`  | A boolean value indicating whether the link can point to an event of any type. |
| `_links.<link type>.targets.types`     | A string array of event names that the link type may point to. Must be non-empty if `any_type` is false, and must be empty if `any_type` is true. |
| `_history`      | An array of objects describing the event type's version history, up to and including the current version. The items should be sorted in reverse order. |
| `_history.version`        | The event version described in this item. |
| `_history.introduced_in`  | A description of the edition in which this item's event version was introduced. |
| `_history.changes`        | A short description of the changes in this item's event version. | 
| `_examples`     | An array of objects describing examples of this event. |
| `_examples.title`         | The name of the example. |
| `_examples.url`           | The URL of the example. |

In addition, the object that describes each property in the schema supports a few additional keys that are specific to the schema definition format and will be omitted when the schema file is produced:

| Key             | Description             |
| --------------- | ----------------------- |
| `_description`  | A description of the property. |
| `_format`       | A description of the expected form of the values, in addition to what's prescribed by the data type. For example, a string property could be expected to contain a URI or a UUID. Optional. |

## Sharing subschemas between events
Another feature of schema definition files is that they may contain references to other schema definition files via standard [JSON references](https://json-spec.readthedocs.io/reference.html). This is used to reuse common definitions like the meta member in all events. Doing so reduces the maintenance burden when making changes to the common parts of the schemas, makes sure there are no unintentional differences between events, and makes it possible for programs reading the files to understand that a subset of the schema actually is common to more than one event. The latter can e.g. be used by programs to generate types for an SDK from the schema definition files.

For example, the definition of __meta__ is found among one of the EiffelMetaProperty subschemas like [definitions/EiffelMetaProperty/3.0.0.yml](../definitions/EiffelMetaProperty/3.0.0.yml). Defining this member and referencing it from the event's schema is done like this:

```
meta:
  $ref: ../EiffelMetaProperty/3.0.0.yml
```

Changing a non-event schema definition that's referenced by actual events, like EiffelMetaProperty, fundamentally works in the same way as changing the event schemas directly. The new event version should be updated according to the [normal patch/minor/major rules](versioning.md), which in practice means that the version number increase should match the change of the referenced schema; if EiffelMetaProperty gets a minor update then all events that update to that version should receive a minor version bump too.

## Example
Here's a minimal example of a schema definition file:

```
$schema: http://json-schema.org/draft-04/schema#
_abbrev: SH
_description: The EiffelSomethingHappenedEvent declares that something happened.
type: object
properties:
  meta:
    $ref: ../EiffelMetaProperty/3.0.0.yml
  data:
    type: object
    properties:
      what:
        _description: A description of what happened.
        _format: A well-formed sentence.
        type: string
      customData:
        type: array
        items:
          type: object
          properties:
            key:
              type: string
            value: {}
          required:
            - key
            - value
          additionalProperties: false
    required:
      - what
    additionalProperties: false
  links:
    type: array
    items:
      $ref: ../EiffelEventLink/1.1.1.yml
required:
  - meta
  - data
  - links
additionalProperties: false
_links:
  CAUSE:
    description: Identifies a cause of the event occurring.
    required: false
    multiple: true
    targets:
      any_type: true
      types: []
_history:
  - version: 1.0.0
    introduced_in: '[edition-lyon](../../../tree/edition-lyon)'
    changes: Initial version.
_examples:
  - title: Simple example
    url: ../examples/events/EiffelSomethingHappenedEvent/simple.json
```

## Generating schemas and documentation
Schema and documentation files should never by updated by hand. Instead, modify the schema definition files and use the [generate_docs.py](../generate_docs.py) and [generate_schemas.py](../generate_schemas.py) Python scripts to regenerate all schemas and documentation. The included [makefile](../Makefile) calls the scripts with the required arguments. Just make sure you have installed the Python dependencies specified in [requirements.txt](../requirements.txt) before running the scripts. Package installations are typically done within a Python virtualenv, but you can also reuse one of the virtualenvs created by tox. The schema definition files and the generated files must always be consistent, i.e. all changes to these files should be committed together. This is enforced via a GitHub Actions workflow when pushing to a branch or creating a PR.
