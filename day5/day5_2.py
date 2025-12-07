# Advent of Code - Day 5 Part 2

def main():
    with open('text5.txt', 'r') as f:
        lines = f.readlines()
    
    # Read only the ranges (first part before empty line)
    ranges = []
    
    for line in lines:
        line = line.strip()
        if line == '':
            break  # Stop at empty line
        
        # Parse range like "3-5"
        parts = line.split('-')
        start = int(parts[0])
        end = int(parts[1])
        ranges.append((start, end))
    
    print(f"Original ranges: {len(ranges)}")
    
    # Sort ranges by start position
    ranges.sort()
    
    # Merge overlapping ranges
    merged_ranges = []
    
    for start, end in ranges:
        # If merged_ranges is empty or current range doesn't overlap with the last merged range
        if not merged_ranges or merged_ranges[-1][1] < start - 1:
            # Add as new range
            merged_ranges.append((start, end))
        else:
            # Overlaps or adjacent, so merge with the last range
            # Update the end of the last range to be the max of both ends
            merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], end))
    
    print(f"Merged ranges: {len(merged_ranges)}")
    
    # Calculate total count of numbers in all merged ranges
    total_count = 0
    
    for start, end in merged_ranges:
        count = end - start + 1
        total_count += count
        print(f"Range [{start}-{end}]: {count:,} numbers")
    
    print(f"\nTotal unique numbers: {total_count:,}")

if __name__ == "__main__":
    main()
