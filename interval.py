a=[1,4,5,9,10,2,3]
interval=0
minimum=0
maximum=0

for i in range(len(a)):
    if a[i] < minimum:
        minimum = a[i]
    if a[i] > maximum:
        maximum = a[i]
        
interval = maximum - minimum
print(interval)
