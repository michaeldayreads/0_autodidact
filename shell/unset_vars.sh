#!/usr/bin/env bash

set -euo pipefail

if [ ! -z "${CI-}" ]; then
  echo "The 'CI' var is NOT zero length, so we must be in the pipeline, so we will do the pipeline things..."
else
  echo "The 'CI' var IS zero, so we are not in the pipeline, and we will do the local things..."
fi

