import re
class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        #making sure no duplicates are added and converting to lower case
        self.dictionary = set(word.lower() for word in dictionary)
        self.prefix_set = self.build_prefix_set(dictionary)
        #getting the length (rows) of the grid
        self.num_rows = len(self.grid)
         #getting the length (columns) of the grid
        self.num_cols = len(self.grid[0]) if self.grid else 0
         #creating an empty set that will be used to add solutions to
        self.solutions = set()

    def build_prefix_set(self, dictionary):
        prefix_set = set()
        for word in dictionary:
            for i in range(1, len(word) + 1):
                prefix_set.add(word[:i].lower())
        return prefix_set

    def validate_grid(self, grid):
        if not grid or len(grid) != len(grid[0]):
            return False
        
        #want to make sure no numbers are in the grid and St and Qu- Q and S can not be in the grid
        regex = r'^(st|qu|[a-prt-z]+)$'
        for row in grid:
            for cell in row:
                 #checking the regex (St and Qu and only letters)
                if not re.match(regex, cell.lower()):
                    return False
        #if it returns true then the grid is valid 
        return True

    def setGrid(self, grid):
        #establishing the grid 
        self.grid = grid
        self.num_rows = len(grid)
        self.num_cols = len(grid[0]) if grid else 0

    def setDictionary(self, dictionary):
         #making the dictionary items all lower (makes sure its not case sensitive)
        self.dictionary = set(word.lower() for word in dictionary)
        self.prefix_set = self.build_prefix_set(dictionary)

    def dfs(self, r, c, current_word, visited):
        #base case - making sure the row & columns arent out of bounds, checks if the index has already been visited
        if r < 0 or c < 0 or r >= self.num_rows or c >= self.num_cols or visited[r][c]:
            return
        #appending the current character to the word 
        current_word += self.grid[r][c].lower()

        # Early termination if current word isn't a prefix of any word in the dictionary
        if current_word not in self.prefix_set:
            return

        #checking the length of the word and checking to see if it is in the dictionary
        if len(current_word) >= 3 and current_word in self.dictionary:
            self.solutions.add(current_word)

        visited[r][c] = True

        #being used to get the directions (or neighboring cells)
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        for dr, dc in directions:
            self.dfs(r + dr, c + dc, current_word, visited)
        # backtracking- making the cell avaliable
        visited[r][c] = False 

    def find_solutions(self):
        self.solutions.clear()
        #created visited matrix (same size of the grid)
        visited = [[False] * self.num_cols for _ in range(self.num_rows)]

         #for each cell searching with DFS
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                self.dfs(r, c, "", visited)

        return list(self.solutions)

    def getSolution(self):
         # Check if the grid is valid
        if not self.validate_grid(self.grid):
            return []
        solutions = self.find_solutions()
        return sorted([word.upper() for word in solutions])

