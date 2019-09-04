#!/bin/bash

cts() {
  echo $(date '+%a %b %d %T %Z %Y')
}

export -f cts

example() {
  STAMP=$(cts)
  echo "${STAMP} -- And the example message."
}

cts
echo "Let's make sure we can use it as expected..."
example

