"""
CSSE1001 Assignment 1
Semester 2, 2020
"""

from a1_support import *

# Fill these in with your details
__author__ = "{{hongfei.shen}} ({{s4610279}})"
__email__ = "hongfei.shen@uqconnect.edu.au"
__date__ = "4.9.2020"


# Write your code here (i.e. functions)
def prompt():
	"""(str) Prompts the user for input and return a response"""
	return input(INPUT_ACTION)
def prompt2():
	"""(str) Prompts the user for input and return a response"""
	return input("Do you want a FIXED or ARBITRARY length word?:")

def main():
    """
    Handles top-level interaction with user.
    """
    # Write the code for your main function here
while True:
	response = prompt()
	if response == "s":
		while True:
			response = prompt2()
			if response == "FIXED":
				pass
			elif response =="ARBITRARY":
				pass
	elif response == "h":
		print(HELP)
	elif response == "q":
		print("Thank you for playing")
		break
	elif response == "":
		print(INVALID)
		
	
if __name__ == "__main__":
    main()
