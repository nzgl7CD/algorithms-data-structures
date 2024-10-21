direction = "DLRU"
# Arrays to represent change in rows and columns
dr = [1, 0, 0, -1]
dc = [0, -1, 1, 0]

def is_valid(row, col, n, maze):
    return 0 <= row < n and 0 <= col < n and maze[row][col] == 1

# Function to get all valid paths

def find_path(row, col, maze, n, ans, current_path):
    # If we reach the bottom right cell of the matrix, add
    # the current path to ans and return
    if row == n - 1 and col == n - 1:
        ans.append(current_path)
        return
    # Mark the current cell as blocked
    maze[row][col] = 0

    for i in range(4):
        next_row = row + dr[i]
        next_col = col + dc[i]
        # Check if the next cell is valid or not
        if is_valid(next_row, next_col, n, maze):
            current_path += direction[i]
            find_path(next_row, next_col, maze, n, ans, current_path)
            current_path = current_path[:-1]

    # Mark the current cell as unblocked
    maze[row][col] = 1


# Driver code
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

n = len(maze)
# List to store all the valid paths
result = []
# Store current path
current_path = ""

if maze[0][0] != 0 and maze[n - 1][n - 1] != 0:
    # Function call to get all valid paths
    find_path(0, 0, maze, n, result, current_path)

if not result:
    print(-1)
else:
    print(" ".join(result))