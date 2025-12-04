file_path = '/Users/kevernier/Documents/AdvenOfCode/day10_20/test10_1.txt'

with open(file_path, 'r') as f:
    docu = f.read().strip().splitlines()

print(docu)

# Create a new list which sorts the list, while keeping the position of the original stored as a tuple
# This creates a list of (value, original_index) and sorts it
sorted_with_position = sorted([(int(x), i) for i, x in enumerate(docu)])
print(sorted_with_position)

jumps = {1: 0, 2: 0, 3: 0}
current_val = 0

for item in sorted_with_position:
    next_val = item[0]
    diff = next_val - current_val
    if diff in jumps:
        jumps[diff] += 1
    print(f"{current_val} to {next_val} is a {diff} jump")
    current_val = next_val

print(f"Jumps of 1: {jumps[1]}")
print(f"Jumps of 2: {jumps[2]}")
print(f"Jumps of 3: {jumps[3]+1}") #the plus 1 at the end is because the last jump is always 3
