#!/usr/bin/env python3

import pickle

# The name of the file where we will store the object
shoplistfile = 'shoplist.data'
# the list of thigs to buy
shoplist = ['apple', 'mango', 'carrot']

f = open(shoplistfile, 'wb')
# Dump the object to file
pickle.dump(shoplist, f)
f.close()

# Destroy the shoplist variable
del shoplist

# Read back from the storage
f = open(shoplistfile, 'rb')
# Load the object from the file
storedlist = pickle.load(f)
print(storedlist)