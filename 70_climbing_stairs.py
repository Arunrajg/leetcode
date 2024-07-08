"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

1111
112
121
211
22

11111
1112
1121
1211
2111
221
212
122

Constraints:

1 <= n <= 45
"""


def climbing_stairs(n: int) -> int:
    a = 1
    b = 1
    if n <= 2:
        return n
    else:
        for _ in range(2, n+1):
            c = a+b
            a = b
            b = c
        return c


print(climbing_stairs(2))
print(climbing_stairs(3))
print(climbing_stairs(4))
print(climbing_stairs(6))


"""
111111
11112
11121
11211
12111
21111
2112
2121
2211
222
"""
