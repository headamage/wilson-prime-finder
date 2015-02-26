#Wilson's prime number theorem script.
#This script examines a range of numbers given by the user
#and prints on the screen which numbers in that range are prime.
#It uses a single thread.

import math, os, sys, multiprocessing
print "This scripts searches for prime numbers in a range defined by the user.\nThe process is multi-threaded."
x=int(raw_input("Select first number in range: "))
y=int(raw_input("Select last number in range: "))

def wilson(x,y): #define the function that checks the numbers in range.
	lst=[] #create a local blank list to store out primes.
	while (x <= y):
		r= math.factorial(x-1)+1
		v = r % x

		if (v == 0):
			print x, " is Prime"
			lst.append(x) #if prime, append it to our list,

		else:
			print x, " is Not Prime" #if not prime, do nothing
		x=x+1
	return lst #output the local list to the main function.

lst = wilson(x,y) #call the wilson function and store its output in the main list
print "\nFound ", len(lst), " primes.\n"
print lst
