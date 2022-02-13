from sys import maxint
def maxSubArraySum(array):
	sum = 0
	maxSum = -maxint -1 
	for i in  range(len(array)):
	    sum = sum + array[i]
	    if sum > maxSum:
	        maxSum = sum
	    if sum < 0:
	        sum = 0
	return sum    