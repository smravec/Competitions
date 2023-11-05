kam = int(input())
arr_kam = list(map(int,input().split()))

sum = 0
for num in arr_kam:
    sum += num

for num in arr_kam:
    print(sum - num)