# Python for Data Quality Engineers (Run 6)
# Home Task 02 - Collections

#1. create a list of random number of dicts (from 2 to 10)
import random
import string

letters = string.ascii_lowercase
rnd_len = random.randint(2,10)
lst = [{random.choice(letters): random.randint(0,100) for _ in range(rnd_len)} for _ in range(rnd_len)]
print(lst)
print(letters)
#dict's random numbers of keys should be letter,
#dict's values should be a number (0-100),
#example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
#2. get previously generated list of dicts and create one common dict:


#if dicts have same key, we will take max value, and rename key with dict number with max value
#if key is only in one dict - take it as is,
#example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
common_dict = {}
for dct in range(len(lst)):
    for key, value in dct.items():
        if key in common_dict:
            if value > common_dict[key]:
                common_dict[key] =