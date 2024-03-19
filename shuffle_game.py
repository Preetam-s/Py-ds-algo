from random import shuffle

def shuffle_list(mylist):
	shuffle(mylist)
	return mylist

def Player_guess():
	guess=''
	while guess not in ['0','1','2']:
		guess = input('Chose a guess in 0,1,2')
	return int(guess)

def check_guess(mylist,guess):
	if mylist[guess] =='O':
		print("you guessed right")
	else:
		print("you guessed wrong")
		print(mylist)

#INITIAL LIST
mylist=[' ','O',' ']
#SHUFFLE THE LIST
mixed_up_list = shuffle_list(mylist)
#TAKE IN PLAYER GUESS
guess = Player_guess()
#CHECK GUESS
check_guess(mixed_up_list,guess)
