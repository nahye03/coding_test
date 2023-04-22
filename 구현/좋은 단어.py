n = int(input())
words = []
for _ in range(n):
    words.append(input())

result = 0
for word in words:
    st = []
    for w in word:
        if not st:
            st.append(w)
        else:
            if st[-1]==w:
                st.pop()
            else:
                st.append(w)
    if not st:
        result+=1
print(result)