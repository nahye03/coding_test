s = input()
rs = ''.join(i for i in s[::-1])

if s==rs:
    print(1)
else:
    print(0)