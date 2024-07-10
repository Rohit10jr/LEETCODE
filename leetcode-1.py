'''

1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

'''

##### solutions #####

# one-hash table
class Solution(object):
    def twoSum(self, nums, target):
        num_to_index = {}
        for i, num in enumerate(nums):
            print('i', i, 'num', num)
            complement = target - num
            print('complement', complement)
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
            print('num_index', num_to_index)

obj = Solution()

print('two sum using one-hash table', obj.twoSum([2,7,11,15], 9))


# two-hash table 

def two_sum_one_hash(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        num_dict[num] = i
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict and num_dict[complement] != i:
            return [i, num_dict[complement]]
        

print('two sum using two-hash table',two_sum_one_hash([2,7,11,15], 9))


# Brute Force

def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            

print('two sum using brute-force', two_sum_brute([2,7,11,15], 9))
