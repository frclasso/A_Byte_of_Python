#!/usr/bin/env python3

try:
    text = input('Enter somthing ===>')
except EOFError:
    print("Why did you do EOFERRO on me?")
except KeyboardInterrupt:
    print("You cancelled the operation!")
else:
    print("You entered: {}".format(text))