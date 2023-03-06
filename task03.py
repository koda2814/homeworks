"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:

    nums = []
    with open(file_name) as f:
        for line in f:
            nums.extend(line.split()) #list of numbers, each element has type 'str'
        nums = [int(x) for x in nums] #now each element of list has type 'int'

        return (max(nums), min(nums))

