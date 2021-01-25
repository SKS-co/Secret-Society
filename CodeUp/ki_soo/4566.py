#4566
def prime_list(m,n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * (n+1)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    s = int(n ** 0.5)
    for i in range(2, s + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n+1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False
    
    # 소수 목록 산출
    return [i for i in range(m ,n+1) if sieve[i] == True]

m = int(input())
n = int(input())
arr = prime_list(m,n)
if 1 in arr:
    arr.remove(1)
    
if len(arr) != 0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)
