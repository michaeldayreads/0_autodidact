api_label = 'rbac'
k8s_apis = {'rbac_k8s': 'rbac.authorization.k8s.io/v1beta',
                        'rbac_openshift': 'v1'}
api_key = api_label + '_' + 'k8s' + foo

if api_key not in k8s_apis:
    print("return false")
else:
    api = k8s_apis[api_key]
    print("look for api key:" + api_key)
    print(api)

