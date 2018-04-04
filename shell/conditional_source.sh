#!/bin/bash
# test and document how to conditionally source context specfic bash or vim files

set -ex

if [[ $1 == '' ]]; then
    echo "[ERROR] script expects a path to check..."
fi

if [[ -f $1 ]]; then
    echo "Found it, and would source it."
else
    echo "Did not find it, and would not source it."
fi
