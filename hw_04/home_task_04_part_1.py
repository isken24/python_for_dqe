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


def create_source_data():
    LETTERS = string.ascii_lowercase
    rnd_len_1 = random.randint(2, 10)
    rnd_len_2 = random.randint(2, 10)
    source_data = [{random.choice(LETTERS): random.randint(0, 100) for _ in range(rnd_len_1)} for _ in range(rnd_len_2)]
    return source_data


def create_common_dict(raw_data: list):
    result = {}
    position = {}
    names = {}
    for index, element in enumerate(raw_data, start=1):
        for key, value in element.items():
            if key in result:
                if value > result[key]:
                    result[key] = value
                    position[key] = index
                names[key] = f'{key}_{position[key]}'
            else:
                result[key] = value
                position[key] = index
    for key, value in names.items():
        result[f'{names[key]}'] = result.pop(key)
    return dict(sorted(result.items()))


if __name__ == "__main__":
    print(create_common_dict(create_source_data()))
