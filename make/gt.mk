.PHONY: test test2

bigip_ver ?= v12.1

ifeq ($(bigip_ver), v13.0)
	echo 13.0
else ifeq($(bigip_ver), v12.1)
	echo 12.1
else if 
