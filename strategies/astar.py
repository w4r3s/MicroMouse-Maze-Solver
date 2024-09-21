# strategies/astar.py

import heapq
import math
from collections import deque

def solve_with_animation(maze, start, end, step, **params):
    width = len(maze[0])
    height = len(maze)
    visited = set()
    queue = deque()
    queue.append((start, [start]))
    visited.add(start)

    while queue:
        current_pos, path = queue.popleft()
        if current_pos == end:
            yield path, visited  # 找到路径
            return

        x, y = current_pos
        neighbors = get_neighbors(x, y, maze, step)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
        yield None, visited  # 继续动画

    yield None, visited  # 未找到路径
    
def solve_with_animation(maze, start, end, step, **params):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    visited = set()
    visited.add(start)

    while open_set:
        current_f, current = heapq.heappop(open_set)
        if current == end:
            path = reconstruct_path(came_from, current)
            yield path, visited
            return

        x, y = current
        neighbors = get_neighbors(x, y, maze, step)
        for neighbor in neighbors:
            tentative_g_score = g_score[current] + 1  # 假设每个移动的代价为1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, end, **params)
                heapq.heappush(open_set, (f_score, neighbor))
                visited.add(neighbor)
        yield None, visited

def solve_with_waypoints(maze, start, waypoints, end, step, **params):
    full_path = []
    current_start = start
    for waypoint in waypoints + [end]:
        path = astar_search(maze, current_start, waypoint, step, **params)
        if path is None:
            return None
        if full_path and path[0] == full_path[-1]:
            full_path.extend(path[1:])
        else:
            full_path.extend(path)
        current_start = waypoint
    return full_path

def astar_search(maze, start, end, step, **params):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    visited = set()
    visited.add(start)

    while open_set:
        current_f, current = heapq.heappop(open_set)
        if current == end:
            return reconstruct_path(came_from, current)

        x, y = current
        neighbors = get_neighbors(x, y, maze, step)
        for neighbor in neighbors:
            tentative_g_score = g_score[current] + 1  # 假设每个移动的代价为1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, end, **params)
                heapq.heappush(open_set, (f_score, neighbor))
                visited.add(neighbor)
    return None

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def get_neighbors(x, y, maze, step):
    moves = [(-step, 0), (step, 0), (0, -step), (0, step)]  # 上下左右
    result = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze):
            if maze[ny][nx] == 0:
                result.append((nx, ny))
    return result

def heuristic(a, b, **params):
    method = params.get('heuristic', '曼哈顿距离')
    x1, y1 = a
    x2, y2 = b
    if method == '曼哈顿距离':
        return abs(x1 - x2) + abs(y1 - y2)
    elif method == '欧几里得距离':
        return math.hypot(x1 - x2, y1 - y2)
    else:
        return 0  # 默认返回0
