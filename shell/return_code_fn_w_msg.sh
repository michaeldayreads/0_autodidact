#!/bin/bash

exit_on_non_zero() {
  rc=$?
  if [ "$rc" != "0" ]; then
    echo $1
    exit $rc
  fi
}

ls
exit_on_non_zero
ls itShallNotBeFound
exit_on_non_zero "Error: custom error message."
echo "We should not see this."

