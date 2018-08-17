number = 25
running = True

while running:
    guess = int(input("Digite um numero: "))
	
    if guess ==  number:
        print("Congratulations, you guessed it. ")
        running = False
    elif guess < number:
        print("No, it's a little higher than that")
    else:
        print("No, it's a little lower than that.")
else:
	print("The while loop is over")
print("Done.")