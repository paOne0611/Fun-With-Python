#Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#src: https://leetcode.com/problems/number-of-islands/description/
 
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

def dfs(grid,inner,outer):
    
    #the entries out of bounds or "0" are water (not to be counted)
    if inner<0 or outer>=len(grid) or outer<0 or inner>=len(grid[outer]) or grid[outer][inner]=="0" :                           
        return None
    
    grid[outer][inner]="0"  #sinking the visited land
    
    #recursion
    dfs(grid,inner+1, outer)  #moving horizontally right
    dfs(grid,inner, outer+1)  #moving vertically down
    #not required to check for up or left, it has been set to "0"


def countIslands(grid):
    num=0
    #traversing throughout the grid
    for o in range(len(grid)):
        for i in range(len(grid[o])):
            if grid[o][i]!="0":   #no water found
                num+=1
                dfs(grid,i, o)
    print(num)
countIslands(grid)











 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 