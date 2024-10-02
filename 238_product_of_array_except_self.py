"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""


def productExceptSelf(nums: list[int]) -> list[int]:
    # Time complexity: O(n)
    # Space complexity: O(1), excluding the space used for output list
    output = [1]*len(nums)
    left_side_product = 1
    for index in range(len(nums)):
        output[index] = left_side_product
        left_side_product = left_side_product * nums[index]

    right_side_product = 1
    for index in range(len(nums)-1, -1, -1):
        output[index] = output[index] * right_side_product
        right_side_product = right_side_product * nums[index]
    return output


print(productExceptSelf([1, 2, 3, 4]))
print(productExceptSelf([-1, 1, 0, -3, 3]))
