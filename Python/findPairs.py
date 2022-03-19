#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: XX/XX/XXXX
#Purpose:
from collections import Counter 

def findPairs(nums, k):
	# Use Counter 
		# O(n) , O(n)

		count = 0

		diction = Counter(nums)

		if k == 0: # then is value >1 means have duplicate then, count += 1
			for du in diction.values():
				if du > 1:
					count += 1
			# print(diction)
		else:
			for key in diction.keys():
				if key+k in diction:
					count += 1
		return count
				
				
print(findPairs([1,3,1,5,4], 0))