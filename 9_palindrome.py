"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""


def ispalindrome(num):
    val = str(num)
    ispal = val == val[::-1]
    print(ispal)
    return ispal


ispalindrome(121)
ispalindrome(-121)
ispalindrome(10)


def ispalindrome_int(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    n = x
    reversed = 0
    while n > 0:
        remainder = n % 10
        reversed = (reversed*10) + remainder
        n = n//10
    return x == reversed


print(ispalindrome_int(121))
print(ispalindrome_int(-121))
print(ispalindrome_int(10))
