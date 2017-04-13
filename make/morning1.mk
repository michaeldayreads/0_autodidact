# declare variable
articles = coat shoes mobile sweater socks\
	   trousers shirt pants undershirt

# explicit rule assigns commands
$(articles)	:; @echo put on $@; touch $@.tmp

# implicit rule state prerequisites
coat:		shoes mobile sweater
shoes:		socks trousers
mobile:		trousers
sweater:	shirt
trousers:	pants shirt
shirt:		undershirt

