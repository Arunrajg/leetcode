"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

# Time Complexity: O(n)
# Space Complexity: O(n)


def containsDuplicate(nums: list) -> bool:
    output = False
    unique_vals = set()
    for num in nums:
        if num in unique_vals:
            output = True
            break
        else:
            unique_vals.add(num)
    return output


print(containsDuplicate([1, 2, 3, 1]))
print(containsDuplicate([1, 2, 3, 4]))
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
