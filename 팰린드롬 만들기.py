name = input()
alpha = [0]*26

for n in name:
    alpha[ord(n)-ord('A')]+=1

left =""
mid=""

for i in range(26):
    al = chr(i+ord('A'))
    if alpha[i]%2==0:
        left+=al*(alpha[i]//2)
    else:
        if mid:
            mid="f"
            break
        else:
            mid+=al
            left += al * (alpha[i] // 2)

if mid=="f":
    print("I'm Sorry Hansoo")
else:
    right = ''.join(reversed(list(left)))
    print(left+mid+right)

######다른 방법
l = input()
a = [i for i in set(l) if l.count(i)%2==1]
b = "".join(sorted([i*(l.count(i)//2) for i in set(l)]))
if len(a)>1:
    print("I'm Sorry Hansoo")
elif len(a)==0:
    print(b+b[::-1])
else:
    print(b+a[0]+b[::-1])