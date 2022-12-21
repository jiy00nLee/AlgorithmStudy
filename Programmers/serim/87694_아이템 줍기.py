from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    graph = [[-1] * 102 for _ in range(102)]
    visited = [[0] * 102 for _ in range(102)]
    queue = deque()
    queue.append([characterX * 2, characterY * 2])


    for r in rectangle:
        t_x1, t_y1, t_x2, t_y2 = r
        x1, y1, x2, y2 = t_x1 * 2, t_y1 * 2, t_x2 * 2, t_y2 * 2
        for i in range(x1 + 1, x2):
            for j in range(y1 + 1, y2):
                graph[i][j] = 0
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if graph[i][j] != 0:
                    graph[i][j] = 1

    while queue:
        x, y = queue.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

    return answer