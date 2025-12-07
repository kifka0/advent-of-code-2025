# Advent of Code - Day 6 Part 2

def main():
    # Read the input file
    filename = 'text6.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines = [line.replace('\n', '') for line in lines]

    # 1. Pad lines to max length to form a rectangle
    max_len = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_len, ' ') for line in lines]
    
    # 2. Transpose the character grid
    # zip(*padded_lines) gives us the columns of the file as rows
    transposed_grid = list(zip(*padded_lines))
    
    total_sum = 0
    current_numbers = []
    current_operator = None
    
    print(f"Processing {len(transposed_grid)} columns...")
    
    for i, row in enumerate(transposed_grid):
        # The last character in the row is from the last line (operator line)
        # The characters before it are the digits
        potential_operator = row[-1]
        digits = row[:-1]
        
        # Check if this column has any digits
        num_str = "".join(digits).replace(" ", "")
        
        if num_str:
            # It's a number column
            number = int(num_str)
            current_numbers.append(number)
            
            # Check for operator
            if potential_operator in ('+', '*'):
                current_operator = potential_operator
        else:
            # It's an empty column (separator)
            # If we have a group collected, process it
            if current_numbers:
                if current_operator:
                    result = 0
                    if current_operator == '+':
                        result = sum(current_numbers)
                        print(f"Group {current_numbers} (+) -> {result}")
                    elif current_operator == '*':
                        result = 1
                        for num in current_numbers:
                            if num == 0:
                                continue
                            result *= num
                        print(f"Group {current_numbers} (*) -> {result}")
                    
                    total_sum += result
                else:
                    print(f"Warning: Group {current_numbers} has no operator!")
                
                # Reset for next group
                current_numbers = []
                current_operator = None
                
    # Process the final group if exists
    if current_numbers:
        if current_operator:
            result = 0
            if current_operator == '+':
                result = sum(current_numbers)
                print(f"Group {current_numbers} (+) -> {result}")
            elif current_operator == '*':
                result = 1
                for num in current_numbers:
                    if num == 0:
                        continue
                    result *= num
                print(f"Group {current_numbers} (*) -> {result}")
            
            total_sum += result
        else:
            print(f"Warning: Group {current_numbers} has no operator!")

    print(f"\nTotal Sum: {total_sum}")

if __name__ == "__main__":
    main()
