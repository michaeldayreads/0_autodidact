#!/usr/bin/python
"""
Replicate eventlet bug.

Create a virtualenv that includes eventlet to see the different behaviors.
"""

import subprocess

try:
    import eventlet
    print "-- eventlet package present"
    eventlet.monkey_patch()
except ImportError as err:
    if "eventlet" not in err.message:
        raise err
    print "-- no eventlet package"


def voodoo():
    """Show type of error raised based on eventlet presence."""
    try:
        cmd = ['false']
        subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        # raise subprocess.CalledProcessError(1, "test", output='baz')
    except subprocess.CalledProcessError as err:
        print 'Caught a "subprocess.CalledProccessError" whose class is:'
        print err.__class__
    except Exception as err:
        print 'Caught an "Exception" whose class is:'
        print err.__class__


voodoo()
