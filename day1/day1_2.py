# Time Complexity: O(N)
file_path = '/Users/kevernier/Documents/AdvenOfCode/day1/textday1.txt'

with open(file_path, 'r') as f:
    # Read the whole file content into a single string
    #file_content = f.read() 
    
    # OR read all lines into a list
    docu = f.readlines()

#print (docu)

results_list =[]
firstLetters = [word[0] for word in docu]

#print(firstLetters)
for item in docu:
    if len(item)>=3:
        substring = item[1:]
        try:
            # Convert the substring to an integer
            result_int = int(substring)
            #while result_int >= 100 or result_int<0:#if i do mistake and it becomes negative dont want an infinite loop
                #result_int -= 100
            results_list.append(result_int)
        
        except ValueError:
            print(f"Skipped item '{item}': Substring '{substring}' is not numeric.")
    else:
        print(f"Skipped item '{item}': Too short to extract the 2nd and 3rd characters.")

#print(results_list)
dial = 50
password =0

for i in range (0,len(docu)):
    if firstLetters[i] == "L":
        print(f"L{i} {dial} minus {results_list[i]} ")
        dial -= results_list[i]
        while dial < 0:
            dial +=100
            print(f"L{i} {dial} password +1")
            password+=1
        

    elif firstLetters[i] == "R":
        print(f"R{i} {dial} plus {results_list[i]} ")
        dial += results_list[i]
        while dial >= 100:
            dial -= 100
            print(f"R{i} {dial} password +1")
            password+=1
"""     if dial == 0:
        password +=1
 """
print (f" password is {password}")
#so the answer is 5899 sooooo yeah, still don't know exact where but AI knows no motivation to check now, maybe one day