"""
Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""


def groupAnagrams(strs: list) -> list:
    """
    Time Complexity: O(n * k log k), where n is the number of strings and
    k is the maximum length of a string. This is because we sort each string, which takes O(k log k) time,
    and we do this for all n strings.

    Space Complexity
    The space complexity is O(n * k), where n is the number of strings and k is the maximum length of a string.
    This is because we store each string in the dictionary.
    """
    grouped_anagram = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word not in grouped_anagram:
            grouped_anagram[sorted_word] = [word]
        else:
            grouped_anagram[sorted_word].append(word)
    return list(grouped_anagram.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
