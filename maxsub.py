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
    results[0] = 0
    results[1] = 0
    results[2] = 0
    arrayLen = len(array)
    maxSum = array[0]
    for i in range(0, arrayLen):
        for j in range(0, arrayLen):
            curSum = 0
            index = i
            while index <=j:
                curSum = curSum + array[index]
                if maxSum < curSum:
                    results[0] = i
                    results[1] = j
                    maxSum = curSum
                index += 1
    results[2] = maxSum
    return results

#Better Enumeration
def maxSubarray2(array, results):
    results[0] = 0
    results[1] = 0
    results[2] = 0
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
    results = [0, 0, 0]
    arraylen = len(array)
    if arraylen == 0:
        results[2] = float("-inf")
    if arraylen == 1:
        results[2] = array[0]
    else:
        midpoint = arraylen/2
        x = maxSubarray3(array[0:midpoint])     
        y = maxSubarray3(array[midpoint:arraylen])
        maxSuf = maxSuffix(array[0:midpoint])
        maxPre = maxPrefix(array[midpoint:arraylen])
        z = maxSuf[2] + maxPre[2] 
        if (x[2] >= y[2]) and (x[2] >= z):
            results = x
        elif (y[2] >= x[2]) and (y[2] >= z):
            results[0] = y[0] + midpoint
            results[1] = y[1] + midpoint
            results[2] = y[2]
        else:
            results[2] = z
            results[0] = maxPre[1]
            results[1] = maxSuf[2]
    return results

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
            maxSum = curTotal
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
    results = [0, 0, 0]
    maxSuf = float("-inf")
    if len(array) < 1:
        results[2] = maxSuf
        return results

    else:
        currentTotal = 0
        #start at the end of the array and iterate backwards
        i = len(array)-1
        results[1] = i
        while i >= 0:
            currentTotal += array[i]
            if maxSuf < currentTotal:
                maxSuf = currentTotal
                results[1] = i
            i -= 1
        results[2] = maxSuf
        return results


#Max Prefix
def maxPrefix(array):
    results = [0, 0, 0]
    maxPre = float("-inf")
    if len(array) < 1:
        results[2] = maxPre
        return results

    else:
        currentTotal = 0
        results[0] = 0
        #start at the beginning of the array and iterate forwards
        i = 0
        results[0] = i
        while i < len(array):
            currentTotal += array[i]
            if maxPre < currentTotal:
                maxPre = currentTotal
                results[0] = i
            i += 1
        results[2] = maxPre
        return results


