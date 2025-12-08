# Read the input file and store it in a 2D vector (list of lists)
# This allows access using coordinates: grid[row][col]

# Time Complexity: O(N*M)
def remove_isolated_symbols(grid):
    """
    Count @ symbols with fewer than 4 @ neighbors and create a new grid
    where those @ symbols are replaced with '.'
    
    Returns: (new_grid, count)
    """
    rows = len(grid)
    cols = len(grid[0])
    counter = 0
    
    # Create a copy of the grid for modifications
    new_grid = [row[:] for row in grid]  # Deep copy
    
    # Go through each position in the grid
    for row in range(rows):
        for col in range(cols):
            # Check if current position is @
            if grid[row][col] == '@':
                # Count neighboring @ symbols in all 8 directions
                neighbor_count = 0
                
                # Check all 8 neighbors: -1, 0, +1 for both row and col
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        # Skip the center position (0, 0)
                        if dr == 0 and dc == 0:
                            continue
                        
                        # Calculate neighbor position
                        new_row = row + dr
                        new_col = col + dc
                        
                        # Check if neighbor is within bounds
                        if 0 <= new_row < rows and 0 <= new_col < cols:
                            # Check if neighbor is @
                            if grid[new_row][new_col] == '@':
                                neighbor_count += 1
                
                # If fewer than 4 neighbors, replace with '.' and increment counter
                if neighbor_count < 4:
                    new_grid[row][col] = '.'
                    counter += 1
    
    return new_grid, counter


# Read and create initial grid
with open('/Users/kevernier/Documents/AdvenOfCode/day4/text4.txt', 'r') as f:
    lines = f.readlines()

# Create a 2D grid where each element can be accessed by grid[row][col]
grid = []
for line in lines:
    # Strip the newline character and convert the line to a list of characters
    row = list(line.strip())
    grid.append(row)

# Print grid dimensions
print(f"Grid dimensions: {len(grid)} rows x {len(grid[0])} columns")

# Process the grid repeatedly until no more @ symbols are removed
total_removed = 0
iteration = 0
current_grid = grid

while True:
    new_grid, removed_count = remove_isolated_symbols(current_grid)
    iteration += 1
    total_removed += removed_count
    
    print(f"\nIteration {iteration}: Removed {removed_count} @ symbols")
    
    # If no symbols were removed, we're done
    if removed_count == 0:
        break
    
    # Update current grid for next iteration
    current_grid = new_grid

print(f"\n{'='*50}")
print(f"Total @ symbols removed: {total_removed}")
print(f"Total iterations: {iteration}")
