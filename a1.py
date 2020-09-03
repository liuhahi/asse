"""
CSSE1001 Assignment 1
Semester 2, 2020
"""

from a1_support import (
	INPUT_ACTION,
	INVALID,
	WELCOME,
	HELP,
	WALL_VERTICAL,
	WALL_HORIZONTAL,
	GUESS_INDEX_TUPLE,
	VOWELS,
	CONSONANTS,	
	load_words,
	random_index,
)

# Fill these in with your details
__author__ = "{{hongfei.shen}} ({{s4610279}})"
__email__ = "hongfei.shen@uqconnect.edu.au"
__date__ = "4.9.2020"
# Write your code here (i.e. functions)
def prompt(action):
		"""(str) Prompts the user for input and return a response"""
		return input(action)

def select_word_at_random(word_select):
		""" Given the word select is either “FIXED” or “ARBITRARY” this function will return a string randomly
				selected from WORDS FIXED.txt or WORDS ARBITRARY.txt respectively. If word select is anything
				other then the expected input then this function should return None"""
		if word_select != "FIXED" and word_select != "ARBITRARY":
				return
		words = load_words(word_select)
		return words[random_index(words)]

def create_guess_line(guess_no, word_length):
		"""GUESS_INDEX_TUPLEThis function returns the string representing the display corresponding to the guess number integer, guess no."""
		line = ""
		start = GUESS_INDEX_TUPLE[word_length - 6][guess_no - 1][0]
		end = GUESS_INDEX_TUPLE[word_length - 6][guess_no - 1][1]
		for n in range(word_length):
				line += WALL_VERTICAL
				if n >= start and n <= end:
						line += ' * '
				else:
					  line += ' - '
		return 'Guess {}{}{}'.format(guess_no, line, WALL_VERTICAL)	

def compute_value_for_guess(word, start_index, end_index, guess):
		"""Return the score, an integer, the player is awarded for a specific guess. The word is a string representing the
		word the player has to guess. The substring to be guessed is determined by the start index and end index.
		The substring is created by slicing the word from the start index up to and including the end index. The
		guess is a string representing the guess attempt the player has made."""
		return 10

def create_border(length):
		""" display border """
		line = WALL_HORIZONTAL
		for n in range(length * 4 + 8):
				line += WALL_HORIZONTAL
		return line

def display_guess_matrix(guess_no, word_length, scores):
		"""This function prints the progress of the game. This includes all line strings for guesses up to guess no with
		their corresponding scores (a tuple containing all previous scores), and the line string for guess no (without
		a score)."""
		# header
		header = "       {}".format(WALL_VERTICAL)
		for n in range(1, word_length + 1):
				header += " {} |".format(n)		
		print(header)
		print(create_border(word_length))
		for g in range(guess_no):
				print(create_guess_line(guess_no, word_length))
				print(create_border(word_length))
		return

def compute_value_for_guesss(word, start_index, end_index, guess):
		"""Return the score, an integer, the player is awarded for a specific guess. The word is a string representing the
		word the player has to guess. The substring to be guessed is determined by the start index and end index.
		The substring is created by slicing the word from the start index up to and including the end index. The
		guess is a string representing the guess attempt the player has made."""
		score = 0
		return score

def main():
		"""
		Handles top-level interaction with user.
		"""
		print(WELCOME)
		while True:	
				response = prompt(INPUT_ACTION)
				if response == "s":
						word_select = ""
						# while word_select != "FIXED" and word_select != "ARBITRARY":
						# 		word_select = prompt('Do you want a "FIXED" or "ARBITRARY" length word?')
						word = select_word_at_random("FIXED")
						guess_no = 1
						word_length = len(word)
						print('Now try and guess the word, step by step!!')
						print('word is', word)		
						scores = (10, )			
						while guess_no < 5:
								display_guess_matrix(guess_no, word_length, scores)								
								ans = prompt('Now enter Guess {}:'.format(guess_no))
								scores = (10, )
								scores += (10, )
								guess_no += 1
						# create_guess_line(word, word_length)
				elif response == "h":	
						print(HELP)
				elif response == "q":
						print("Thank you for playing")
						break
				else:
						print(INVALID)

if __name__ == "__main__":
		main()
