file_path = "/Users/kevernier/Documents/AdvenOfCode/day2/testday2.txt"

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
# Nested for loop to go through each range
for i in range(len(premiere)):
    # For each range, iterate through all numbers from premiere[i] to seconde[i] (inclusive)
    for num in range(premiere[i], seconde[i] + 1):
        # Convert to string and take the first half
        num_str = str(num)
        half_length = len(num_str) // 2
        first_half = num_str[:half_length]
        second_half = num_str[half_length:]
        
        # Check if first half equals second half
        if first_half == second_half:
            InvalidID.append(num)

# Print the InvalidID list at the end
print(f"Invalid IDs: {InvalidID}")
print(f"Count: {len(InvalidID)}")
