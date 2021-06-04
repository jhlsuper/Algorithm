def dfs(graph, v, visited):
	# 현재 노드를 방문 처리
    vistied[v] =True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
    	if not visited[i]:
        	dfs(graph, i,visted)

graph =[[],
		[2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]]

visited = [False] * 9
def dfs(graph, v, visited):
	# 현재 노드를 방문 처리
    vistied[v] =True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
    	if not visited[i]:
        	dfs(graph, i,visted)

graph =[[],
		[2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]]

visited = [False] * 9
dfs(graph, 1, visited)
```

### BFS 구현

bfs는 너비 우선 탐색이다. 즉 가까운 노드부터 탐색하는 알고리즘이다.
BFS는 FIFO인 큐를 이용하는 것이 정석이다. 인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면 자연스럽게 먼저 들어온 것이 먼저 나가게 되어, 가까운 노드부터 탐색을 진행한다.

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리 한다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

deque 라이브러리를 사용하면 수행시간이 O(N)이다.

```
from collections import deque

#BFS 메서드 정의
def bfs(graph, start, visited):
	#큐 구현을 위해 deque라이브러리 사용
    queue = deque([start])
    #현재 노드를 방문 처리
    visited[start] = True

    #큐가 빌때 까지 반복
    while deque:
    	v= queue.popleft()
        print(v,end=' ')

        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
        	if not visited[i]:
            	queue.append(i)
                visited[i] =True

graph =[[],
		[2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]]

visited = [False] * 9

bfs(graph, 1, visited)

dfs(graph, 1, visited)