# https://www.acmicpc.net/problem/2428
#
# Q:
# 대회의 참석자는 총 N명이고 각각 솔루션 파일 1개를 제출했다.
# 이 솔루션 파일을 F1, F2, ..., Fn이라고 한다.
#
# 채점 결과를 발표하기 전에, 남의 것을 배낀 사람이 있는지 찾아내려고 한다.
# 이 대회의 주최측은 두 파일을 비교해서 너무 비슷한지 아닌지 판별하는 프로그램이 있다.
#
# 하지만, 제출한 파일의 개수가 너무 많아서, 파일 크기가 너무 다른 경우에는 그러한 쌍을 검사하지 않고 넘어가기로 했다.
#
# 좀더 정확하게 하기 위해서, 대회의 심판들은 두 파일이 있을 때,
# 작은 파일의 크기가 큰 파일 크기의 90%보다도 작을 때는, 이러한 쌍은 검사하지 않고 넘어가기로 했다.
# 따라서, (Fi, Fj) 쌍을 검사해야 하는데, 이때, i≠j이고, size(Fi) ≤ size(Fj)이면서, size(Fi) ≥ 0.9 × size(Fj)인 쌍만 검사하려고 한다.
#
# 몇 개의 쌍을 검사해야 하는 지 구하는 프로그램을 작성하시오.
#
# Input:
# 첫째 줄에 제출한 솔루션의 개수 N이 주어진다.
# 둘째 줄에는 각 솔루션 파일의 크기 size(F1), size(F2), ..., size(FN)이 주어진다. (1 ≤ N ≤ 100,000, 1 ≤ size(Fi) ≤ 100,000,000)
# 솔루션 파일의 크기는 정수이다.
#
#
# Output:
# 첫째 줄에 검사해야 하는 파일의 개수를 출력한다.
#
# Example:
# in:
# 5
# 1 1 1 1 1
#
# out:
# 10

import sys
input = sys.stdin.readline

n = int(input())
files = list(map(int, input().split()))
files.sort()

answer = 0

for i in range(n):
    lt, rt = i, n-1
    f_size = files[i] * 10 / 9

    while lt <= rt:
        mid = (lt + rt) // 2

        if f_size >= files[mid]:
            lt = mid + 1
        else:
            rt = mid - 1

    answer += rt - i

print(answer)
