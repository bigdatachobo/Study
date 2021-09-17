string=input()
word=input()

count=0
i=0
while len(string)-i >= len(word):
    if string[i:i+len(word)]==word:
        i += len(word)
        count += 1
    else:
        i += 1
print(count)
