VALID_ORCH_V := k8s-1-4 k8s-1-6
VALID_ORCH_V_MSG := (valid orchestration -- version combinations: k8s 1-4, k8s 1-6)

all:
	@printf "docs..."

ifeq ("$(ov)",) 
	ifeq ("$(bigip_ctlr_tag)", "devel-master")
		orc := kubeadm
		db := 4
	else
		orc := k8s
		db := 5
	endif
else
	ifeq ("$(ov)", "1-4")
		orc := k8s
		db := 0
	else ifeq ("$(ov)", "1-6")
		orc := kubeadm
		db := 1
	else
		db := 3
		$(error ERROR: Invalid orchestration and version combination)
	endif
endif

mu:
	@echo "$(orc)"
	@echo "$(db)"
	@echo "$(sane)"


