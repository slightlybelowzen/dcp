def solve(m: int, n: int, maze: list[list[str]]):
    center = (1, 1)
    max_num_points = 0
    for i, row in enumerate(maze):
        num_points = len(list(filter(lambda x: x == "#", row)))
        if num_points >= max_num_points:
            max_num_points = num_points
            center = (i + 1, len(row) // 2)
    print(center)


if __name__ == "__main__":
    k = int(input())
    while k > 0:
        m, n = [int(s) for s in input().split()]
        maze = []
        for i in range(m):
            maze.append([])
            maze[i] = [s for s in input()]
        solve(m, n, maze)
        k -= 1
