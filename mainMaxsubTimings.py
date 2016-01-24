""" CS 325 Project 1: Maximum sum Subarray Group 13: Janel Buckingham,
Alisha-Crawley Davis, Sara Sakamoto """

import random #to generate random numbers for arrays
import maxsub
import time
import timeit
from timeit import Timer

random.seed()

def generateArray(theArray, n):
	for i in range(n):
		theArray.append(random.randint(-2000,2000))

#store the left index, the right index and max computed sum to return
#results = [0, 0, 0]

#Open file to store timing information
myfile = "timingInfo.txt" #Text file for easy import into Excel
target = open(myfile, 'w')
target.write("n, Algo1, Algo2, Algo3, Algo4\n") #Comma delimited header

"""
Generate arrays to use to test timings
Using at least ten values of n
"""
for n in [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 25000, 50000, 75000, 100000]:
	#Zero out totals and averages
	alg1ave = alg2ave = alg3ave = alg4ave = 0
	alg1total = alg2total = alg3total = alg4total = 0

	#Find average running time of ten input arrays of size n
	for i in range(10):

		# Zero out sums and averages
		alg1time = alg2time = alg3time = alg4time = 0
		results = [0,0,0]

		#Generate array with n random entries
		myArray = []
		generateArray(myArray,n)

		# timeit clocking function time for Algorithm 1
		# To save time, only run timings on Algorithm 1 up to n=1000
		if n<1001:
			t=Timer(lambda: maxsub.maxSubarray1(myArray,results))
			alg1time = t.timeit(number=1)

		# timeit clocking function time for Algorithm 2
		# To save time, only run timings on Algorithm 2 up to n=50000
		if n < 50001:
			t=Timer(lambda: maxsub.maxSubarray2(myArray,results))
			alg2time = t.timeit(number=1)

		# timeit clocking function time for Algorithm 3
		start = 0
		end = len(myArray) -1
		t = Timer(lambda: maxsub.maxSubarray3(myArray, start, end))
		alg3time = t.timeit(number=1)

		# timeit clocking function time for Algorithm 4
		t=Timer(lambda: maxsub.maxSubarray4(myArray,results))
		alg4time = t.timeit(number=1)

		# Add times to the total
		alg1total = alg1total + alg1time
		alg2total = alg2total + alg2time
		alg3total = alg3total + alg3time
		alg4total = alg4total + alg4time

	# Find averages
	alg1ave = alg1total/n
	alg2ave = alg2total/n
	alg3ave = alg3total/n
	alg4ave = alg4total/n

	# Write to file, comma delimited for easier import in Excel
	target.write(str(n))
	target.write(", ")
	target.write(str(alg1ave))
	target.write(", ")
	target.write(str(alg2ave))
	target.write(", ")
	target.write(str(alg3ave))
	target.write(", ")
	target.write(str(alg4ave))
	target.write("\n")
	
target.close()
