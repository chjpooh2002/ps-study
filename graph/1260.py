from collections import deque        # bfs에서 사용

N,M,V= map(int,input().split())
graph = [[] for _ in range(N+1)]     # 기본적인 그래프 만드는 방법    
visited_1 = [False]*(N+1)            # 특정 노드를 방문했는지 판별
visited_2 = [False]*(N+1)

for _ in range(M):                   # 보통 그래프는 양방향 그래프임
    a,b = map(int,input().split())
    graph[a].append(b)               # 정점 a에 인접한 노드 b
    graph[b].append(a)               # 정점 b에 인접한 노드 a

for i in range(N+1):
    graph[i].sort()                  # 정점 작은 것부터 방문해야 되므로 각 인접 노드를 담은 리스트 정렬

def dfs(x):      # 정점 x에서 깊이 우선 탐색 시작
    visited_1[x] = True
    print(x,end = ' ')    # 방문한 노드 출력
    for nx in graph[x]:   # graph[x]가 의미하는 것이 바로 정점 x에 인접한 정점 리스트 
        if not visited_1[nx]:  # x에 인접한 정점 중에 방문하지 않은 정점 nx에 대해 다시 dfs
            dfs(nx)
def bfs(x):
    queue = deque([x])
    visited_2[x] = True
    print(x, end = ' ')
    
    while queue:        #queue가 빌 때까지 수행
        now = queue.popleft() # bfs
        
        for next_node in graph[now]:
            if not visited_2[next_node]:
                visited_2[next_node] = True
                print(next_node, end = ' ')
                queue.append(next_node)
    
            
dfs(V)
print()
bfs(V)