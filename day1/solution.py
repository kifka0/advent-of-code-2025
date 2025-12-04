file_path = '/Users/kevernier/Documents/AdvenOfCode/day1/textday1.txt'

with open(file_path, 'r') as f:
    docu = f.readlines()

results_list =[]
firstLetters = [word[0] for word in docu]

for item in docu:
    if len(item)>=3:
        substring = item[1:10]
        try:
            result_int = int(substring)
            results_list.append(result_int)
        except ValueError:
            print(f"Skipped item '{item}': Substring '{substring}' is not numeric.")
    else:
        print(f"Skipped item '{item}': Too short to extract the 2nd and 3rd characters.")

dial = 50
password = 0

for i in range (0,len(docu)):
    if firstLetters[i] == "L":
        dial -= results_list[i]
        if dial < 0:
            password += 1
            dial = dial % 100

    elif firstLetters[i] == "R":
        dial += results_list[i]
        if dial >= 100:
            password += 1
            dial = dial % 100

print (f" password is {password}")
