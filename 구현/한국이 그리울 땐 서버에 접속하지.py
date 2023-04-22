n = int(input())
pat = input().split('*')
files = []

for _ in range(n):
    files.append(input())

len_l = len(pat[0])
len_r = len(pat[1])

for f in files:
    if f[:len_l]==pat[0] and f[-len_r:]==pat[1]:
        if len(f) >= len_l + len_r:
            print('DA')
        else:
            print('NE')
    else:
        print('NE')