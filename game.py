import random


flag = True

while flag:
	num = input("Type a number for a n upper bound: ")


	if num.isdigit():
		print("Lets play the game !!!")
		num = int(num)
		flag = False
	else:
		print("Invalid input \nTry Again !!!")


secret = random.randint(1,num)


guess = None
count = 1


while guess != secret:
	guess = input("PLease type a number between 1 and " + str(num) + ": ")
	if guess.isdigit():
		guess = int(guess)

	if guess == secret:
		print("YOu got it !!!")
	else:
		print("Please try again")
		count = count+1
print("It took you " + str(count) +" guesss") 

		