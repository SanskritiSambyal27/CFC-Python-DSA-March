n = 5
for i in range(1, 2*n):
    if i < n:
        for j in range(1, 2*n+1):
            if j<=i or j>2*n-i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    elif i==n:
        for j in range(1, 2*n+1):
            print("*", end=" ")
    else:
        for j in range(1, 2*n+1):
            if j<=(2*n-i) or j>i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()
