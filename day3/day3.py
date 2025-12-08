file_path = '/Users/kevernier/Documents/AdvenOfCode/day3/test3.txt'

# Time Complexity: O(N^2)
with open(file_path, 'r') as f:
    docu = f.read().strip().splitlines()

results = []
for line in docu:
    best_val = -1
    best_pair = (0, 0, 0)
    
    # Iterate through all pairs (i, j) where i < j
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            val = int(line[i] + line[j])
            if val > best_val:
                best_val = val
                best_pair = (i, j, val)
    
    results.append(best_pair)

print(results)

total = sum([t[2] for t in results])
print(f"Total sum: {total}")
