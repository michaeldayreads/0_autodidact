#!/bin/bash
#
# Tool to find duplicates in files.i
#
# Note that trailing whitespace is problematic; lines that differ by only trailing whitespace will still be seen as unique.
# Use `grep -rIn '[[:blank:]]$' .` to find potentially problematic lines.
# -----------------------
# deliberate dup for demo
# deliberate dup for demo

set -e

if [ "$1" == "" -o "$2" == "" ]; then
    echo "[usage] ./dup_detector.sh <pattern> <dir>"
    exit 1
fi

for x in $(find $2 -name $1);
do
    result=$(sort --ignore-case  $x | uniq -id)
    if [ "$result" != "" ]; then
        echo -e "\nIn $x found:\n$result"
    fi
done
