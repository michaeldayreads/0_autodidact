# modified from https://realpython.com/blog/python/primer-on-python-decorators/

import time


def timer_function(function_being_decorated):
    def the_decorated_function():
        t1 = time.time()
        function_being_decorated()
        t2 = time.time()
        elapsed = t2 - t1
        print("Time to run function: " + str(elapsed) + "\n")
        print("And the locals are: " + str(locals()) + "\n")
    return the_decorated_function


@timer_function
def syntactic_sugar():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("Sum: " + str((sum(num_list))))

print(syntactic_sugar)

syntactic_sugar()

print(syntactic_sugar)


def sugar_free():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("Sum: " + str((sum(num_list))))

print(sugar_free)

sugar_free = timer_function(sugar_free)

print(sugar_free)

sugar_free()

print(sugar_free)

def still_sugar_free():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("Sum: " + str((sum(num_list))))

print(still_sugar_free)

still_sugar_free = timer_function(still_sugar_free)

print(still_sugar_free)

still_sugar_free()

print(still_sugar_free)

# notice that each instance of decoration is a distinct object
