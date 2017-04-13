.PHONY:	tidy hello all

all:
	@printf "available targets:\n"
	@printf "  hello: prints hello world\n"
	@printf "  diskfree: outputs free space on disk.\n"
	@printf "  tidy: remove files matching `*.tmp`"

hello:
	@echo hello world

diskfree:; df -h /

tidy:
	-rm *.tmp
