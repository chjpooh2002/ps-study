#백준 2606(실버3)

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

def dfs(x):
    visited[x] = True
    global count
    count+=1
    for next_node in graph[x]:
        if not visited[next_node]:
            dfs(next_node)
            
dfs(1)
print(count-1)