import time # includes a module named time
import random #includes a module named random
from rps_functions import *

name = input('Hi... what is your name? ')
print ('')

if name == 'Lucas' or name == 'Luke':
	print ('I\'m sorry, I stopped listening for a second there.')
	time.sleep(3)
	answer = input('Anyway, stranger, how about a game or RPS 25? (y/n): ')
	if answer == 'y' or answer == 'Y' or answer == 'yes' or answer == 'Yes':
		rps25()
	elif answer == 'n' or answer == 'N' or answer == 'no' or answer == 'No':
		print('OK! I hope your day is splendid!')

elif name == 'Otto':
	print('Not *that* Otto?!?!')
	time.sleep(1.5)
	print('Wow! It\'s an honor to meet you!')
	time.sleep(.5)
	answer = input('Would you like play a game of RPS 25 with me? (y/n): ')
	if answer == 'y' or answer == 'Y' or answer == 'yes' or answer == 'Yes':
		rps25()
	elif answer == 'n' or answer == 'N' or answer == 'no' or answer == 'No':
		print('OK! I hope your day is splendid!')

else:
	print ('Welcome, ', name, '. Let\'s play rock, paper, scissors! I\'ve made my choice, now it\'s your turn!')
	rps25()
