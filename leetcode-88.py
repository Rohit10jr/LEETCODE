'''

88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

'''

# Using Extra List
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        num = []
        for i in range(len(nums1)):
            if nums1[i] != 0:
                # print(num1[i])
                num.append(nums1[i])
        nums1=num
        # nums1 +=nums2
        nums1.extend(nums2)
        nums1.sort()
        print("solution", nums1)

obj= Solution()
obj.merge([1,2,3,0,0,0], 3, [2,5,6], 3)


#  In-Place Merge with Sorting

def merge1(nums1, m, nums2, n):
    # nums1[:] = sorted(nums1[:m] + nums2)
    #  nums1[:] = nums1[:m]  
    nums1[m:] = nums2
    nums1.sort()
    print("merge 1", nums1)

merge1([1,2,3,0,0,0], 3, [2,5,6], 3)


#  Merge and Sort 

def merge2(nums1, m, nums2, n): 

    for j in range(n):
        nums1[m + j] = nums2[j]
    nums1.sort()
    print("merge 2", nums1)

merge2([1,2,3,0,0,0], 3, [2,5,6], 3)


# Two-Pointer Merge 

def merge3(nums1, m, nums2, n):
    nums1[:] = nums1[:m]  # Remove extra zeros at the end of nums1
    i, j = 0, 0
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            i += 1
        else:
            nums1.insert(i, nums2[j])
            j += 1
            m += 1
    if j < n:
        nums1.extend(nums2[j:])

    print("merge 3",nums1)

merge3([1,2,3,0,0,0], 3, [2,5,6], 3)

