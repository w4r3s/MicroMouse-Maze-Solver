# strategies/dfs.py
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
    width = len(maze[0])
    height = len(maze)
    visited = set()
    stack = []
    stack.append((start, [start]))
    visited.add(start)

    while stack:
        current_pos, path = stack.pop()
        if current_pos == end:
            yield path, visited
            return

        x, y = current_pos
        neighbors = get_neighbors(x, y, maze, step)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))
        yield None, visited

def solve_with_waypoints(maze, start, waypoints, end, step, **params):
    full_path = []
    current_start = start
    for waypoint in waypoints + [end]:
        path = dfs_search(maze, current_start, waypoint, step)
        if path is None:
            return None
        if full_path and path[0] == full_path[-1]:
            full_path.extend(path[1:])
        else:
            full_path.extend(path)
        current_start = waypoint
    return full_path

def dfs_search(maze, start, end, step):
    width = len(maze[0])
    height = len(maze)
    visited = set()
    stack = []
    stack.append((start, [start]))
    visited.add(start)

    while stack:
        current_pos, path = stack.pop()
        if current_pos == end:
            return path

        x, y = current_pos
        neighbors = get_neighbors(x, y, maze, step)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))
    return None

def get_neighbors(x, y, maze, step):
    moves = [(-step, 0), (step, 0), (0, -step), (0, step)]  # 上下左右
    result = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze):
            if maze[ny][nx] == 0:
                result.append((nx, ny))
    return result
