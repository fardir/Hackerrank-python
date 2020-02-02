#!/bin/python3

import os


# Complete the solve function below.
def solve(s):
    nama = s.split(' ')
    # str = ' '.join(kata.capitalize() for kata in nama)
    str = ''
    for kata in nama:
        kata = kata.replace(kata, kata.capitalize())
        str += kata + ' '
    # print(str)
    return str


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
