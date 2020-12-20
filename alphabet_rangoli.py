#!/bin/python3

def print_rangoli(size):
    for i in range(-(size - 1), size):
        for j in range(-2 * (size - 1), 2 * (size - 1) + 1):
            if j % 2 == 0 and (abs(j // 2) + abs(i)) < size:
                print(chr(abs(j // 2) + abs(i) + ord('a')), end='')
            else:
                print('-', end='')
        print()

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)