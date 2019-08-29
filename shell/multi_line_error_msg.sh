#!/bin/bash

add_error() {
  # Preserve spaces in error messages
  if [ "$error_msg" == ""  ];then
    error_msg=$(echo "$1")
  else 
    error_msg=$(echo "$error_msg"; echo "$1")
  fi
}

print_error() {
  # Color wrapper to highlight error messages
  RED="\033[0;31m"
  NC="\33[0m"
  printf "${RED}${1}${NC}\n"
}

echo Doing thing 0 of 1
add_error "This is the first error."
echo Doing thing 1 of 1
add_error "And the second."

if [ "$error_msg" != "" ];then
  print_error "$error_msg"
  exit 1
else
  echo No errors!
fi
