arr = [1,-2,3]

arr.sort(reverse = True)
print(arr)
c = 0
t = 0
for i in arr:
    c += i
    t += c
print(t)