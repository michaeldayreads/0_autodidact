# explicit rule
coat shoes modile sweater socks trousers shirt\
pants undershirt:	;	@echo put on $@; touch $@.tmp

# implicit
coat:		shoes mobile sweater
shoes:		socks trousers
mobile:		trousers
sweater:	shirt
trousers:	pants shirt
shirt:		undershirt

tidy:
	rm *.tmp
