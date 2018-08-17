while True:
	s = input("Digite uma string qualquer ou 'quit' para parar:' ")
	if s == 'quit':
		break
	if len(s) < 3:
		print("Too Small")
		continue
	print('The length of the string is: ',len(s))
print('Done.')