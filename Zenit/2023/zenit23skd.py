nums = int(input())
num_arr = []
for num in range(nums):
    num_arr.append(int(input()))

bin_num_arr = []
for num in num_arr:
    bin_num_arr.append("{:032b}".format(num))

for index,num in enumerate(bin_num_arr):
    new_num = ""
    last_char = len(num) -1
    while last_char >= 0:
        new_num = f"{new_num}{num[last_char]}"
        bin_num_arr[index] = new_num
        last_char -= 1     

for num in bin_num_arr:
    print(int(num,2))