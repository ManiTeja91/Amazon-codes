from collections import Counter

arr = [10,6,7,9,5,5,9,10,10,6,9]

#finding count and creating a new array
frequency = Counter(arr)

arr1 = []
for value, count in frequency.items():
    arr1.append([value,count])
    
print(arr1)

#sorting the array based on the frequency

#   Quick Sort
arr2 = sorted(arr1, key=lambda x: (-x[1],x[0]))
print(arr2)