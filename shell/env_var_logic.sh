#!/bin/bash

die() {
  printf "%s\n" "$*"
  exit 1
}

MYPATH="docs"

if [ $BUILD_HTML_DIR ]; then
    $MYPATH=$BUILD_HTML_DIR
fi

[ -d "bash" ] || die "bash path does not exist"
[ -d $MYPATH ] || die "$MYPATH path does not exist"

echo $MYPATH
