#!/bin/bash

usage() {
  echo "Usage: $(basename "$0") OPTION
  where OPTION is
    -d|--schemas-dir SCHEMAS_DIR
      Prints out the latest JSON schemas of SCHEMAS_DIR. It expects a folder
      containing sub-folders per event, i.e. <SCHEMAS_DIR>/<event-dir>/X.Y.Z.json.
      The output is list of files separated by new-lines.

    -h|--help        Prints out this help.
"

}
schemasdir=''

while [[ $# -gt 0 ]]; do
  case $1 in
    -d|--schemas-dir)
      schemasdir="$2"
      shift 2
      ;;
    *)
      usage
      exit 1
      ;;
  esac
done

if [ -z "$schemasdir" ]; then
  usage
  exit 1
fi

while IFS= read -r -d '' schemadir
do
  schema=$(ls "$schemadir/$d" | sort -V | tail -1)
  echo "$schemadir/$d$schema"
done <   <(find "$schemasdir" -mindepth 1 -type d -print0 )