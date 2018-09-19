#!/bin/bash

set -e

prefix=$1

if [ "$prefix" == "" ]; then
    echo Prefix arg required
    exit 1
fi

ID="$(date '+%Y%m%d%H%M%Sid')"
sID="$(date '+%Y%m%d%H%M%Sid')-suffix"
pID="$prefix-$(date '+%Y%m%d%H%M%Sid')-suffix"
echo "basic: $ID"
echo "suffixed $sID"
echo "prefixed: $pID"

