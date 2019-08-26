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
# Additionally, examples of variable override and recursive invocation are demonstrated.


.PHONY : doc lint _lint_both _run_in_docker var_override

THIS_FILE := $(lastword $(MAKEFILE_LIST))
# this pattern from 
# https://stackoverflow.com/questions/5377297/how-to-manually-call-another-target-from-a-make-target

doc:
	@head -15 make_in_docker.mk

var_override:
	@echo check
	@echo $(CMD)
	$(eval override CMD=bar)
	@echo $(CMD)

lint:
	$(eval CMD=_lint_both)  # _$@_both also could be used
	$(MAKE) -f $(THIS_FILE) _run_in_docker CMD=$(CMD)

_lint_both:
	# In CI/CD, invoke directly; `make _lint_both`
	@echo do lint thing one
	@echo do lint thing two
	@echo do all the lint things!

_run_in_docker:
	docker run \
	-it \
	-v `pwd`:`pwd` \
	-w `pwd` \
	python:3.7-alpine \
	sh scripts/bootstrap_container.sh $(THIS_FILE) $(CMD)
