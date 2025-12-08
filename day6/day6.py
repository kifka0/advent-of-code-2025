# Advent of Code - Day 6

# Time Complexity: O(N)
def main():
    # Read the input file
    with open('text6.txt', 'r') as f:
        lines = f.readlines()

    matrix = []
    for line in lines:
        # Split line by whitespace
        parts = line.strip().split()
        if not parts:
            continue
        row = []
        for part in parts:
            # Try to convert to int, keep as string if it's an operator
            try:
                row.append(int(part))
            except ValueError:
                row.append(part)
        matrix.append(row)

    # Transpose the matrix
    # zip(*matrix) takes the columns and makes them rows
    transposed_matrix = list(map(list, zip(*matrix)))

    total_sum = 0

    print(f"Processing {len(transposed_matrix)} rows...")

    for i, row in enumerate(transposed_matrix):
        operator = row[-1]
        numbers = row[:-1]
        
        result = 0
        
        if operator == '+':
            result = sum(numbers)
            print(f"Row {i+1}: Sum({numbers}) = {result}")
        elif operator == '*':
            result = 1
            for num in numbers:
                result *= num
            print(f"Row {i+1}: Product({numbers}) = {result}")
        else:
            print(f"Row {i+1}: Unknown operator '{operator}'")
            continue
            
        total_sum += result

    print(f"\nTotal Sum of all results: {total_sum}")

if __name__ == "__main__":
    main()
