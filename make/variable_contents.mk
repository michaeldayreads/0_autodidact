.PHONY: all baz

all:
	@printf "All the things"

VALID := foo bar qux
MSG := (Valid values are foo, bar, qux)

ifeq ("$(MAKECMDGOALS)", "")
  $(NOOP)
else
  ifndef md
    $(error ERROR: md value not provided $(MSG))
  else ifeq ($(md), $(filter $(md), $(VALID)))
    $(NOOP)
  else
    $(error ERROR: invalid value '$(md)' $(VALID))
  endif
endif

baz:
	@echo baz
