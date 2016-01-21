"""
Four functions to compute the maximum subarray of an array of numbers.
Parameters:
    An array of integers, at least one of which is positive
    An array to hold the results
Return Value:
    Results[ left index of max sub array, right index of max sub array, max sum]
"""
#Enumeration
def maxSubarray1(array, results):
    arrayLen = len(array)
    maxSum = array[0]
    for i in range(0, arrayLen):
        for j in range(0, arrayLen):
            curSum = sum(array[i:j])
            if maxSum < curSum:
              results[0] = i
              results[1] = j
              maxSum = curSum
    results[2] = maxSum
    return results

#Better Enumeration
def maxSubarray2(array, results):
    arrayLen = len(array)
    maxSum = array[0]
    for i in range(0, arrayLen):
        curSum = 0
        for j in range(i, arrayLen):
            curSum += array[j]
            if maxSum < curSum:
                results[0] = i
                results[1] = j
                maxSum = curSum
    results[2] = maxSum
    return results

#Divide and Conquer
def maxSubarray3(array):
    arraylen = len(array)
    if arraylen == 0:
        return 0
    if arraylen == 1:
        return array[0]
    else:
        midpoint = arraylen/2
        x = maxSubarray3(array[0:midpoint])     
        y = maxSubarray3(array[midpoint+1:arraylen])
        z = maxSuffix(array[0:midpoint]) + maxPrefix(array[midpoint+1:arraylen])
        return max(x, y, z)


#Linear Time
def maxSubarray4(array, results):
    arrayLen = len(array)
    if arrayLen < 1:
        return 0
    maxSum = float("-inf")
    curTotal = float("-inf")
    for j in range(0, arrayLen):
        curRight = j
        if curTotal > 0:
            curTotal += array[j]
        else:
            curLeft = j
            curTotal = array[j]
        #update the results with new maxSum, and subarray indexes
        if curTotal > maxSum:
            results[0] = curLeft
            results[1] = curRight
            results[2] = curTotal
    return results

"""
Helper functions for Divide and Conquer Algorithm, computes
max suffix and prefix of an array
"""

#Max Suffix
def maxSuffix(array):
    if len(array) < 1:
        return 0
    maxSuf = 0
    currentTotal = 0
    #start at the end of the array and iterate backwards
    for i in range((len(array)-1), 0):
        currentTotal += array[i]
        if maxSuf < currentTotal:
            maxSuf = currentTotal
    return maxSuf

#Max Prefix
def maxPrefix(array):
    if len(array) < 1:
        return 0
    maxPre = 0
    currentTotal = 0
    for i in array:
        currentTotal += i
        if maxPre < currentTotal:
            maxPre = currentTotal
    return maxPre

