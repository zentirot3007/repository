a=[1,4,5,9,10,2,3]
interval=0

for i in range (len(a)):
    for j in range (len(a)):
        diff=abs(a[i]-a[j])
        if diff>interval:
            interval = diff
print(interval)