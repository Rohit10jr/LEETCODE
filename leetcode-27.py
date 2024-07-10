'''27. Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

'''

class Solution(object):
    def removeElement(self, nums, val):
        #  two pointers:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                # If the current element is not equal to val, append it to the list
                nums[k] = nums[i]
                k += 1
        return k

obj= Solution()
print(obj.removeElement([3,2,2,3], val = 3))


# while loop

def removeElement1(nums, val):
    i = 0

    # Iterate through the list
    while i < len(nums):
        # If the current element is equal to val, remove it
        if nums[i] == val:
            nums.pop(i)
        else:
            # Move to the next element
            i += 1
    return len(nums)


print(removeElement1([3,2,2,3], val = 3))


# list manipulation techniques

def removeElement2(nums, val):
        nums[:] = [num for num in nums if num != val]
        return len(nums)

# print(removeElement2([3,2,2,3], val = 3))


# Backward Iteration

def removeElement3(nums, val):
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == val:
            nums.pop(i)

    return len(nums)

print(removeElement3([3,2,2,3], val = 3))



# lowest time
# Two Pointers Initialization

def removeElement4(nums, val):
        num = len(nums)
        if num == 0:
            return 0
        i = 0
        j = num - 1
        while i < j:
            if nums[i] == val:
                if nums[j] != val:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
                else:
                    j -= 1
            else:
                if nums[j] == val:
                    i += 1
                    j -= 1
                else:
                    i += 1
        return i if nums[i] == val else i + 1

print(removeElement4([3,2,2,3], val = 3))


# mine

def removeElement5(nums, val):
        nums_copy =  list(nums)
        nums_copy = nums.copy()
        for num in nums_copy:
            if num == val:
                nums.remove(num)
        k = len(nums)
        return k

print(removeElement5([3,2,2,3], val = 3))

