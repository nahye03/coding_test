n = int(input())
words =set()
for _ in range(n):
    w = input().rstrip()
    words.add((w, len(w)))

words = list(words)
words.sort(key=lambda x:(x[1], x[0]))

for i in range(len(words)):
    print(words[i][0])
