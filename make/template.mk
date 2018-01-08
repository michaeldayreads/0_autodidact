# simple starter makefile for additional new tests
# make -f make/template.mk foo			>> ** ERROR md value not provided
# make -f make/template.mk foo md=test		>> ** ERROR invalid value
# make -f make/template.mk foo md=anon		>> foo


.PHONY: all foo baz

all:
	@printf "All the things"

VALID := alice anon bob
MSG := (Valid values are alice anon bob)

ifndef md
  $(error ERROR: md value not provided $(MSG))
else ifeq ($(md), $(filter $(md), $(VALID)))
  $(NOOP)
else
  $(error ERROR: invalid value '$(md)' $(VALID))
endif

foo:
	@echo foo

baz:
	@echo baz
