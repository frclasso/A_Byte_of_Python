zoo = ('python', 'elephant', 'penguin')

print("Number of animals in zoo is:", len(zoo))

newZoo = 'monkey', 'camel', zoo

print('Animals in new zoo is: ',newZoo)
print("Animals brought from  old zoo is: ", newZoo[2])
print("Last animal brought from  old zoo is: ", newZoo[2][2])
print("Number of animals in new zoo is", len(newZoo)-1+len(newZoo[2]))
