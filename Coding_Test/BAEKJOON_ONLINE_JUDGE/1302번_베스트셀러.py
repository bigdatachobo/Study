n=int(input())
count={}

for _ in range(n):
    word=input()
    try:count[word] += 1
    except:count[word] = 1

target=max(count.values())
array=[]

for key,number in count.items():
    if number == target:
        array.append(key)
print(sorted(array)[0])
