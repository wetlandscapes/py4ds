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
