dc = [1,2,2]

ds = [5,2,4]

dc.sort()
ds.sort()
t = 0
for i in range(len(dc)):
    t += abs(dc[i]-ds[i])
print(t)