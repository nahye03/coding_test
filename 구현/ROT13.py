st = input()
result = ""
for s in st:
    if s.isupper():
        new_s = ord(s)+13
        if new_s>ord('Z'):
            new_s -= 26
        result+= chr(new_s)
    elif s.islower():
        new_s = ord(s)+13
        if new_s>ord('z'):
            new_s -= 26
        result += chr(new_s)
    else:
        result+=s

print(result)

#chr((ord(s)-ord('a')+13)%26 +ord('a'))
