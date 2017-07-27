#!/bin/bash

set -ex

TEST=$1

if [ "$TEST" == "yep" ]; then
    echo yep
else
    echo "all the things...
    except these things...
    and these"
fi

