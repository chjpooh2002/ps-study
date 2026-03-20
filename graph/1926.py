from collections import deque

N,M = map(int,input().split())
graph = [ list(map(int,input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]   #--> x,y 조합으로 계속 이동해 나감

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
        
            if nx <0 or nx>=N or ny<0 or ny>=M: # 범위 밖의 좌표일 때 다시 좌표 설정
                continue
            if visited[nx][ny]:                 # 이미 방문한 곳이라면 다시 좌표 설정
                continue
            if graph[nx][ny] == 0:              # 벽(0)이면 갈 수 없으니 다시 경로 설정
                continue
                
            visited[nx][ny] = True                 # 처음 방문하는 곳이면
            queue.append((nx,ny))
            size +=1
        
    return size

count = 0
max_size = []
for n in range(N):
    for m in range(M):
        if not visited[n][m] and graph[n][m] == 1:  # 아직 방문을 하지 않은 점에 대하여 bfs 생성하여 연결 요소 정함.
            count+=1
            max_size.append(bfs(n,m))
        
print(count)
print(max(max_size) if max_size else 0)