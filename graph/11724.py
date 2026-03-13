import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    visited[x] = True

    for next_node in graph[x]:
        if not visited[next_node]:
            dfs(next_node)
count = 0
for i in range(1,N+1):
    if not visited[i]:
        count +=1
        dfs(i)

print(count)