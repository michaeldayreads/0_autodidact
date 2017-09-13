class _k8s(object):

    # __dict__ = {"fooi": "bar"}

    configs = {
          "foo" : 
            }

    def __getattr__(self, x):
        print(self.__dict__[x])

    def __init__(self):
        self._clusterroles = _ClusterRoleManager(self)
        print("k8s init")

    @property
    def clusterroles(self):
        return self._clusterroles


class _ClusterRoleManager(object):

    # configs = {"_k8s": "foo", 
    #           "Openshift": "bar"}

    def __init__(self, orchestration):
        self.orchestration = orchestration
        self.cluster
        self.cluster_role_config = {"foo": "bar"}
        self.cluster_role_binding = {"foo": "bar"}
        self.base_cmd = ['kubectl']
        print("k8s clusterRoleManager")

    def run_cmd(base_cmd, add_cmd):
        cmd = base_cmd + add_cmd
        print(cmd)

    def createRole(self, name):
        pass
