#
#
# Q:
# 김형택은 지금 몰래 Spider Solitaire(스파이더 카드놀이)를 하고 있다. 형택이는 이 게임을 이길 때도 있었지만, 질 때도 있었다.
# 형택이는 잠시 코딩을 하는 사이에 자신의 게임 실력이 눈에 띄게 향상된 것을 알았다.
#
# 이제 형택이는 앞으로의 모든 게임에서 지지 않는다.
# 하지만, 형택이는 게임 기록을 삭제 할 수 없기 때문에, 자신의 못하던 예전 기록이 현재 자신의 엄청난 실력을 증명하지 못한다고 생각했다.
#
# 게임 기록은 다음과 같이 생겼다.
#
# * 게임 횟수 : X
# * 이긴 게임 : Y (Z%)
# Z는 형택이의 승률이고, 소수점은 버린다. 예를 들어, X=53, Y=47이라면, Z=88이다.
#
# X와 Y가 주어졌을 때, 형택이가 게임을 최소 몇 번 더 해야 Z가 변하는지 구하는 프로그램을 작성하시오.
#
# Input:
# 각 줄에 정수 X와 Y가 주어진다.
#
# Output:
# 첫째 줄에 형택이가 게임을 최소 몇 판 더 해야하는지 출력한다. 만약 Z가 절대 변하지 않는다면 -1을 출력한다.
#
# Example:
# in:
# 10 8
#
# out:
# 1

x, y = map(int, input().split())
rate = (y * 100) // x

if rate >= 99:
    print(-1)
else:
    lt, rt = 1, x
    answer = 0

    while lt <= rt:
        mid = (lt + rt) // 2

        if (y + mid)*100 // (x + mid) <= rate:
            lt = mid + 1
        else:
            answer = mid
            rt = mid - 1

    print(answer)