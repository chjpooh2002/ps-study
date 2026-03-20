from collections import deque

T = int(input())      # 연결 요소를 구하는 문제

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    size = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx >=N or ny < 0 or ny>=M:
                continue
            if graph[nx][ny]==0:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            queue.append((nx,ny))
            size += 1
    return size
    
for _ in range(T):
    N,M,K = map(int,input().split())
    graph = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    count = 0
    for i in range(K):
        x,y = map(int,input().split())
        graph[x][y] = 1
    for j in range(N):
        for k in range(M):
            if not visited[j][k] and graph[j][k] == 1:
                bfs(j,k)
                count+=1
    print(count)
