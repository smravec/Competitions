pocet_ciselx = int(input())
arr8 = []

for y in range(pocet_ciselx):
    arr8.append(input())

found = "WA"

pat1 = "ZENIT"
pat2 = "TINEZ"

#Arr horizontal 
for line in arr8:
    if line.find(pat1) != -1 or line.find(pat2) != -1:
        found = "OK"

#Arr vertical
ver_arr = []
for index,line in enumerate(arr8):
    if index == 0:
        for char in line:
            ver_arr.append(char)
    else:
        index1 = 0
        for char in line:
            ver_arr[index1] = f"{ver_arr[index1]}{char}" 
            index1 +=1

for line in ver_arr:
    if line.find(pat1) != -1 or line.find(pat2) != -1:
        found = "OK"

#Arr diagonal left to right
digl_arr = []
num_of_chars = pocet_ciselx - 4
current_index = 0
for index,line in enumerate(arr8):
    if index == 0:
        for char in range(num_of_chars):
            digl_arr.append(line[char + current_index])

    else:
        for char in range(num_of_chars):
            if char + current_index < len(line):
                digl_arr[char] = f"{digl_arr[char]}{line[char + current_index]}"

    current_index += 1

for line in digl_arr:
    if line.find(pat1) != -1 or line.find(pat2) != -1:
        found = "OK"

#Arr diagonal right to left
digr_arr = []
num_of_chars = pocet_ciselx - 4
current_index = -1

for index,line in enumerate(arr8):
    if index == 0:
        for char in range(num_of_chars):
            digr_arr.append(line[ (char*-1) + current_index])
        
    else:
        for char in range(num_of_chars):
            if (char *-1) + current_index >= (len(line) * -1):
                digr_arr[char] = f"{digr_arr[char]}{line[(char*-1) + current_index]}"

    current_index -= 1

for line in digr_arr:
    if line.find(pat1) != -1 or line.find(pat2) != -1:
        found = "OK"

print(found)