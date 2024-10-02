"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""


def longestConsecutive(nums: list[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)
    if not nums:
        return 0
    nums = set(nums)
    streak = 0

    for num in nums:
        if num-1 not in nums:
            current_streak = 1
            while num+1 in nums:
                current_streak += 1
                num += 1
            streak = max(streak, current_streak)
    return streak


print(longestConsecutive([100, 4, 200, 1, 3, 2]))
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
