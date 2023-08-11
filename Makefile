# Copyright 2022-2023 Axis Communications AB and Others.
# For a full list of individual contributors, please see the commit history.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The goals assume that all Python package dependencies are
# available, e.g. via a virtualenv.

.PHONY: all
all: generate_docs generate_manifest generate_schemas ## Generate all documentation and schemas from YAML

# Following help file tip from https://stackoverflow.com/questions/8889035/how-to-document-a-makefile
.PHONY: help
help:     ## Show this help.
	 @egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-30s\033[0m %s\n", $$1, $$2}'

.PHONY: tests
test: ## Run all document related checks found in tox: pytest, jsonformat, validate
	tox run -e pytest,jsonformat,validate

.PHONY: generate_docs
generate_docs: ## Generate the Markdown files based on the YAML definitions
	./generate_docs.py definitions/Eiffel*Event/*.yml

.PHONY: generate_manifest
generate_manifest: ## Generate the manifest file
	./generate_manifest.py > event_manifest.yml

.PHONY: generate_schemas
generate_schemas: ## Generate the schemas based on the YAML definitions
	./generate_schemas.py definitions/Eiffel*Event/*.yml
