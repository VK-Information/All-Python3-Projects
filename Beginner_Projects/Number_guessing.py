import random

num = random.randrange(1,10)
guess = int(input("Enter any Number(1-10): "))
while num != guess:
	if guess < num:
		print("Too low")
		guess = int(input("Enter number again: "))
	elif guess > num:
		print("Too high")
		guess = int(input("Enter number again: "))
	else:
		break

print(f"You have guess it right, The Answer is {guess}")
