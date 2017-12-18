#!/bin/bash

set -e

TRAVIS_COMMIT=$(git log --format=format:%H -1)
TRAVIS_BUILD_ID=$(date +%Y%m%d-%H%M)
TRAVIS_BUILD_NUMBER="user-gen"

echo $TRAVIS_COMMIT
echo $TRAVIS_BUILD_ID
echo $TRAVIS_BUILD_NUMBER

