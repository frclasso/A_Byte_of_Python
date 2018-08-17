number = 25
guess = int(input("Digite um numero: "))


if guess ==  number:
	print("Congratulations, you guessed it. ")
elif guess < number:
	print("No, it's a little higher than that")
else:
	print("No, it's a little lower than that.")

print("Done.")