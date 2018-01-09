#!/bin/bash

set -ex

if [ "$1" == "" ]; then
    echo "ERROR: no value provided!"
elif [ "$1" == "foo" -o "$1" = "bar" ]; then
    my_var=foo
else
    my_var=$1
fi

echo $my_var
