import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
count_list = [0 for _ in range(N+1)]  # 연결된 정점 개수를 세는 리스트
visited = [0]*(N+1) 
mark = 0

for _ in range(M):
    a,b = map(int,input().split())
    graph[b].append(a)             # a b 형태이면 b 해킹하면 a 해킹 가능

for i in range(1,N+1):
    count = 0
    mark += 1
    stack = [i]
    visited[i] = mark
    
    while stack:
        now = stack.pop()
        for next_node in graph[now]:
            if visited[next_node]!=mark:   # 방문하지 않은 곳
                visited[next_node] = mark
                stack.append(next_node)
                count+=1
    count_list[i] = count
        
max_count = max(count_list)
for i in range(1,N+1):
    if(count_list[i]==max_count):
        print(i, end = " ")



