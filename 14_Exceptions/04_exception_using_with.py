#!/usr/bin/env python3

import sys
import time

f = None
try:
	with open("poem.txt") as f:
		for line in f:
			print(line)
			sys.stdout.flush()
			print("Press crtl+c now!")
			time.sleep(2)
except IOError:
	print("Could not find poem.txt")
except KeyboardInterrupt:
	print("You cancelled the reading from the file")
finally:
	if f:
		f.close()
	print("Cleaning up, closing the file.")


print("Done.")