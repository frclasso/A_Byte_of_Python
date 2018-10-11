#!/usr/bin/env python3


def powerSum(power, *args):
    """Return the sum of each argument raised to the specified power"""
    total = 0
    for i in args:
        total += pow(i, power)
    return total


print(powerSum(2,3,4))  # 3**2 = 9 + 4**2 =16 //total = 25
print(powerSum(2, 10)) # 10**2
