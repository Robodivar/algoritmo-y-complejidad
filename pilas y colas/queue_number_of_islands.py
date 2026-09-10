from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        filas = len(grid)
        columnas = len(grid[0])
        cantidad = 0
        direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(filas):
            for j in range(columnas):
                if grid[i][j] == "1":
                    cantidad += 1
                    cola = deque([(i, j)])
                    grid[i][j] = "0"

                    while cola:
                        x, y = cola.popleft()

                        for dx, dy in direcciones:
                            nx, ny = x + dx, y + dy

                            if (0 <= nx < filas and
                                0 <= ny < columnas and
                                grid[nx][ny] == "1"):
                                grid[nx][ny] = "0"
                                cola.append((nx, ny))

        return cantidad
