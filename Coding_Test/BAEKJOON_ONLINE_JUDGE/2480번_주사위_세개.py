array = list(map(int,input().split()))
prize = 0

if len(set(array)) == 1: ## 3개 다 같은 눈
    prize = 10000 + array[0] * 1000

elif len(set(array)) == 2: ## 2개가 같은 눈
    temp = list(set(array))
    if array.count(temp[0]) == 2:
        prize = 1000 + temp[0] * 100
    else:
        prize = 1000 + temp[1] * 100

elif len(set(array)) == 3:
    num = max(array)
    prize = num * 100

print(prize)
