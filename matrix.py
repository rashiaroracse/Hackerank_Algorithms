n = int(input())
arr = []
a = 0
b = 0
for i in range(n):
    arr.append(list(map(int,input().rstrip().split())))
print(arr)
for h in range(n):
    for k in range(n):
        if h == k:
            a += arr[h][k]
        if h == n-k-1:
            b += arr[h][k]
print(abs(a-b))


