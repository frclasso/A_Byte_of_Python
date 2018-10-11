#!/usr/bin/env python3

# List comprehension

listOne = [2,3,4]

# listTwo foi criada a partir de listOne
listTwo = [2*i for i in listOne if i > 2]
print(listTwo)