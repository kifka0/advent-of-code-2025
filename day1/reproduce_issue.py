
def solve(rotations):
    dial = 50
    password = 0
    
    for rot in rotations:
        direction = rot[0]
        distance = int(rot[1:])
        
        for _ in range(distance):
            if direction == 'L':
                dial -= 1
                if dial < 0:
                    dial = 99
            elif direction == 'R':
                dial += 1
                if dial > 99:
                    dial = 0
            
            if dial == 0:
                password += 1
                
    return password

example_rotations = [
    "L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"
]
print(f"Example result: {solve(example_rotations)}")

test_rotations = [
    "R50", "R50", "L50", "L50", "R75", "L50", "L25", "L75", "R50"
]
print(f"Test result: {solve(test_rotations)}")
