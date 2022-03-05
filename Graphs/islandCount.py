'''
-------------------------------------------
island count
------------------------------------------
Write a function, island_count, that takes in a grid containing Ws and Ls.
W represents water and L represents land. The function should return the 
number of islands on the grid. An island is a vertically or horizontally
connected region of land.
'''

# def island_count(grid, visited=set()):
#     count = 0
#     for row in range(len(grid)):
#         for column in range(len(grid[0])):
#             source = (row, column)
#             if source in visited:
#                 continue
#             exploreGrid(grid, row, column, visited)
#             count += 1
#             print(count)
#     return count
def island_count(grid):
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited) == True:
                count += 1
    return count





# # Dfs
# def exploreGrid(grid, row, column, visited=set()):
#     # node not in bounds
#     row_inbounds = 0 <= row < len(grid)
#     col_inbounds = 0 <= column < len(grid[0])
#     if not row_inbounds or not col_inbounds:
#         return 
#     # Ignore water, we want to explore land only
#     if grid[row][column] == 'W':
#         return 
#     # node not in visited
#     source = (row, column)
#     if source not in visited:
#         visited.add(source)
#         exploreGrid(grid, row-1, column, visited)
#         exploreGrid(grid, row+1, column, visited)
#         exploreGrid(grid, row, column-1, visited)
#         exploreGrid(grid, row, column+1, visited)


def explore(grid, r, c, visited):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])
  if not row_inbounds or not col_inbounds:
    return False
  
  if grid[r][c] == 'W':
    return False
  
  pos = (r, c)
  if pos in visited:
    return False
  visited.add(pos)
  
  explore(grid, r - 1, c, visited)
  explore(grid, r + 1, c, visited)  
  explore(grid, r, c - 1, visited)
  explore(grid, r, c + 1, visited)
  
  return True












def island_count(grid):
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited) == True:
                count += 1
    return count

def explore(grid, r, c, visited):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])
  if not row_inbounds or not col_inbounds:
    return False
  
  if grid[r][c] == 'W':
    return False
  
  pos = (r, c)
  if pos in visited:
    return False
  visited.add(pos)
  
  explore(grid, r - 1, c, visited)
  explore(grid, r + 1, c, visited)  
  explore(grid, r, c - 1, visited)
  explore(grid, r, c + 1, visited)
  
  return True


if __name__ == "__main__":

    grid = [
            ['W', 'L', 'W', 'W', 'W'],
            ['W', 'L', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'L', 'W'],
            ['W', 'W', 'L', 'L', 'W'],
            ['L', 'W', 'W', 'L', 'L'],
            ['L', 'L', 'W', 'W', 'W'],
           ] # ---> 3

    print(island_count(grid))