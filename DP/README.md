> 알고리즘을 해결해가며 느낀점 + 개인적인 생각

---
## Dynamic Programming

- 특정 범위까지의 값을 구하기 위해 '이전 범위의 값을 활용'하여 효율적으로 값을 얻는 기법
- 이전 범위의 값을 저장(Memorization)하여, 똑같은 문제가 발생했을 때 이를 참조하여 해결함.

~~점화식을 만들어서 적용한다는 느낌으로 접근해 볼 예정~~

### #1904

``` python
dp = [0]*(n+1)

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = ...
```

<details>
<summary> ... </summary>

    첫 DP 문제.
    점화식을 만들어서 푼다는 것 까지는 이해했으나, 아직 문제 풀이에 있어서는 감을 잡지 못한 상태 ㅠ
</details>