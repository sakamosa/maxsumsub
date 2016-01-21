""" CS 325 Project 1: Maximum sum Subarray Group 13: Janel Buckingham,
Alisha-Crawley Davis, Sara Sakamoto """

import maxsub
import time

#Test Array taken from MSS_Test
testArray = [10, -11, -1, -9, 33, -45, 23, 24, -1, -7 -8, 19]   

#store the left index, the right index and max computed sum to return
results = [0, 0, 0]

"""
Call each algorithm, passing the test array through the timer wrapper
the 'number' variable indicates how many times you want the function to run
for time tests
"""

print "Algorithm 1"
print maxsub.maxSubarray1(testArray, results)

print "Algorithm 2"
print maxsub.maxSubarray2(testArray, results)

print "Algorithm 3"
print maxsub.maxSubarray3(testArray)

print "Algorithm 4"
print maxsub.maxSubarray4(testArray, results)
