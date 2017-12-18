#!/bin/bash
# multi arg readable tests

set -e

REPO=$1
SHA=$2
BUILD_CMD=$3
DOCKER_NAMESPACE=$4

if [ \
    "$REPO" == "" -o \
    "$SHA" == "" -o \
    "$BUILD_CMD" == "" -o \
    "$DOCKER_NAMESPACE" == "" \
    ]; then
    echo "[ERROR:] repo, sha, build command & docker namespace required"
    false
fi
