""" CS 325 Project 1: Maximum sum Subarray Group 13: Janel Buckingham,
Alisha-Crawley Davis, Sara Sakamoto """

import maxsub
import time
import timeit
from timeit import Timer

#Test Array taken from MSS_Test
testArray = [10, -11, -1, -9, 33, -45, 23, 24, -1, -7 -8, 19]   
testArray2 = [10, -11, -1, -9, 33, -45, 23, 24, -1, -7 -8, 19, 100, -41, -12, -19, 33, -55, 22, 24, -2, -17 -81, 59, 10, -11, -1, -9, 33, -45, 23, 24, -1, -7 -8, 19, 100, -41, -12, -19, 33, -55, 22, 24, -2, -17 -81, 59, 10, -11, -1, -9, 33, -45, 23, 24, -1, -7 -8, 19, 100, -41, -12, -19, 33, -55, 22, 24, -2, -17 -81, 59, 10, -11, -1, -9, 33, -45, 23, 24, -1, -7 -8, 19, 100, -41, -12, -19, 33, -55, 22, 24, -2, -17 -81, 59] 

#store the left index, the right index and max computed sum to return
results = [0, 0, 0]

"""
Call each algorithm, passing the test array through the timer wrapper
the 'number' variable indicates how many times you want the function to run
for time tests
"""

print "Algorithm 1"
t = Timer(lambda: maxsub.maxSubarray1(testArray2, results))
print "Running time: " + str(t.timeit(number=1))
print maxsub.maxSubarray1(testArray, results)

print "Algorithm 2"
t = Timer(lambda: maxsub.maxSubarray2(testArray2, results))
print "Running time: " + str(t.timeit(number=1))
print maxsub.maxSubarray2(testArray, results)

print "Algorithm 3"
t = Timer(lambda: maxsub.maxSubarray3(testArray2))
print "Running time: " + str(t.timeit(number=1))
print maxsub.maxSubarray3(testArray)

print "Algorithm 4"
t = Timer(lambda: maxsub.maxSubarray4(testArray2, results))
print "Running time: " + str(t.timeit(number=1))
print maxsub.maxSubarray4(testArray, results)
