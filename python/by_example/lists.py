my_list = ['a', 'b', 'c']

for item in my_list:
    print(item)

my_list_of_dicts = [{'ip': '10.0.0.0', 'port': 80 },{'ip': '10.0.0.1', 'port': 443 }]

for i, v in enumerate(my_list_of_dicts):
    print("Index: %i  Value: %s" % (i, v))

for instance in my_list_of_dicts:
    print("ip: %s  port: %i" % (instance['ip'], instance['port']))


