# Example partie 1
# 12, 38, 15, and 77. Adding these together produces 142.

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
file_value = 0

f = open('input','r+')
for line in f:

    line = (
        line.replace("one", "o1e")
        .replace("two", "t2o")
        .replace("three", "t3e")
        .replace("four", "f4r")
        .replace("five", "f5e")
        .replace("six", "s6x")
        .replace("seven", "s7n")
        .replace("eight", "e8t")
        .replace("nine", "n9e")
    )

    line_value = 0
    
    first = next((ele for ele in list(line) if ele in set(digits)), None)
    last = next((ele for ele in list(reversed(line)) if ele in set(digits)), None)
    
    line_value = int(''.join([first, last]))
    print(f"{line.strip()} = {line_value}")
    file_value += line_value

print(file_value) 