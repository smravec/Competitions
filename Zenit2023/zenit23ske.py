films = int(input())
films_arr = []

for x in range(films):
    films_arr.append(int(input()))

#Find two max
max1 = -1
max2 = -1

for film in films_arr:
    if film >= max1:
        max2 = max1
        max1 = film
    elif film > max2:
        max2 = film 

all_trailers = len(films_arr) - 2

max2 -= 1
if max1 == max2:
    max2 -= 2
    if max2 - all_trailers <= 0:
        print(max2)
    else:
        print(all_trailers) 
else:
    if max2 - all_trailers <= 0:
        print(max2)
    else:
        print(all_trailers) 