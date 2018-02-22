#!/bin/bash
set -ex

my_array=(foo bar baz qux)

for item in "${my_array[@]}"; do
    echo $item
done
