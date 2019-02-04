#!/bin/bash

echo "Test the success case."

ls && flag=true || flag=false

if [ $flag ]; then
    echo "Success, as expected."
fi

echo "Test the failure case."

foo && flag=true || flag=false

if [ $flag ]; then
    echo "And here we would have a warning..."
fi

