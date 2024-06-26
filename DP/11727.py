#
#
# Q:
# 2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
#
# 아래 그림은 2×17 직사각형을 채운 한가지 예이다.
#
#
# ┌───┬─┬───┬───┬───┬───┬───┬───┬─┬─┐
# ├───┤ │   │   │   ├───┼───┤   │ │ │
# └───┴─┴───┴───┴───┴───┴───┴───┴─┴─┘
#
# Input:
# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
#
# Output:
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
#
# Example:
# in:
# 2
#
# out:
# 3

Recurrence = '''
 dp  total
 0     1
 1     1
 2     3   -> 1*2   +1
 3     5   -> 1*2   +3
 4     11  -> 3*2   +5
 5     21  -> 5*2   +11
 6     xx  -> 11*2  +21  -> 43
 ...
'''

n = int(input())

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-2] * 2 + dp[i-1]

print(dp[n] % 10007)