#!/bin/bash

if [ "$1" == "-b"  ]; then
	echo we got the option
fi

for i in `seq 1 10`;
do
  echo test $i
done
