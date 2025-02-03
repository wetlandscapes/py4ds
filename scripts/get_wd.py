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

#Note that it prints the key and not the value
for i in my_dict:
    print(i)

#Using just one placeholder with enumerate returns tupple: (<index>, <key>)
for i in enumerate(my_dict):
    print(i)

for index, key in enumerate(my_dict):
    print("Index: " + str(index))
    print("Key: " + str(key))
    print("Value: " + str(my_dict[key]))

#Same for a list
for index, key in enumerate(list(my_dict)):
    print("Index: " + str(index))
    print("Key: " + str(key))
    print("Value: " + str(my_dict[key]))