#!/bin/bash

set -e
FOO="foo"
echo "before: $FOO"
FOO="$(./return-test-result.sh)"
echo "after: $FOO"

