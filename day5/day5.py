# Advent of Code - Day 5

# Time Complexity: O(N)
def main():
    with open('text5.txt', 'r') as f:
        lines = f.readlines()
    
    # Split input into two parts based on empty line
    first_part = []
    second_part = []
    empty_line_found = False
    num_fresh = 0
    num_spoiled = 0
    
    for line in lines:
        line = line.strip()
        if line == '':
            empty_line_found = True
            continue
        
        if not empty_line_found:
            first_part.append(line)
        else:
            second_part.append(line)
    
    # Store ranges as tuples (start, end) instead of individual numbers
    ranges = []
    
    for range_str in first_part:
        # Parse range like "3-5"
        parts = range_str.split('-')
        start = int(parts[0])
        end = int(parts[1])
        ranges.append((start, end))
    
    print(f"Number of ranges: {len(ranges)}")
    
    # Check if numbers from second part fall within any range
    for num_str in second_part:
        num = int(num_str)
        is_in_range = False
        
        for start, end in ranges:
            if start <= num <= end:
                is_in_range = True
                break
        
        if is_in_range:
            num_fresh += 1
        else:
            num_spoiled += 1
    
    print(f"Number of fresh: {num_fresh}")
    #print(f"Number of spoiled: {num_spoiled}")

if __name__ == "__main__":
    main()
