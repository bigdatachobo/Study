def up_count(array):
    now=array[0]
    result = 1
    for i in range(1,len(array)):
        if now < array[i]:
            result += 1
            now = array[i]
    return result            

n=int(input())
array=[]

for _ in range(n):
    number=int(input())
    array.append(number)

print(up_count(array))
array.reverse()
print(up_count(array))
