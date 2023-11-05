#!/usr/bin/python

n,q = 5,2
#n,q = input().split()
n,q = int(n),int(q)
n_arr = [2,5,4,2,4]
#n_arr = list(map(int,input().split()))

q_arr = [[1,3,2],[2,5,2]]
#q_arr = [list(map(int,input().split())) for item in range(q)]


for x in q_arr:
    
    start_index = x[0]
    end_index = x[1]
    hladane_cislo = x[2]
    found = False

    while start_index <= end_index:
        
        if hladane_cislo != n_arr[start_index-1]:
            
            print(n_arr[start_index -1])
            Found = True
            break
        
        start_index = start_index + 1


    if Found == False:
        print(-1)
