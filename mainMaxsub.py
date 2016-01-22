""" CS 325 Project 1: Maximum sum Subarray Group 13: Janel Buckingham,
Alisha-Crawley Davis, Sara Sakamoto """

import maxsub
import time
import timeit
from timeit import Timer


#Test Array taken from MSS_Test
#testArray = [10, -11, -1, -9, 33, -45, 23, 24, -1, -7 -8, 19]   
#longer array for timeit testing purposes
#testArray2 = [10, -11, -1, -9, 33, -45, 23, 24, -1, -7 -8, 19, 100, -41, -12, -19, 33, -55, 22, 24, -2, -17 -81, 59, 10, -11, -1, -9, 33, -45, 23, 24, -1, -7 -8, 19, 100, -41, -12, -19, 33, -55, 22, 24, -2, -17 -81, 59, 10, -11, -1, -9, 33, -45, 23, 24, -1, -7 -8, 19, 100, -41, -12, -19, 33, -55, 22, 24, -2, -17 -81, 59, 10, -11, -1, -9, 33, -45, 23, 24, -1, -7 -8, 19, 100, -41, -12, -19, 33, -55, 22, 24, -2, -17 -81, 59] 

#store the left index, the right index and max computed sum to return
results = [0, 0, 0]

"""
Call each algorithm, passing the test array through the timer wrapper
the 'number' variable indicates how many times you want the function to run
for time tests
"""

in_file = open('MSS_Problems.txt', 'r')
out_file = open('MSS_Results.txt', 'w')

while (1):
	line = in_file.readline()
	if (not line) or (len(line) < 2):
		break
	line = [int(i) for i in line.replace("[","").replace(" ","").replace("]","").split(",")]
#	if len(line) != 0
	print "Algorithm 1"
	t = Timer(lambda: maxsub.maxSubarray1(line, results))
	print "Running time: " + str(t.timeit(number=1))
	out_file.write(str(results))
	out_file.write('\n')

out_file.write('\n')
in_file.seek(0)
while (1):
	line = in_file.readline()
	if (not line) or (len(line) < 2):
		break
	line = [int(i) for i in line.replace("[","").replace(" ","").replace("]","").split(",")]
	print "Algorithm 2"
	t = Timer(lambda: maxsub.maxSubarray2(line, results))
	print "Running time: " + str(t.timeit(number=1))
	out_file.write(str(results))
	out_file.write('\n')

out_file.write('\n')
in_file.seek(0)
while (1):
	line = in_file.readline()
	if (not line) or (len(line) < 2):
		break
	line = [int(i) for i in line.replace("[","").replace(" ","").replace("]","").split(",")]
	print "Algorithm 3"
	t = Timer(lambda: maxsub.maxSubarray3(line))
	print "Running time: " + str(t.timeit(number=1))
	out_file.write(str(maxsub.maxSubarray3(line)))
	out_file.write('\n')

out_file.write('\n')
in_file.seek(0)
while (1):
	line = in_file.readline()
	if (not line) or (len(line) < 2):
		break
	line = [int(i) for i in line.replace("[","").replace(" ","").replace("]","").split(",")]
	print "Algorithm 4"
	t = Timer(lambda: maxsub.maxSubarray4(line, results))
	print "Running time: " + str(t.timeit(number=1))
	out_file.write(str(results))
	out_file.write('\n')


out_file.close()
in_file.close()