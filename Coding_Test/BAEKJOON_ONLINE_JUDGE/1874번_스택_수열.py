n = int(input())

stack = []
result = []
number = 1

for i in range(1,n+1):
    data = int(input())
    
    while number <= data:
        stack.append(number)
        number += 1
        result.append('+')
    
    if data == stack[-1]:
        stack.pop()
        result.append('-')
    
    else:
        print("NO")
        exit(0)
print('\n'.join(result))
