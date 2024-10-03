"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length
"""


def characterReplacement(s: str, k: int) -> int:
    # Time complexity: O(n)
    left = 0
    frequency_map = {}
    max_count = 0
    max_len = 0

    for right in range(len(s)):
        if s[right] not in frequency_map:
            frequency_map[s[right]] = 1
        else:
            frequency_map[s[right]] += 1
        max_count = max(max_count, frequency_map[s[right]])
        if right-left+1-max_count > k:
            frequency_map[s[left]] -= 1
            left += 1
        max_len = max(max_len, right-left+1)
    return max_len


print(characterReplacement(s="ABAB", k=2))
print(characterReplacement(s="AABABBA", k=1))
