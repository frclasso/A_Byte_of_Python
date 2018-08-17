ab = {
'Swaroop': 'swaroop@email.com',
'Larry':'larry@email.com',
'Matsumoto':'matsumoto@email.com',
'Spamer':'spamer@email.com'
}

print("Swaroop's email address is:",ab['Swaroop'])

print("\nThere are {} contacts in the address-book.".format(len(ab)))
del ab['Spamer']

print("\nNow there are {} contacts in the address-book.".format(len(ab)))

for name, address in ab.items():
	print("Contact {} at {}".format(name,address))

ab['Guido'] = 'guido@email.com'
if 'Guido' in ab:
	print("Guido address is",ab['Guido'])