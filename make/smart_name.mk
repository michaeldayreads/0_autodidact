# sanitized and reworked excerpt testing call funtions

func_module_name := my_func_$(orchestration)
scale_module_name := my_scale_$(orchestration)
ha_module_name := f5_mlb_ha_$(orchestration)
smoke_module_name := my_smoke_$(orchestration)

stack_current_ver := v12.1.0
stack_oldver_1_ver := v12.0.0
stack_oldver_1_img := stack-osready-12.0.0.4.0.674
stack_oldver_2_ver := v11.6.1
stack_oldver_2_img := stack-osready-11.6.1.1.0.326

# stack_ver := $(stack_current_ver)
ifeq ($(stack_ver), )
  stack_params :=
else ifeq ($(stack_ver), $(stack_oldver_1_ver))
  stack_params := --params $(stack_module_name)/stack_img:$(module_oldver_1_img)
else ifeq ($(stack_ver), $(stack_oldver_2_ver))
  stack_params := --params $(stack_module_name)/stack_img:$(module_oldver_2_img)
else
  $(error ERROR: stack version $(stack_ver) is not supported)
endif

# use 'stack' unless there are params
named_stack = stack:$(1)_$(stack_ver)

functest-install:
	@echo --requires $(if $(stack_ver), \
		$(call named_stack,$(func_module_name)),stack) $(stack_params)

functest-run:
	@echo tbd

functest-teardown:
	$(if $(stack_ver),@echo module -v delete --name \
		$(call named_stack,$(func_module_name)),\
		@echo INFO: No stack_ver specified - skipping teardown)
