#!/usr/bin/env python3

# Assertion

myList = ['item']


def verify():
    assert len(myList) >=1
    return "OK"


print(verify())