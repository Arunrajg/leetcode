"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?"""


from collections import Counter


def valid_anagram(s: str, t: str) -> bool:
    # Time Complexity: O(nlog n)
    # Space Complexity: O(n)
    _s = sorted(s)
    _t = sorted(t)
    return (_s == _t)


# More pythonic way

def efficient_solution(s: str, t: str) -> bool:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    return Counter(s) == Counter(t)


print(valid_anagram("anagram", "nagaram"))
print(valid_anagram("rat", "car"))
print(efficient_solution("anagram", "nagaram"))
print(efficient_solution("rat", "car"))
