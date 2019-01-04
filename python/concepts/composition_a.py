"""
Stub out POC for multicloud embeded client.
Desire is for a simple API for an abstraction that spans clouds,
yet with minimal boiler plate and (if possible) avoiding ABC or other 
multi inheritance or mixin pattern.

I did explore those alternatives, but the implementation always required more
code - and more complex code - and in the end the invocations always ended
up along the lines of:

    awc = AmazonAWC()
    awc = AzureAWC()

when the whole point is that this was for tests that will run on one provider
per run / or per process and the tests should be the same for all providers.

Thus;

    awc = AWC()
    awc.client.scale_out(3) 

etc.

"""

# the tests are told which provider they should test on...

cloud_config = {"provider":"aws"}


class AWC(object):
    """Autoscale Workload Collection"""
    def __init__(self, min_inst=1, max_inst=10, des_inst=1, svr='http', port=80):
        self.config = {}
        self.config['min'] = min_inst
        self.config['max'] = max_inst
        self.config['des'] = des_inst
        self.config['svr'] = svr
        self.config['port'] = port
        self.client = AWC._client_helper(cloud_config['provider'])
        self.client.create(self.config)
        
    @staticmethod
    def _client_helper(provider):
        if provider is not 'aws':
            raise NotImplementedError
        else:
            return AWS_client()


class AWS_client(object):
    """An autoscale group in AWS"""
    def __init__(self):
        self.autoscale = "mock boto autoscale client"
        self.ec2 = "mock boto ec2 client"

    def create(self, config):
        print("Create the launch config with all the params:")
        print(config)
        print("create the autoscale group based on those params...")


    def scale_out(self, n):
        print(("AWS to scale out to {} backends".format(n)))

    def scale_in(self, n):
        print(("AWS to scale in to {} backends".format(n)))


awc = AWC()
assert 0 == 0  # mock test

awc.client.scale_out(4)
assert 4 == 4  # mock test

awc.client.scale_in(3)
assert 3 == 3  # mock test

