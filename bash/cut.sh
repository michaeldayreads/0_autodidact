#!/bin/bash

set -e

USER_REPO="anon/foo"
USER=$(echo $USER_REPO | cut -d "/" -f 1)
REPO=$(echo $USER_REPO | cut -d "/" -f 2)

echo "$USER and $REPO"
