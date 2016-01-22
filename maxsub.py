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
def maxSubarray3(array, start, end, results):
    suffixRet = ""
    prefixRet = ""
    arraylen = end - start
    if start > end:
        return float("-inf")
    if start == end:
        return array[start]
    else:
        midpoint = arraylen//2 + start
        x = maxSubarray3(array, start, midpoint, results)     
        y = maxSubarray3(array, midpoint +1, end, results)
        z1 = maxSuffix(array, start, midpoint, suffixRet)
        z2 = maxPrefix(array, midpoint +1, end, prefixRet)
        z = z1 + z2
        maxSum = max(x, y, z)

        if (maxSum == z):
            start = prefixRet
            end = suffixRet
            
        results[0] = start
        results[1] = end
        results[2] = maxSum

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
def maxSuffix(array, start, end, suffixRet):
    if (end - start) < 0:
        return float("-inf")
    maxSuf = float("-inf")
    currentTotal = 0
    #start at the end of the array and iterate backwards
    i = end
    j = start
    while i >= j:
        currentTotal += array[i]
        if maxSuf < currentTotal:
            maxSuf = currentTotal
            suffixRet = i
        i -= 1
    return maxSuf

#Max Prefix
def maxPrefix(array, start, end, prefixRet):
    if (end - start) < 0:
        return float("-inf")
    maxPre = float("-inf")
    currentTotal = 0
    #start at the beginning of the array and iterate forwards
    i = start
    j = end
    while i <= j:
        currentTotal += array[i]
        if maxPre < currentTotal:
            maxPre = currentTotal
            prefixRet = j
        i += 1
    return maxPre


