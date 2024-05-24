#  https://www.acmicpc.net/problem/21921
#
# Q:
# 찬솔이는 블로그를 시작한 지 벌써 N일이 지났다.
# 찬솔이는 X일 동안 가장 많이 들어온 방문자 수와 그 기간들을 알고 싶다.
#
# 찬솔이를 대신해서 X일 동안 가장 많이 들어온 방문자 수와 기간이 몇 개 있는지 구해주자.
#
# Input:
# 첫째 줄에 블로그를 시작하고 지난 일수 N와 X가 공백으로 구분되어 주어진다.
# 둘째 줄에는 블로그 시작 1일차부터 N일차까지 하루 방문자 수가 공백으로 구분되어 주어진다.
#
# Output:
# 첫째 줄에 X일 동안 가장 많이 들어온 방문자 수를 출력한다. 만약 최대 방문자 수가 0명이라면 SAD를 출력한다.
# 만약 최대 방문자 수가 0명이 아닌 경우 둘째 줄에 기간이 몇 개 있는지 출력한다.
#
# Example:
# in:
# 5 2
# 1 4 2 5 1
#
# out:
# 7
# 1

import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visitor = list(map(int, input().split()))

if max(visitor) == 0:
    print('SAD')
else:
    answer = sum(visitor[:x])
    tmp = answer
    max_cnt = 1

    for i in range(n - x):
        tmp = tmp - visitor[i] + visitor[i + x]

        if answer == tmp:
            max_cnt += 1
        elif answer < tmp:
            max_cnt = 1
            answer = tmp

    print(answer)
    print(max_cnt)