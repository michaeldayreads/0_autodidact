#!/bin/bash

exit_on_non_zero() {
  rc=$?
  if [ "$rc" != "0" ]; then
    echo "We shall exit... comment out next line for sanity check"
    exit $rc
  fi
}

ls
exit_on_non_zero
ls itShallNotBeFound
exit_on_non_zero
echo "We should not see this."

