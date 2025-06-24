def decode(grid):
    left = [grid[0][0], grid[1][1], grid[2][1], grid[3][1], grid[4][0]]
    left.reverse()
    right = [grid[0][4], grid[1][3], grid[2][3], grid[3][3], grid[4][4]]
    right.reverse()
    return ''.join(left + right)
print("Enter the grid (5 rows, 5 letters each):")
grid = []
for i in range(5):
    row = input().split()
    if len(row) != 5:
       print("Please enter exactly 5 letters separated by spaces.")
       exit()
    grid.append(row)
decoded_word = decode(grid)
print("\nDecoded word:", decoded_word)









