# Exercises (coded in ipython)
#
# 1) Name three things that exceptions are good for.
#   a:  1) Gracefully handing errors that will occur, due to dependencies,
#           networks etc.
#       2) Improve precision of information to the technologist or user of the
#           code (as appropriate).
#       3) As an alternative to custom coding a context manager.
#       4) Termination actions (I prefer context managers).
#       5) Event notification (i.e. highly granular errors/debug).
# 2) What happens to an exception if you do not do anything special with it?
#   a: Program exits with a stack trace.
# 3) How can your script recover from an exception?
#   a: Use a try/except (with or without else, finally as appropriate) to retry,
#       log, or otherwise respond to the *expected* failure encountered.
# 4) Name two ways to trigger exceptions in your script.
#   a: Assert, and manually raise them.
# 5) Name two ways to specify actions run at termination.
#   a: Try/finally and context managers (with/as).
