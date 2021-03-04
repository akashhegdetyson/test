def solve(arr):
    res = []
    s = []
    for i in range(len(arr)):
        if(len(s) == 0):
            res.append(1)
        elif(s[-1] > arr[i]):
            res.append(1)
        else:
            while(s and s[-1] <= arr[i]):
                s.pop()
            if(len(s) == 0):
                res.append(i+1)
            else:
                res.append(i-arr.index(s[-1]))
        s.append(arr[i])

    return(res)

arr = list(map(int, input().strip().split()))
result = solve(arr)
print(*result)