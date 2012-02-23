import random

secretNum = random.randint(0, 100)
guesses = []
for x in range (0,10):
	guess = raw_input()
	try:
		guess = int(guess)	
	except:
		guess = 0
	guesses.append(guess)	
	print "Your guess was %i."% guess,
	if guess == secretNum:
		print "You got it!",
		break
	elif guess > secretNum:
		print "It's lower"
	elif guess < secretNum:
		print "It's higher"		
print "The number was %i"% secretNum
print guesses
