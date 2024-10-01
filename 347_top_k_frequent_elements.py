"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from collections import Counter


def topKFrequent(nums: list[int], k: int) -> list[int]:
    # Time complexity O(n log k)
    # Space Complexity O(n)
    frequency = Counter(nums)
    top_k = frequency.most_common(k)
    return [i[0] for i in top_k]


def another_solution(nums: list, k) -> list:
    # Time complexity O(n)
    # Space Complexity O(n)
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    max_freq = max(frequency.values())
    buckets = [[] for _ in range(max_freq + 1)]
    for num, freq in frequency.items():
        buckets[freq].append(num)
    result = []
    for i in range(max_freq, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(topKFrequent([1], 1))
print(another_solution([1, 1, 1, 2, 2, 3], 2))
print(another_solution([1], 1))
