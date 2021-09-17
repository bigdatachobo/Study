S,cnt = input(), 0
for i in range(len(S) - 1):
    if S[i] != S[i-1]: # 바뀌는 부분을 세어준다.
        cnt += 1
print((cnt+1)//2) # 바뀐 부분 센 값에서 1을 더하고 2로 나눠주면 뒤집는 횟수가 나오게된다.
