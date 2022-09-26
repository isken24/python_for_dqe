"""
Python for Data Quality Engineers (Run 6)
Home Task 02 - Collections

 1. create a list of random number of dicts (from 2 to 10)
 dict's random numbers of keys should be letter,
 dict's values should be a number (0-100),
 example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

 2. get previously generated list of dicts and create one common dict:
 if dicts have same key, we will take max value, and rename key with dict number with max value
 if key is only in one dict - take it as is,
 example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
"""



import random
import string
from collections import OrderedDict

# 1.
# creating string of lowercase letters as a source for dict keys:
letters = string.ascii_lowercase
# creating variable that will describe lengths of list and dicts:
rnd_len = random.randint(2, 10)
# creating list od dicts using list and dict comprehensions:
lst = [{random.choice(letters): random.randint(0, 100) for _ in range(rnd_len)} for _ in range(rnd_len)]


# 2.
# Creating empty dict that will contain key-value pairs with
# max value, according to the task:
common_dict = {}
# Creating empty dict that will contain key-value pairs with
# value representing number of the dict with max value:
positions = {}

# Let's first iterate through list and then iterate through each dict.
# For each key-value pair we will seek for same key in our common_dict.
# If key is present in common_dict we will compare value from iterated
# dict with the value from common_dict.
# If key form iterated dict is NOT in the common dict, then new key-value pair
# will be added to the common_dict.

for i, dct in enumerate(lst, start=1):
    for key, value in dct.items():
        if key in common_dict:
            if value > common_dict[key]:
                common_dict[key] = value
                positions[key] = i
        else:
            common_dict[key] = value

# Now we will rename keys according to the task.
# If key from "positions" matches with key from "common_dict"
# then new kay-value pair with appropriate key naming will be created and
# old key-value pair will be removed by using pop() method.
for key, value in positions.items():
    common_dict[f'{key}_{value}'] = common_dict.pop(key)

print(dict(sorted(common_dict.items())))
