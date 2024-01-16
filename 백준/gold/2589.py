from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [list(input()) for _ in range(n)]

def push(x,y,s):
    q.append((x,y))
    visited[x][y] = True
    step[x][y] =s

def can_go(x,y):
    if 0<=x<n and 0<=y<m and not visited[x][y] and graph[x][y] =='L' :
        return True
    else:
        return False


def bfs():
    while q:
        x,y = q.popleft()
        dxs = [-1,1,0,0]
        dys = [0,0,-1,1]
        for dx,dy in zip(dxs,dys):
            nx = x+dx
            ny = y+dy
            if can_go(nx,ny):
                push(nx,ny,step[x][y]+1)
    return step[x][y]
                
ans =0
for j in range(m):
    for i in range(n):
        visited = [[False for _ in range(m)] for _ in range(n)]
        step = [[0 for _ in range(m)] for _ in range(n)]
        if graph[i][j] =="L":
            q = deque()
            push(i,j,0)
            ans = max(ans,bfs())
            
print(ans)