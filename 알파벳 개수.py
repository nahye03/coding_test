sentence = input()
a = ord('a')
result = [0]*26

for s in sentence:
    result[ord(s)-a] +=1

print(*result)