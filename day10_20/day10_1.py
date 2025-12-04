file_path = '/Users/kevernier/Documents/AdvenOfCode/day10_20/test10_1.txt'

with open(file_path, 'r') as f:
    docu = f.read().strip().splitlines()

print(docu)

# Create a new list which sorts the list, while keeping the position of the original stored as a tuple
# This creates a list of (value, original_index) and sorts it
sorted_with_position = sorted([(int(x), i) for i, x in enumerate(docu)])

# Add the charging outlet (0) at the start
sorted_with_position.insert(0, (0, -1))

# Append the built-in adapter which is always 3 higher than the highest adapter
# We use -1 for the original index to indicate it's a synthetic adapter
sorted_with_position.append((sorted_with_position[-1][0] + 3, -1))
print(sorted_with_position)


# Initialize a dictionary to count paths to each adapter
# We start with 1 way to reach the charging outlet (0)
# For all other adapters, we start with 0 paths found so far
paths_count = {item[0]: 0 for item in sorted_with_position}
paths_count[0] = 1

for i, item in enumerate(sorted_with_position):
    current_adapter_val = item[0]
    current_ways = paths_count[current_adapter_val]
    
    # Look ahead at the next 3 adapters in the sorted list
    for offset in range(1, 4):
        if i + offset < len(sorted_with_position):
            next_tuple = sorted_with_position[i + offset]
            next_val = next_tuple[0]
            diff = next_val - current_adapter_val
            
            if diff <= 3:
                # The Logic:
                # If I can jump from A to B, then any path that got me to A
                # can be extended to reach B.
                # So, we add (ways to reach A) to (ways to reach B).
                paths_count[next_val] += current_ways
                print(f"Adapter {current_adapter_val} ({current_ways} paths) connects to {next_val}. New total for {next_val}: {paths_count[next_val]}")

# The answer is the number of ways to reach the final built-in adapter
final_adapter_val = sorted_with_position[-1][0]
print(f"Total permutations: {paths_count[final_adapter_val]}")
