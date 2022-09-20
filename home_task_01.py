# Python for Data Quality Engineers (Run 6)
# Home Task 01 - Python Basics

import random

# 1. Create list of 100 random numbers from 0 to 1000:

# We will use randint() method to generate random numbers
# that then will be used in list comprehention.
# lenghts - represents lengths of the list.
length = 100
int_list = [random.randint(0, 1000) for _ in range(length)]


# 2. Sort list from min to max (without using sort())

# We will use buble sort method to complete this task.
# Each element of the list will be compared with next element
# and if value of element is greater than value of next element
# they will be swapped by each other. In order to check all of the
# elements we need to implement for-loop and nested for-loop.
# Nested for-loop can skip last 'i' elements since they have been already
# sorted in first for-loop.
for i in range(length-1):
    for j in range(length-1-i):
        if int_list[j] > int_list[j+1]:
            int_list[j], int_list[j+1] = int_list[j+1], int_list[j]


# 3. Calculate average for even and odd numbers

# Creating two blank lists for even and odd numbers:
even_numbers = []
odd_numbers = []

# Searching for even and odd numbers in int_list:
for el in int_list:
    if el % 2 == 0:
        even_numbers.append(el)
    else:
        odd_numbers.append(el)

# Calculating average for even numbers, if there are even numbers
# ZeroDivisionError will be raised, since we can't divide by 0:
try:
    avg_even_numbers = sum(even_numbers) / len(even_numbers)
except ZeroDivisionError:
    print('No even numbers were found.')

# Calculating average for odd numbers, if there are odd numbers
# # ZeroDivisionError will be raised, since we can't divide by 0:
try:
    avg_odd_numbers = sum(odd_numbers) / len(odd_numbers)
except ZeroDivisionError:
    print('No odd numbers were found.')


# 4. Print both average result in console
print(avg_even_numbers)
print(avg_odd_numbers)
