#!/bin/bash

set -e

USER_REPO="anon/foo"
USER=$(echo $USER_REPO | cut -d "/" -f 1)
REPO=$(echo $USER_REPO | cut -d "/" -f 2)

echo $USER_REPO
echo "$USER and $REPO"

EDITABLE_REQ="anon/foo.git@83d7a311767ea8ca47e144233c4697fce0a3a2bd"
SHA=$(echo $EDITABLE_REQ | cut -d "@" -f 2)

echo $EDITABLE_REQ
echo $SHA
