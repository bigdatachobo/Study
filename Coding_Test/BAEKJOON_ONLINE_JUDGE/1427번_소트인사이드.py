number=input()

for i in range(9,-1,-1):
    for j in number:
        if i == int(j):
            print(i, end='')
