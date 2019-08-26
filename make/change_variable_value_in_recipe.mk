.PHONY : demo

example = foo

demo:
	@echo Modifying a variable in a recipie requires an eval...
	@echo $(example)
	$(eval example=bar)  # override may be needed if passed from invocation
	@echo $(example)
