#!/bin/bash

set -e

if [ "$(python -V 2>&1)" == "Python 2.7.10" ]; then
    echo "yep!"
else
    echo "nope"
fi

