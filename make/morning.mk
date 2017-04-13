# the example from http://www.jfranken.de/homepages/johannes/vortraege/make.en.html
#.PHONY: coat shoes mobile sweater socks trousers shirt pants undershirt

coat:		shoes mobile sweater; 	@echo put on $@; touch $@.tmp
shoes:		socks trousers;		@echo put on $@; touch $@.tmp
mobile:		trousers;		@echo put on $@; touch $@.tmp
sweater:	shirt;			@echo put on $@; touch $@.tmp
socks:		;			@echo put on $@; touch $@.tmp
trousers:	pants shirt;		@echo put on $@; touch $@.tmp
shirt:		undershirt;		@echo put on $@; touch $@.tmp
pants:		;			@echo put on $@; touch $@.tmp
undershirt:	;			@echo put on $@; touch $@.tmp
