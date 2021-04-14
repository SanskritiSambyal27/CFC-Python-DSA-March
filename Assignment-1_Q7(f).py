n = 5
for i in range(1, 2*n):
    if i == 1:
        for j in range(1, 2*n):
            if j == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    elif i>1 and i<n:
        for j in range(1, 2*n):
            if j == n:
                print("*", end=" ")
            if j<(n-i+1) or j>=(2*n-(n-i)-1):
                print(" ", end=" ")
            else:
                print("*", end=" ")
    elif i == n:
        for j in range(1, 2*n):
            print("*", end=" ")
    else:
        for j in range(1, 2*n):
            if j == n:
                print("*", end=" ")
            elif j<=(i-n) or j>=(2*n-(i-n)):
                print(" ", end=" ")
            else:
                print("*", end=" ")
    print()