introstr=input("enter your intro:")
print(introstr)
chars=0
words=1
for i in introstr:
    chars=chars+1
    if i==' ':
        words=words+1
print(chars)
print(words)