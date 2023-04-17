arr=[[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
result = 0
arr.sort(key=lambda x:x[1])
cm = -30001

for a in arr:
    if cm<a[0]:
        result+=1
        cm=a[1]

print(result)