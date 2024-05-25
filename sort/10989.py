# https://www.acmicpc.net/problem/10989
#
# Q:
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
#
# Input:
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다.
# 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
#
# Output:
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
#
# Example:
# in:
# 10
# 5
# 2
# 3
# 1
# 4
# 2
# 3
# 5
# 1
# 7
#
# out:
# 1
# 1
# 2
# 2
# 3
# 3
# 4
# 5
# 5
# 7

import sys
input = sys.stdin.readline

n = int(input())
l = [0] * (10000 + 1)

# 계수 정렬
for _ in range(n):
    l[int(input())] += 1

for i in range(len(l)):
    if l[i] != 0:
        for _ in range(l[i]):
            print(i)
