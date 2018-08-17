#!/usr/bin/env python3

f = open('poem.txt', 'w')
f.write('New line of poem.\nAnother Line.')
f.close()

f = open('poem.txt')
while True:
    line = f.readline()
    # Zero length indicates EOF
    if len(line) == 0:
        break

    print(line)

f.close()