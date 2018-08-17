shoplist = ['apple', 'mango', 'carrot', 'banana']

print("I have ", len(shoplist),'items to purchase.')

print("These items are:")
for k, item in enumerate(shoplist):
	print(k,'->', item)

print()
print("\nI also have to buy rice.")
shoplist.append('rice')
print("My shoplist is now:",shoplist)
print()

print("I will sort my list now:")
shoplist.sort()
print("Sorted shopping list is:",shoplist)
print()

print("The first item I will buy is:",shoplist[0])
olditem = shoplist[0]

del shoplist[0]
print("I bought the",olditem)
print("My shoplist is now: ",shoplist)

