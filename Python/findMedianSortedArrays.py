#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/04/2022
#Purpose: findMedianSortedArrays
def findMedianSortedArrays(nums1, nums2):
	nums = nums1 + nums2
	nums.sort()
	l = (len(nums) // 2)
	if(len(nums) % 2 == 0):
		return (nums[l] + nums[(l - 1)]) / 2
	else:
		return (float(nums[len(nums) // 2]))

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

print(findMedianSortedArrays(nums1, nums2))
