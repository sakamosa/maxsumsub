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

# open files for reading/writing
in_file = open('MSS_Problems.txt', 'r')
out_file = open('MSS_Results.txt', 'w')

#infinite looping ... 
while (1):
	# read a line from file
	line = in_file.readline()
	# if EOF or if line doesn't contain an array (second condition necessary on MSS_Problems.txt), break
	if (not line) or (len(line) < 2):
		break
	# line is assigned an array created from the integers in line, removing brackets, whitespace, and delimiting commas
	line = [int(i) for i in line.replace("[","").replace(" ","").replace("]","").split(",")]

	print "Algorithm 1"
	# timeit clocking function time
	t = Timer(lambda: maxsub.maxSubarray1(line, results))
	# if we remove this print statement we will need to make sure we still run t.timeit for clocking and to get result
	print "Running time: " + str(t.timeit(number=1))
	# write result as string to file
	out_file.write(str(results))
	out_file.write('\n')

out_file.write('\n')
# rewind to beginning of file and do it again with algorithm 2...
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
# rewind to beginning of file and do it again with algorithm 3...
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
# rewind to beginning of file and do it again with algorithm 4...
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

# close files
out_file.close()
in_file.close()