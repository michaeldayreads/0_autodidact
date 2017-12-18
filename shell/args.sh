#!/bin/bash

set -e

ORG="michaeldayreads"

REPO=$1
SHA=$2
BUILD_SH=$3

echo $BUILD_SH

exit 1

if [ "$REPO" == "" -o "$SHA" == "" ]; then
    echo "ERROR: Both repo and sha required"
    false
fi

mkdir $REPO
cd $REPO
git init
git remote add upstream https://github.com/$ORG/$REPO.git
git fetch upstream master
git reset --hard $SHA 

