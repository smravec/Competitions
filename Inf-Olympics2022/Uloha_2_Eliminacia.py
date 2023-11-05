#!/usr/bin/python

import math

pocet_kolacov = int(input())
kolace_arr= list(map(int,input().split()))

kto_konci = ""

if math.log(pocet_kolacov,2) // 2 != math.log(pocet_kolacov,2) / 2:
    kto_konci = "Andras"
else:
    kto_konci = "Sandra"


def andrasov_tah(arr):
    
    arr_index = 0
    new_arr = []

    while arr_index + 1 <= len(arr) - 1:
    
        if arr[arr_index] > arr[arr_index + 1]:
            new_arr.append(arr[arr_index])
        
        else:
            new_arr.append(arr[arr_index + 1])
        
        arr_index += 2
    
    return new_arr


def sandrin_tah(arr):

    arr_index = 0
    new_arr = []

    while arr_index + 1 <= len(arr) - 1:
    
        if arr[arr_index] < arr[arr_index + 1]:
            new_arr.append(arr[arr_index])
        
        else:
            new_arr.append(arr[arr_index + 1])
        
        arr_index += 2
    
    return new_arr

momentalny_tah = kto_konci

while len(kolace_arr) != 1 :

    if momentalny_tah == "Andras":
        kolace_arr = andrasov_tah(kolace_arr)
        momentalny_tah = "Sandra"

    else:
        kolace_arr = sandrin_tah(kolace_arr)
        momentalny_tah = "Andras"
        
print(kolace_arr[0])
