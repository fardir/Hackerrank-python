#!/bin/python3

import numpy as np

n = int(input())
arr = np.array([input().split() for i in range(n)], float)
np.set_printoptions(legacy='1.13')
print(np.linalg.det(arr))