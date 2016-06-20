"""
It is created to check the ability of random module's function - random which creates random floating point numbers from between 0 and  1.
"""
# Watch how to print floats till a particular digit after decimal

import random

# Create a list with all the exponents of two
exp = []
for n in range(11):
	power = 2 ** n
	exp.append(power)

# Inputs
#---------#
# Set initial values DONT SET IT TO ANY INTEGER 
usr_input_no_of_nos = None
usr_input_no_of_interval = None

# Take input from user
def askInputNos(usr_input_no_of_nos):
	'''
	Asks for input from the user.
	'''
	usr_input_no_of_nos_local = input("\n\t\tYou can opt for default value = 1000 just by pressing Enter.\nHow many random numbers to be generated?? ")
	usr_input_no_of_nos = usr_input_no_of_nos_local
	return usr_input_no_of_nos

def askInputInterval(usr_input_no_of_interval):
	'''
	Asks for no. of interval from the user.
	'''
	print("\t\tYou can opt for default value = 4 just by pressing Enter.\n\t\t\tPlease enter a power of 2 for simplification.\n\t\t\t", exp) 
	usr_input_no_of_interval_local = input("How many intervals to be generated?? ")
	usr_input_no_of_interval = usr_input_no_of_interval_local
	return usr_input_no_of_interval

while True:
	try:
		# Assign values to global variables.
		
		usr_input_no_of_nos = askInputNos(usr_input_no_of_nos)
		usr_input_no_of_interval = askInputInterval(usr_input_no_of_interval)
		
		# Check if the user has opted for default values by just pressing enter.
		if usr_input_no_of_nos == "":
			usr_input_no_of_nos = 1000
		if usr_input_no_of_interval == "":
			usr_input_no_of_interval = 4
		
		# Convert usr_input to integer form and check wether they are proper or not.		
		usr_input_no_of_nos = int(usr_input_no_of_nos)
		usr_input_no_of_interval = int(usr_input_no_of_interval)
		
		#Check if user has entered a power of 2.
		count = 0
		for ch in exp:
			if ch == usr_input_no_of_interval:
				count = count + 1
				break
			else:
				pass
		if count == 0:
			raise TypeError
		break
	
	except TypeError:
		print("Please enter a power of 2 so that results are in a simplified form.")

	except ValueError:
		
		print("Please enter a valid integer")
		usr_input_no_of_nos = askInputNos(usr_input_no_of_nos)
		usr_input_no_of_interval = askInputInterval(usr_input_no_of_interval)
	
# Define helper and wrapper functions.

def count_in_range(li, low, high):
	"""
	It counts the no. of times a NUMBER in the list 'li' occurs in the range(low, high) - 
														mathematically - [low, high)
	"""
	count = 0
	for i in range(0, len(li)):
		if low <= li[i] < high:
			count = count + 1
		else:
			pass
	return count

def test_numbers(n):		 # n -- no of random nos to be generated
	 """
	 Creates random numbers
	 """
	 s = [0]
	 test_li = s * int(n)
	 for i in range(int(n)):
	 	test_li[i] = random.random() 
	 	i = i + 1
	 return test_li	   

# Creating a variable with value - a list containing the generated random numbers to be tested.
test_number_list = test_numbers(usr_input_no_of_nos)

def range_length(n):         # n -- no of intervals(buckets) that have to be defined.
	"""
	Defines the range of one Interval(Bucket).
	"""
	length = 1 / int(n)
	return length

# Creating a variable stroring the length(range) of the interval.
var_range_length = range_length(usr_input_no_of_interval) 

def print_table():
	"""
	Prints a table with well defined intervals and no. of numbers in between the interval.
	"""
	print("\n---------------------------------------------------------\nInterval \t \t \t \t  No. of numbers: \n---------------------------------------------------------")
	for i in range(usr_input_no_of_interval):
		print("In the Interval of: " , (var_range_length * i) , "to" , (var_range_length * (i + 1)) , "\t | \t" , count_in_range(test_number_list, (var_range_length * i), (var_range_length * (i + 1))), "\t")
		i = i + 1
	print("---------------------------------------------------------\n")
	return


if __name__ == "__main__":
	print_table()

######################################

# Testing Results -- SUCCESSFULLY TESTED IN PYTHON3.7.6

######################################