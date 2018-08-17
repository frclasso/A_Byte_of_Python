print("Simple Assignment")

shoplist=['apple', 'mango','pear', 'orange']
mylist = shoplist

del shoplist[0]
print("shoplist is", shoplist)
print("mylist is", mylist)

print()
print("Copy by make a full slice")
mylist = shoplist[:]
del mylist[0]
print("shoplist is", shoplist)
print("mylist is", mylist)

