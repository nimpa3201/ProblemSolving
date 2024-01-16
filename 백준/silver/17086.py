from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
ans = -1
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
step = [[0 for _ in range(m)] for _ in range(n)]
q = deque()

def push(x, y, s):
    q.append((x, y))
    visited[x][y] = 1
    step[x][y] = s

def can_go(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs():
    while q:
        x, y = q.popleft()
        dxs = [0, 0, -1, 1, -1, -1, 1, 1]
        dys = [1, -1, 0, 0, -1, 1, 1, -1]
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 0:
                push(nx, ny, step[x][y] + 1)

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            push(i, j, 0)
bfs()

for i in range(n):
    for j in range(m):
        ans = max(ans, step[i][j])
print(ans)
