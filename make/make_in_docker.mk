# This file is an experiment / poc to seek a simple pattern for targets to run in docker locally while
# set up to expect that container as the environment in CI/CD.
#
# A common pattern is needing to have make targets do the same - or as near as possible to the same -
# thing in CI/CD as locally. Often, CI/CD is container centric, meaning each job is run using a specified
# container. Thus, if we use the same container locally to perform operations like linting and building
# then variance between local and pipeline builds should be reduced.
#
# At the same time, as DevOps, Makefiles offer us a way to define an interface to a project. That is, we
# can leverage existing conventions for makefile targets and add those appropriate to our own community's
# needs so that workflows are consistent across repos. Additionally, if we consistently use the same
# targets, we can consolidate our files and use `include` more easily.
#

.PHONY : motivation

motivation:
	@head -13 make_in_docker.mk
