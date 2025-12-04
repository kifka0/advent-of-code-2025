def solve(commands):
    dial = 50
    password = 0
    for cmd, val in commands:
        if cmd == "L":
            dial -= val
            if dial < 0:
                password += 1
                dial = dial % 100
        elif cmd == "R":
            dial += val
            if dial >= 100:
                password += 1
                dial = dial % 100
    return password, dial

# Test cases
# L 250: 50 - 250 = -200. Should count 1. Dial -> 0.
print(f"L 250: {solve([('L', 250)])}") 
# R 250: 50 + 250 = 300. Should count 1. Dial -> 0.
print(f"R 250: {solve([('R', 250)])}")
# L 50: 50 - 50 = 0. Should count 0. Dial -> 0.
print(f"L 50: {solve([('L', 50)])}")
# R 50: 50 + 50 = 100. Should count 1. Dial -> 0.
print(f"R 50: {solve([('R', 50)])}")
