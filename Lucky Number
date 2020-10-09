# Python program to check for lucky number 

# Returns 1 if n is a lucky number otherwise returns 0 
def isLucky(n): 
	# Function attribute will act as static variable 
	
	# just for readability, can be removed and used n instead 
	next_position = n 
	
	if isLucky.counter > n: 
		return 1
	if n % isLucky.counter == 0: 
		return 0
	
	# Calculate next position of input number 
	next_position = next_position - next_position / isLucky.counter 
	
	isLucky.counter = isLucky.counter + 1
	
	return isLucky(next_position) 
	
	
# Driver Code 

isLucky.counter = 2 # Acts as static variable 
x = 5
if isLucky(x): 
	print x,"is a Lucky number"
else: 
	print x,"is not a Lucky number"
	
# Contributed by Harshit Agrawal 
