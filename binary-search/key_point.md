### #1920
    binary search 첫 해결 문제.
    min(lt) 과 max(rt) 값을 설정하고 중간 값(mid)을 세워 검증하고
    기준보다 작다면 lt와 mid 사이에서 다시 검증,
    기준보다 크다면 mid와 rt 사이에서 다시 검증.

- 해당 문제는 set을 사용할 경우 이진탐색보다 빠르게 답을 찾을 수 있다고 한다.
``` python
# 입력
N = int(input())
A = set(map(int, input().split()))	# 탐색 시간을 줄이기 위해 set으로 받음
M = int(input())
arr = list(map(int, input().split()))

for num in arr:				# arr의 각 원소별로 탐색
    print(1) if num in A else print(0)	# num이 A 안에 있으면 1, 없으면 0 출력
```


### #1654
    lan선 이라는 단어에 꽂혀서 자꾸 다른 생각을 하게 됨
    대학생 시절 이진 탐색을 배웠을 즈음이 떠올랐다.
    lt 값과 rt 값이 교차하는 순간 탐색이 종료 된다는 것.