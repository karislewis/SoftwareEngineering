import re

class Boggle:
    def __init__(self, grid, dictionary):
        
        self.grid = grid 
        #making sure no duplicates are added and converting to upper case
        self.dictionary = set(word.lower() for word in dictionary)  
        #getting the length (rows) of the grid
        self.num_rows = len(self.grid)
        #getting the length (columns) of the grid
        self.num_cols = len(self.grid[0])
        #creating an empty set that will be used to add solutions to
        self.solutions = set()

    def validate_grid(self, grid):
        #checking to see if the length rows and columns are the same (making sure the grid is a square) 
        max_row_length = len(grid)
        max_col_length = len(grid[0])

        if max_row_length != max_col_length:
            #if its not a square return false
           
            return False  
        #want to make sure no numbers are in the grid and St and Qu- Q and S can not be in the grid
        regex = r'^(st|qu|[a-prt-z]+)$'

        
        for row in grid:
            for cell in row:
                #checking the regex (St and Qu and only letters)
                if not re.match(regex, cell.lower()):  # Case-insensitive check
               
                    return False  
      #if it returns true then the grid is valid 
        return True

    def setGrid(self, grid):
      #establishing the grid 
        self.grid = grid
        self.num_rows = len(grid)
        self.num_cols = len(grid[0]) if grid else 0

    def setDictionary(self, dictionary):
      #making the dictionary items all capitals (makes sure its not case sensitive)
        self.dictionary = set(word.lower() for word in dictionary)  # Case-insensitive

    def dfs(self, r, c, current_word, visited):

        #base case - making sure the row & columns arent out of bounds, checks if the index has already been visited 
        if r < 0 or c < 0 or r >= self.num_rows or c >= self.num_cols or visited[r][c]:
            return

        #appending the current character to the word 
        current_word += self.grid[r][c].lower()

        #checking the length of the word and checking to see if it is in the dictionary
        if len(current_word) > 1 and current_word in self.dictionary:
            #if it is I can add to the list of solutions
            self.solutions.add(current_word)
        #marking the current cell as visited
        visited[r][c] = True

        # being used to get the directions (or neighboring cells)
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # going through the neighbors (dr- row, dc-column)
        for dr, dc in directions:
          #this is what will be forming the words
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

        #returning the solutions 
        return list(self.solutions)

    def getSolution(self):
        # Check if the grid is valid
        if not self.validate_grid(self.grid):
            return []
        # If grid is valid, find and return solutions
        #converting the list of words to upper case 
        solutions = self.find_solutions()
        upper_solutions = [word.upper() for word in solutions]
     

        #return that upper case list 
        return upper_solutions

def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    
    mygame = Boggle(grid, dictionary)
    solutions = mygame.getSolution()

  
    print(sorted(solutions))

if __name__ == "__main__":
    main()
