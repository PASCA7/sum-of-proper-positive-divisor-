def maneesh(N):
    arr = []
    for i in range(1,N):
        if N % i == 0:
            arr.append(i)   
    i = 0
    total = 0
    while N >= total:
        if i == len(arr):
            break
        total = total + arr[i]
        prev = total
        i = i+1
    if total == N:
        return 'YES'
    else:
        return 'NO'
            
           
    
    
    
T = int(input())
for _ in range(T):
    N = int(input())
    out_ = maneesh(N)
    print (out_)
    
