!#/bin/bash

set -e

# use case: remove a character from an existing variable
# note result could also be assigned to a new variable or simply output as needed

foo=foo-bar-baz
echo $foo
foo=$(echo $foo | sed 's/-//g')
echo $foo
