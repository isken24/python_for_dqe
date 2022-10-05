"""
Refactor homeworks from module 2 and 3 using functional approach with decomposition.

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

# 1.
# creating string of lowercase letters as a source for dict keys:
letters = string.ascii_lowercase
# creating variable that will describe lengths of list:
rnd_len_1 = random.randint(2, 10)
rnd_len_2 = random.randint(2, 10)
# creating list od dicts using list and dict comprehensions:
lst = [{random.choice(letters): random.randint(0, 100) for _ in range(rnd_len_1)} for _ in range(rnd_len_2)]


# 2.
# Creating empty dict that will contain key-value pairs with
# max value, according to the task:
#common_dict = {}

# Creating empty dict that will contain key-value pairs with
# value representing number of the dict with max value:
#position = {}

# Creating empty dict that will contain key-value pairs that
# then will be used to rename keys in common dict:
#names = {}

# Let's first iterate through list and then iterate through each dict.
# For each key-value pair we will seek for same key in our common_dict.
# If key is present in common_dict we will compare value from iterated
# dict with the value from common_dict in order to find max value.
# Number of the dict with max value for specified key will be stored in
# 'position' dict.
# 'names' dict will store new key-names for 'common_dict, only if comparison
# of values will occur.
# If key form iterated dict is NOT in the common dict, then new key-value pair
# will be added to the common_dict.
def create_common_dict(lst):
    common_dict = {}
    position = {}
    names = {}
    for i, dct in enumerate(lst, start=1):
        for key, value in dct.items():
            if key in common_dict:
                if value > common_dict[key]:
                    common_dict[key] = value
                    position[key] = i
                names[key] = f'{key}_{position[key]}'
            else:
                common_dict[key] = value
                position[key] = i
    for key, value in names.items():
        common_dict[f'{names[key]}'] = common_dict.pop(key)
    return(dict(sorted(common_dict.items())))
# Now we will rename keys according to the task.
# If key from "names" matches with key from "common_dict"
# then new kay-value pair with appropriate key naming will be created and
# old key-value pair will be removed by using pop() method.
#for key, value in names.items():
#    common_dict[f'{names[key]}'] = common_dict.pop(key)

#print(dict(sorted(common_dict.items())))

if __name__ == "__main__":
    create_common_dict(lst)