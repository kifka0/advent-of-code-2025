file_path = '/Users/kevernier/Documents/AdvenOfCode/day3/text3.txt'

with open(file_path, 'r') as f:
    docu = f.read().strip().splitlines()

results = []
for line in docu:
    # We want to find a subsequence of length 12 that forms the largest number.
    # We also need the indices of these digits.
    # We use a greedy approach with a stack.
    
    k = 12
    stack = [] # Stores tuples of (digit, index)
    n = len(line)
    
    for i, char in enumerate(line):
        digit = int(char)
        remaining_chars = n - 1 - i
        
        # While we can pop from stack and still have enough chars left to fill it to size k
        # and the current digit is better than the top of the stack
        while stack and stack[-1][0] < digit and (len(stack) - 1 + remaining_chars + 1) >= k:
            stack.pop()
            
        if len(stack) < k:
            stack.append((digit, i))
            
    # Extract indices and value
    indices = tuple(item[1] for item in stack)
    val_str = "".join(str(item[0]) for item in stack)
    val = int(val_str)
    
    # Result format: (idx1, idx2, ..., idx12, val)
    result_tuple = indices + (val,)
    results.append(result_tuple)

print(results)

total = sum([t[-1] for t in results])
print(f"Total sum: {total}")
