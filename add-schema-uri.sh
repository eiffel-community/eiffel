#!/bin/bash

# A helper script to add property schemaUri to the latest schemas and increase
# its version.
schemas_dir="schemas"
semver_regex='(.*)/([[:digit:]]+)\.([[:digit:]]+)\.([[:digit:]]+)\.(json)'

property_path='.properties.meta.properties'
property_to_add='{schemaUri: {type: "string", additionalProperties: false}}'

for current_file in $(./find-latest-schemas.sh -d "$schemas_dir"); do
  # schema=$(basename "$path")
  if [[ ! "$current_file" =~ $semver_regex ]]; then
    echo "$path doesn't match $semver_regex" 1>&2
    exit 1
  fi

  path="${BASH_REMATCH[1]}"
  major="${BASH_REMATCH[2]}"
  minor="${BASH_REMATCH[3]}"
  patch="${BASH_REMATCH[4]}"
  suffix="${BASH_REMATCH[5]}"

  ((minor += 1))
  new_version="$major.$minor.$patch"
  new_file="$path/$new_version.$suffix"

  cat "$current_file" | jq "$property_path += $property_to_add" | \
    jq ".properties.meta.properties.version.enum[0] |= \"$new_version\"" | \
    jq ".properties.meta.properties.version.default |= \"$new_version\"" \
    > "$new_file"
  ls -l "$new_file"
done