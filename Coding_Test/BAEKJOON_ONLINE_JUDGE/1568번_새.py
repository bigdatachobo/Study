def bird_count(num,time):
    if num == 0:
        return time
    n=int(((1+8*num)**(1/2)-1)/2)
    prep_num=num-(n*(n+1)/2)
    time += n
    return bird_count(prep_num,time)

number=int(input())

print(bird_count(number,0))            
