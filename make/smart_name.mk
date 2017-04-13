func_testenv_name := f5mlb_func_$(orchestration)
scale_testenv_name := f5mlb_scale_$(orchestration)
ha_testenv_name := f5_mlb_ha_$(orchestration)
smoke_testenv_name := f5mlb_smoke_$(orchestration)

bigip_current_ver := v12.1.0
bigip_oldver_1_ver := v12.0.0
bigip_oldver_1_img := bigip-osready-12.0.0.4.0.674
bigip_oldver_2_ver := v11.6.1
bigip_oldver_2_img := bigip-osready-11.6.1.1.0.326

bigip_ver := $(bigip_current_ver)
ifeq ($(bigip_ver), $(bigip_current_ver))
	bigip_params :=
else ifeq ($(bigip_ver), $(bigip_oldver_1_ver))
	bigip_params := --params $(bigip_testenv_name)/bigip_img:$(bigip_oldver_1_img)
else ifeq ($(bigip_ver), $(bigip_oldver_2_ver))
	bigip_params := --params $(bigip_testenv_name)/bigip_img:$(bigip_oldver_2_img)
else
	$(error ERROR: bigip version $(bigip_ver) is not supported)
endif

# use 'bigip' unless there are params
default_bigip = bigip
named_bigip = bigip:$(1)_bigip

functest-install:
	@echo --requires $(if $bigip_ver, \
		$(call named_bigip,$(func_testenv_name)),bigip) $(bigip_params)

functest-run:
	@echo tbd

functest-teardown:
	@echo tbd
