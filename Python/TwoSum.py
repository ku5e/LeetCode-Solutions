#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/01/2022
#Purpose:
def twoSum(arr, x):
	for i in range(len(arr)):
		for j in range(len(arr)):
			if i != j and arr[i] + arr[j] == x:
				return [i, j]
	return -1


nums = [1, 3, 5, 6, 11, 23]
print(twoSum(nums, 9))

