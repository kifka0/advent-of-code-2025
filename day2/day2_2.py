file_path = "/Users/kevernier/Documents/AdvenOfCode/day2/textday2.txt"

with open(file_path, "r") as file:
    # Read the entire content of the file and remove any trailing newline
    content = file.read().strip()
    
    # Split the content at every comma
    items = content.split(',')

# Now 'items' is a list of strings, e.g., ['11-22', '95-115', ...]
#I guess no leading zeroes is helping me bc I dont know how to handle them
premiere = []
seconde = []
InvalidID = []

for item in items:
    premiere.append((int(item.split('-')[0])))
    seconde.append((int(item.split('-')[1])))
# Function to check if a string has a repeating pattern
# Time Complexity: O(N)
def has_repeating_pattern(s):
    length = len(s)
    # Check all possible pattern lengths (divisors of the total length)
    for pattern_len in range(1, length):
        # Only check if pattern_len divides evenly into length
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            # Check if repeating this pattern gives us the original string
            if pattern * (length // pattern_len) == s:
                return True
    return False

# Nested for loop to go through each range
for i in range(len(premiere)):
    # For each range, iterate through all numbers from premiere[i] to seconde[i] (inclusive)
    for num in range(premiere[i], seconde[i] + 1):
        # Convert to string
        num_str = str(num)
        
        # Check if the number has a repeating pattern
        if has_repeating_pattern(num_str):
            InvalidID.append(num)

# Print the InvalidID list at the end
print(f"Invalid IDs: {InvalidID}")
print(f"Count: {len(InvalidID)}")
print(f"Sum: {sum(InvalidID)}")
