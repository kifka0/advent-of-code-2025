# Advent of Code - Day 7 Part 2
from collections import defaultdict

# Time Complexity: O(N)
def main():
    filename = 'text7.txt'
    with open(filename, 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]

    # Find S in the first line
    start_col = -1
    if 'S' in grid[0]:
        start_col = grid[0].index('S')
    
    if start_col == -1:
        print("Start point 'S' not found!")
        return

    print(f"Start point 'S' found at column {start_col}")

    # Dictionary mapping column index to number of paths reaching it
    # {col_index: count}
    active_paths = defaultdict(int)
    active_paths[start_col] = 1
    
    # Process line by line starting from the second line
    for r in range(1, len(grid)):
        next_active_paths = defaultdict(int)
        
        for c, count in active_paths.items():
            # Check bounds
            if c < 0 or c >= len(grid[r]):
                continue
                
            char = grid[r][c]
            
            if char == '.':
                # Flow continues down
                next_active_paths[c] += count
            elif char == '^':
                # Splitter: flow goes left and right
                # Check Left
                if c - 1 >= 0:
                    left_char = grid[r][c-1]
                    if left_char == '.':
                        next_active_paths[c-1] += count
                
                # Check Right
                if c + 1 < len(grid[r]):
                    right_char = grid[r][c+1]
                    if right_char == '.':
                        next_active_paths[c+1] += count
            elif char == '|':
                # If it's already a pipe, treat it like '.' (flow continues/merges)
                next_active_paths[c] += count
        
        active_paths = next_active_paths
        
        # Optimization: if no paths, stop
        if not active_paths:
            break

    # Sum all paths at the bottom
    total_paths = sum(active_paths.values())
    print(f"\nTotal different paths: {total_paths}")

if __name__ == "__main__":
    main()
