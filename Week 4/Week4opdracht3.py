def B2(k, n):
    grid = list(list(0 for _ in range(k+1)) for _ in range(n+1))
    
    for r in range(n+1): #row counter
        for c in range(k+1): #column counter
            if c == 0:
                grid[r][c] = 1
                continue 
            if c > 0:
                value = grid[r-1][c] + grid[r-1][c-1]
                grid[r][c] = value
    
    return grid[len(grid)-1][len(grid[0])-1] #bottom right element which should be the result

print(B2(3,6))