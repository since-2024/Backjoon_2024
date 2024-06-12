> 알고리즘을 해결해가며 느낀점 + 개인적인 생각

---
## 	Breadth-first Search (BFS, 너비 우선 탐색)

> - 시작 정점을 방문한 후 시작 점점에 인접한 모든 정점들을 우선 방문,  
>   더 이상 방문하지 않은 정점이 없을 때까지 방문하지 않은 모든 정점들에 대해서도 너비 우선 탐색을 적용
>
> - 큐(Queue)을 이용하여 구현

## 	Depth-first Search (DFS, 깊이 우선 탐색)

> - 시작 정점을 방문한 후 시작 점점에 인접한 하나의 정점을 우선 방문,  
>   인접한 정점이 있다면 해당 정점에 방문하고 인접한 정점이 없을 때까지 계속해서 방문,  
>   더 이상 인접하지 않은 정점이 없다면 방문하지 않은 정점까지 거슬러 올라가 같은 방식으로 깊이 우선 탐색을 적용
>
> - 스택(Stack)을 이용하여 구현

---

### #1260

- BFS
``` python
import heapq

que = []

# 넣거나 뺄 때 마다 작은 값이 나오도록 정렬된다고 생각하면 된다.
# 따라서 큰 값을 우선 배출하고 싶다면 (-)를 붙여서 사용하고, 반환할 때 (-)를 붙여서 내보내야 한다.
heapq.heappush(que, int(input()))

# 작은 값이 반환된다. ( heapq.heappop(que) == que[0] )
min_value = heapq.heappop(que)
```

- DFS
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

### #11725

``` python
# 메모리 초과나는 방법:
graph_fail = [[False] * (n+1) for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph_1[a][b] = True
    graph_1[b][a] = True


# 이를 해결하기 위한 방법:
graph_succ = [[] for _ in range(n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph_2[a].append(b)
    graph_2[b].append(a)
```

<details>
<summary> ... </summary>

    메모리 초과를 맞은 문제.
    dp 방식을 살려서 해보려고 했으나, 100,000^2 은 생각보다 큰 수였고,,,
    연결이 되어있는 것만 잘 적용해주면 되는 풀이법을 배워왔다.

[참고한 링크](https://d-cron.tistory.com/22)
</details>