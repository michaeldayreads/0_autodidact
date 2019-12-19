# No explicit #! to test in different shells.

echo "Before running this script, be sure to set 'foo=bar'."
echo "Also, it is suggested to run a watch on ps for your shell to see the difference even more clearly."

# ensure there is time to see the additional process
sleep 2

echo $foo

