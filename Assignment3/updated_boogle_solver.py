import re


class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = set(word.lower() for word in dictionary)
        self.prefix_set = self.build_prefix_set(dictionary)
        self.num_rows = len(self.grid)
        self.num_cols = len(self.grid[0]) if self.grid else 0
        self.solutions = set()

    def build_prefix_set(self, dictionary):
        """Build a set of all possible prefixes from the dictionary."""
        prefix_set = set()
        for word in dictionary:
            for i in range(1, len(word) + 1):
                prefix_set.add(word[:i].lower())
        return prefix_set

    def validate_grid(self, grid):
        """Validate if the grid is square and contains valid characters."""
        if not grid or len(grid) != len(grid[0]):
            return False

        regex = r'^(st|qu|[a-prt-z]+)$'
        for row in grid:
            for cell in row:
                if not re.match(regex, cell.lower()):
                    return False
        return True

    def setGrid(self, grid):
        """Set the grid and update its dimensions."""
        self.grid = grid
        self.num_rows = len(grid)
        self.num_cols = len(grid[0]) if grid else 0

    def setDictionary(self, dictionary):
        """Set the dictionary and build the prefix set."""
        self.dictionary = set(word.lower() for word in dictionary)
        self.prefix_set = self.build_prefix_set(dictionary)

    def dfs(self, row, col, current_word, visited):
        """Depth-First Search to find all valid words from a given cell."""
        if (row < 0 or col < 0 or row >= self.num_rows or
                col >= self.num_cols or visited[row][col]):
            return

        current_word += self.grid[row][col].lower()

        if current_word not in self.prefix_set:
            return

        if len(current_word) >= 3 and current_word in self.dictionary:
            self.solutions.add(current_word)

        visited[row][col] = True

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for dr, dc in directions:
            self.dfs(row + dr, col + dc, current_word, visited)

        visited[row][col] = False

    def find_solutions(self):
        """Find all valid words in the grid using DFS."""
        self.solutions.clear()
        visited = [[False] * self.num_cols for _ in range(self.num_rows)]

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.dfs(row, col, "", visited)

        return list(self.solutions)

    def getSolution(self):
        """Get all valid words found in the grid."""
        if not self.validate_grid(self.grid):
            return []
        solutions = self.find_solutions()
        return sorted([word.upper() for word in solutions])
