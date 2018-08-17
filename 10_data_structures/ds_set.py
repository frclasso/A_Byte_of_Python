bri = set(['Brazil', 'Russia', 'India'])
print('India' in bri)
print('USA' in bri)

bric = bri.copy()
bric.add("China")
print(bric)

print(bric.issuperset(bri))

bri.remove('Russia')
print(bric & bri)  # intersection