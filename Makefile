# Copyright 2022-2023 Axis Communications AB.
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

.PHONY: all
all: generate_docs generate_manifest generate_schemas

# The generate_* goals assume that all Python package dependencies are
# available, e.g. via a virtualenv.

.PHONY: generate_docs
generate_docs:
	./generate_docs.py definitions/Eiffel*Event/*.yml

.PHONY: generate_manifest
generate_manifest:
	./generate_manifest.py > event_manifest.yml

.PHONY: generate_schemas
generate_schemas:
	./generate_schemas.py definitions/Eiffel*Event/*.yml
