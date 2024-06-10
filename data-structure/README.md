> 알고리즘을 해결해가며 느낀점 + 개인적인 생각

---
## Data Structure (자료 구조)

### Priority Queue (우선순위 큐)
> - 우선순위가 높은 데이터가 먼저 나가는 형태
> - 힙(Heap)을 이용하여 구현


---

### #1655
#### 우선순위 큐 (Priority Queue)

``` python
import heapq

que = []

# 넣거나 뺄 때 마다 작은 값이 나오도록 정렬된다고 생각하면 된다.
# 따라서 큰 값을 우선 배출하고 싶다면 (-)를 붙여서 사용하고, 반환할 때 (-)를 붙여서 내보내야 한다.
heapq.heappush(que, int(input()))

# 작은 값이 반환된다. ( heapq.heappop(que) == que[0] )
min_value = heapq.heappop(que)
```

<details>
<summary> ... </summary>

    첫 우선순위 큐 문제.
    처음에는 큐에 첫 값을 넣고 해당 값보다 작으면 왼쪽에, 크면 오른쪽에 삽입을 하려고 했었지만,
    구현하기 직전에야 잘못된 것을 깨닫고 다른 방법을 찾기 위해 검색하는 과정을 거쳤다.
    
    정렬되는 방식을 이해하진 못했으나, 우선순위 큐 문제를 풀기위해 어떻게 써야할지는 터득한 것 같다.
</details>
