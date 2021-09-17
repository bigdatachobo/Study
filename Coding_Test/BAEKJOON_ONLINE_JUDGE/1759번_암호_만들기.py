import copy
result=[]
string=[]
visited=[]

def combination(array,length,index):
    if len(string) == length:
        result.append(copy.deepcopy(string))
        return
    
    for i in range(index,len(array)):
        if i in visited:
            continue
        string.append(array[i])
        visited.append(i)
        combination(array,length,i+1)
        string.pop()
        visited.pop()

vowels=('a','e','i','o','u')        
L,C=map(int,input().split())

array=input().split()
array.sort()

combination(array,L,0)

for password in result:
    count=0
    for word in password:
        if word in vowels:
            count += 1
    
    if count >= 1 and count <= L-2:
        print(''.join(password))
