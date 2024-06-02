# https://www.acmicpc.net/problem/12865
#
# Q:
# 준서가 여행에 필요하다고 생각하는 N개의 물건이 있다.
# 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다.
# 아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다.
# 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.
#
# Input:
# 첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다.
# 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.
#
# 입력으로 주어지는 모든 수는 정수이다.
#
# Output:
# 한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.
#
# Example:
# in:
# 4 7
# 6 13
# 4 8
# 3 6
# 5 12
#
# out:
# 14

# 틀린 풀이 방법
if 0:
    bag.sort()

    for i in range(1, k + 1):
        for w, v in bag:
            if i < w:
                break
            else:
                dp[i] = max(dp[i - 1], dp[i], dp[i - w] + v)

    print(dp[k])

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        # [ 현재 최대 무게j ]가 [ 해당 물건 무게 ]보다 큰 경우
        if j >= bag[i-1][0]:
            # [ 표의 윗 셀의 값 ]과 [현재 물건의 V + 이전 물건의 V값의 최댓값]을 DP[i][j]에 저장
            dp[i][j] = max(bag[i-1][1] + dp[i-1][j - bag[i-1][0]], dp[i-1][j])

        # [ 현재 최대 무게j ]가 [ 해당 물건 무게 ]보다 작은 경우 (현재 물건을 담을 수 없는 경우)
        else:
            # [ 표의 윗 셀의 값 ]을 그대로 가져와 저장
            dp[i][j] = dp[i-1][j]

print(dp[n][k])
