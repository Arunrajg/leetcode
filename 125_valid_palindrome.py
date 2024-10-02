"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


def isPalindrome(s: str) -> bool:
    # Time complexity: O(n)
    # Two pointer algorithm
    start = 0
    end = len(s)-1
    while start < end:
        while start < end and not s[start].isalnum():
            start += 1
        while start < end and not s[end].isalnum():
            end -= 1
        if s[start].lower() != s[end].lower():
            return False
        start += 1
        end -= 1
    return True


def pythonicWay(s: str) -> bool:
    # Time complexity: O(n)
    char_list = [char.lower() for char in s if char.isalnum()]
    return char_list == char_list[::-1]


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))
print(pythonicWay("A man, a plan, a canal: Panama"))
print(pythonicWay("race a car"))
print(pythonicWay(" "))
