#!/usr/bin/env bash

set -e

zeroCheck() {
  if [ "$1" == 0  ]; then
    return 0
  else
    return 1
  fi
}

echo "check 0"
zeroCheck 1
# it errors out on the last line, returns a 1
echo "check 1"
zeroCheck 0
