#!/bin/bash

# ensure make is available 
apk add --update --no-cache make

# invoke make with arg target
make -f $1 $2
