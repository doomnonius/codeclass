options = ['Dynamite', 'Pistol', 'Rock', 'Sun', 'Fire', 'Scissors', 'Axe', 'Snake', 'Monkey', 'Woman', 'Man', 'Tree', 'Cockroach', 'Wolf', 'Sponge', 'Paper', 'Moon', 'Air', 'Bowl', 'Water', 'Alien', 'Dragon', 'Devil', 'Lightning', 'Nuke']
options2 = options * 2
import random


def rps25 ():
	'''Takes user input and randomly returns one of the twelve options that defeats that choice'''
	print('')
	print ('Choose from this list of options: ' + str(options))
	print('')
	print('I\'ve made my choice already, and I\'ll reveal it once you\'ve chosen.')
	print('')
	choice = input('Write your choice here: ')
	if checkList(choice, 0):
		print('I had chosen ' + str(compare (choice, indexPosition(choice, 0))) + ', so it looks like I win!' )
		answer = input('Try again? (y/n): ')
		if answer == 'y' or answer == 'Y' or answer == 'yes' or answer == 'Yes':
			rps25()
		elif answer == 'n' or answer == 'N' or answer == 'no' or answer == 'No':
			print('OK! I hope your day is splendid!')
	elif isInt(choice):
		print ('It seems your input is the number ' , int(choice) , ' but you should have entered a word. Do you even understand what you\'re doing?')
	elif isFloat(choice):
		print ('It seems your input is the number ' , float(choice) , ' but you should have entered a word. Do you even understand what you\'re doing?')
	else:
		print ('That is not a valid option, you fat-faced (or maybe just fat-fingered...) spoilsport.')

def distance(first, second):
    '''Returns the edit distance between first and second.'''

    if first == '':
        return len(second)
    elif second == '':
        return len(first)
    elif first[0] == second[0]:
        return distance(first[1:], second[1:])
    else:
        substitution = 1 + distance(first[1:], second[1:])
        deletion = 1 + distance(first[1:], second)
        insertion = 1 + distance(first, second[1:])
        return min(substitution, deletion, insertion)

def isInt (foo):
	'''Takes foo and checks if it is an integer'''
	try:
		int(foo)
		return True
	except:
		return False

def isFloat (foo):
	'''Takes foo and checks if it is an integer'''
	try:
		float(foo)
		return True
	except:
		return False

def checkList (choice, index):
	'''Takes choice and checks if it matches options[index]'''
	if index > 24:
		print('False')
		return False
	elif distance(choice, options[index]) <= 1:
	#elif choice == options[index]:
		return True
	else:
		return checkList(choice, (index+1))

def indexPosition ( choice, index ):
	'''Finds the index position of choice'''
	if index > 24:
		print('Somehow, indexPosition returned False...')
		return False
	elif distance(choice, options[index]) <= 1: #choice == options[index]:
		return index
	else:
		return indexPosition (choice, (index+1))

def compare ( choice, index ):
	'''Takes choice and says what it will beat and what it will lose too'''
	## A choice beats the next 12 in the list and loses to the previous 12.
	## First, create a list variable equal to what it beats - for this one the index will always have at least 12 after it, so we'll be fine.
	beats = options2[(index+1):(index+13)]
	## Second, create a list variable of what it loses to - for this one we always add 25 to index so that we are guaranteed 12 preceding options.
	index = index + 25
	loses = options2[(index-13):(index-1)]
	## Finally, randomly select an option from the beats list variable.
	return random.choice(beats)
