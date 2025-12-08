# Advent of Code - Day 7

# Time Complexity: O(N)
def main():
    filename = 'text7.txt'
    with open(filename, 'r') as f:
        # Read lines and convert to list of lists (mutable)
        grid = [list(line.strip()) for line in f.readlines()]

    # Find S in the first line
    start_col = -1
    if 'S' in grid[0]:
        start_col = grid[0].index('S')
    
    if start_col == -1:
        print("Start point 'S' not found!")
        return

    print(f"Start point 'S' found at column {start_col}")

    # Set of active columns where flow is coming from
    active_cols = {start_col}
    split_count = 0
    
    # Process line by line starting from the second line
    for r in range(1, len(grid)):
        next_active_cols = set()
        
        for c in active_cols:
            # Check bounds
            if c < 0 or c >= len(grid[r]):
                continue
                
            char = grid[r][c]
            
            if char == '.':
                # Flow continues down
                grid[r][c] = '|'
                next_active_cols.add(c)
            elif char == '^':
                # Splitter: flow goes left and right
                split_count += 1
                # Check Left
                if c - 1 >= 0:
                    left_char = grid[r][c-1]
                    if left_char == '.':
                        grid[r][c-1] = '|'
                        next_active_cols.add(c-1)
                
                # Check Right
                if c + 1 < len(grid[r]):
                    right_char = grid[r][c+1]
                    if right_char == '.':
                        grid[r][c+1] = '|'
                        next_active_cols.add(c+1)
            elif char == '|':
                # If it's already a pipe (maybe from another merge), continue flow?
                # The prompt implies we are modifying the grid as we go.
                # If flow merges, we just add to next_active_cols
                next_active_cols.add(c)
        
        active_cols = next_active_cols
        
        # If no more active columns, we can stop (optimization)
        if not active_cols:
            break

    # Print the result and count |
    print("\nFinal Grid:")
    total_pipes = 0
    total_splits = 0
    
    for r, row in enumerate(grid):
        row_str = "".join(row)
        pipes_in_row = row_str.count('|')
        splits_in_row = row_str.count('^') # This counts all ^, not just active ones.
        
        # To count active splits, we should have tracked it during simulation.
        # But let's just count total | for now as requested "count the char | after each line"
        
        total_pipes += pipes_in_row
        print(f"{row_str} (Pipes: {pipes_in_row})")

    print(f"\nTotal '|' count: {total_pipes}")
    print(f"Total splits encountered: {split_count}")

if __name__ == "__main__":
    main()
