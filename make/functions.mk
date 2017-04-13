.PHONY: test,alpha,beta
alpha = ls *$(1)*

# beta = ack $(1)

test: # conditional expansion based on command line arg
	@echo working!
	$(if $(bigip_ver),$(call alpha,a),$(call beta,a))
	@echo after if

beta = ack $(1)

