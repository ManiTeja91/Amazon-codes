arr = [640,26,276,224,737,677,893,87,422,30]
operations = [[0,9], 
[2, 2],
[5, 5],
[1, 6],
[5, 6],
[5, 9],
[0, 8],
[6, 7],
[1, 9],
[3, 3]]

for i in range(len(operations)):
        n, m = operations[i][0], operations[i][1]
        if n == 0 and m == len(arr)-1:
            arr.reverse()
        elif n == 0:
            arr = list(reversed(arr[0:m+1])) + arr[m+1:]
        elif m == 9:
            arr = arr[0:n] + list(reversed(arr[n:]))
        else:
            arr = arr[0:n] + list(reversed(arr[n:m+1])) + arr[m+1:]
        print(arr)
        
        
print(arr)


    