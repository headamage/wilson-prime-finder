#Wilson's prime number theorem script.
#This script examines a range of numbers given by the user
#and prints on the screen which numbers in that range are prime.
#This script can use multiple cores, the number defined by the user.

import math, os, sys
import multiprocessing as mp
x=int(raw_input("Select first number in range: "))
y=int(raw_input("Select last number in range: "))
c=int(raw_input("How many cores to use?: "))

def wilson(x):                  #define the function that checks a number.
	
	r= math.factorial(x-1)+1        #Wilson'd formula.
	v = r % x                       #Wilson's formula.

	if (v == 0):
		print x, " is Prime"
		return x #when prime is found, return it to the main process so we can append it to the list.
		
	else:
		print x, " is Not Prime" #when not a prime, return nothing to the main process.

if __name__ == '__main__':
	pool=mp.Pool(processes=c)       #create a job pool and define the number of cores to use.
	results = pool.map(wilson, range(x,y)) #assign the function to the pool and fill it with jobs

	results = filter(None, results) #when a number is not prime, the function returns "None". we eliminate "None" to keep only the primes.
	print "\Found ", len(results), " primes.\n"
	print results
