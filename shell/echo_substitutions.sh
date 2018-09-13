#!/bin/bash

set -e

clear

echo "Problem: How do we substitute vars into json?"
echo "Solution: Use quotes and doublequotes cleverly."
set -x

myvar=bar
echo '{"foo": "'$myvar'"}'

set +x
echo 'Note that the `$myvar` in the preceding line is substituted even for the `set -x` output.'

#ticks - single quotes around ticks let them print
#set - toggle invocation for logging / debugging
