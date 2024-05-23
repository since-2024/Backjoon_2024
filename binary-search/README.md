> 알고리즘을 해결해가며 느낀점 + 개인적인 생각

---
### #1920

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
<details>
<summary> ... </summary>

    binary search 첫 해결 문제.
    min(lt) 과 max(rt) 값을 설정하고 중간 값(mid)을 세워 검증하고
    기준보다 작다면 lt와 mid 사이에서 다시 검증,
    기준보다 크다면 mid와 rt 사이에서 다시 검증.


</details>

---
### #1654
<details>
<summary> ... </summary>

    lan선 이라는 단어에 꽂혀서 자꾸 다른 생각을 하게 됨
    대학생 시절 이진 탐색을 배웠을 즈음이 떠올랐다.
    lt 값과 rt 값이 교차하는 순간 탐색이 종료 된다는 것.
</details>

---
### #2805
<details>
<summary> ... </summary>

    #1654와 같은 유형.
    4764 ms로 통과. 비슷한 시간대에 384 ms 걸린 풀이도 보여서 다시 풀이 예정
</details>

---
### #1072
<details>
<summary> ... </summary>

    answer와 그를 구하는데 비교되는 승률의 혼동으로 조금 헤맸다.
</details>

---
### #1072

``` python
    multiple_lines_list = [int(input()) for _ in range(n)]
```
<details>
<summary> ... </summary>

    집에서 빨리 쉬겠다며 퇴근 버스 안에서 풀었다.
    그러다보니 전 문제에 풀었던 방식은 생각이 잘 났지만
    list 를 만드는 컴프리헨션이 생각나지 않았기에 상기시킬겸 기록해둔다.
</details>


---
### #1072
<details>
<summary> ... </summary>

    list의 index 값과 index에 해당되는 값에 혼동이 생겨 오래 걸린 문제.
    예시를 들어보며 풀다보니 헷갈리는 점이 풀리면서 문제도 풀렸다.
</details>