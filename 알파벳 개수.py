sentence = input()
a = ord('a')
result = [0]*27

for s in sentence:
    result[ord(s)-a] +=1

for i in result:
    print(i, end=' ')