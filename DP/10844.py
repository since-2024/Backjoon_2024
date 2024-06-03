# https://www.acmicpc.net/problem/10844
#
# Q:
# 45656이란 수를 보자.
# 이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.
#
# N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자.
# 0으로 시작하는 수는 계단수가 아니다.
#
# Input:
# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.
#
# Output:
# 첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
#
# Example:
# in:
# 1
#
# out:
# 9

n = int(input())

MOD = 1000000000

dp = [[0] * 10 for _ in range(n+1)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:  # j == (2 ~ 8)
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % MOD)
