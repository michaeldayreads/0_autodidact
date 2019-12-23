# This file is an interpretation of the code examples and related experiments
# from pmotw3/argparse.

import argparse

parser = argparse.ArgumentParser(description="Example app for argparse experiments.", conflict_handler='resolve')

parser.add_argument('positional', action='store')
parser.add_argument('-f', action="store_true", dest="foo", default=False, help="Sets 'foo', defaults to False")
parser.add_argument('-v', '--verbose', action='count', default=0, help='Set verbosity level.')
parser.add_argument('--bar', '-b', action="store", help="Sets 'bar' to the corresponding value", required=True)
parser.add_argument('-qux', '-q', action="store", dest="qux", type=int, default=0, help="Sets qux to an int value")
parser.add_argument('-t', '--target', action="append", dest='targets', default=[], help="List of targets.")
parser.add_argument('--version', action='version', version='%(prog)s 0.1.0')

myargs = parser.parse_args()

if myargs.verbose > 0:
    print("[INFO] Verbose output requested.")
if myargs.verbose > 1:
    print("[INFO] Very verbose output requested.")
if myargs.verbose > 2:
    print("[WARN] This is down right loquacious, and is all the program can do.")

print(myargs.__dict__)

print("And this is the rest of the application / control loop...")

# Note that the pmotw blog is confusing if not incorrect; this version of the program raises no errors if invoked with no options.
# This may simply be different defaults for another `add_argument()` option of `required=[True|False]`.
# The article suggests that the arguments flagged 'store' are required, but I see no behavior to validate this claim.

# Also, if no value is given for an option that would be converted to an int, we are left with the value of None,
# unless we specify an `int` default value.