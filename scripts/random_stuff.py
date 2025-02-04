import os

os.getcwd()

my_tuple = (1, "b", 3.0)
type(my_tuple)
len(my_tuple)

# Aliasing lists
A = ["banana"]
B = A
A[0] = "split"
B # Result: ["split"]

# Cloning lists
A = ["banana"]
B = A[:]
A[0] = ["split"]
B # Result: ["banana"]

my_dict = {1: "A", "B": 3}
my_dict

my_dict[1] # "A"
my_dict[0] # Error
0 in my_dict # False
1 in my_dict # True

list(my_dict.keys())

my_set = {"my", "stuff", "things", "lorem", "stuff"}
my_set

for i in range(5):
    print(i)

# Note that it prints the key and not the value
for i in my_dict:
    print(i)

# Using just one placeholder with enumerate returns tupple: (<index>, <key>)
for i in enumerate(my_dict):
    print(i)

for index, key in enumerate(my_dict):
    print("Index: " + str(index))
    print("Key: " + str(key))
    print("Value: " + str(my_dict[key]))

# Same for a list
for index, key in enumerate(list(my_dict)):
    print("Index: " + str(index))
    print("Key: " + str(key))
    print("Value: " + str(my_dict[key]))

for x in range(0, 3):
    print(x)

sum(['a', 'b', 'c']) # Error
sum([5, 2, 4]) # 11

def my_func():
    pass
    return None

my_func()

def print_names(*names):
	print(type(names))

print_names("John", "Jim", "Jerry") # <class 'tupple'>

def print_names(*names):
	for name in names:
		print(name)

print_names("John", "Jim", "Jerry")


def print_names(**names):
	print(type(names))

print_names(a="John", b="Jim", c="Jerry") # <class 'dict'>

def print_names(**names):
	for key in names:
		print(names[key])

print_names(a="John", b="Jim", c="Jerry")

L = [1, 3, 2]
sorted(L)


class Circle:
    
    name = "Circle"
	
    def __init__(self, radius = 0, color = 'grey'):
        self.radius = radius
        self.color = color

    def set_radius(self, r):
        self.radius = r

my_circle = Circle()
my_circle.radius # 0
my_circle.color # 'grey'
my_circle.name # 'Circle'

other_circle = Circle(3, "blue")
other_circle.radius # 3
other_circle.color # 'blue'

other_circle.set_radius(r = 12)
other_circle.radius # 12
other_circle.color # 'blue'
other_circle.name # 'Circle'
