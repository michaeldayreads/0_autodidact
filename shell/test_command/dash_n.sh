#!/usr/bin/env bash

if [ -n "$dash_n" ]; then
  echo "dash_n ($dash_n) is NOT empty, so a test for -n is True, and the if block executes."
else
  echo "dash_n ($dash_n) IS empty, so a test for -n is False, and the else block executes."
fi

printf "\n\nImportantly, the \`-n\` is OPTIONAL, so the same logic can be written without the explicit flag.\n\n"

if [ "$dash_n" ]; then
  echo "dash_n ($dash_n) is NOT empty, so bare test for it is True, and the if block executes."
else
  echo "dash_n ($dash_n) IS empty, so a base test for it is False, and the else block executes."
fi
