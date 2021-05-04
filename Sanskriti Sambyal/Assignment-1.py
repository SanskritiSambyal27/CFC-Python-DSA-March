
#1
cred = int(input("Enter the credits"))
if cred<4500:
    print("Rising Star")
elif cred>=4500 and cred<6000:
    print("Mega Leader")
elif cred>=6000 and cred<7500:
    print("Gega Leader")
elif cred>=7500:
    print("Tera Leader")

#2
amount = int(input("Enter the amount: "))
rate = int(input("Enter the rate: "))
time = int(input("Enter the time(in years): "))
simple_interest = (amount*rate*time)/100
print("Simple Interest: ",simple_interest)

#3
def hcf(a, b):
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("The GCD of",a,"and",b,"is: ",hcf(a,b))

#4
series_range = int(input("Enter the range for even series odd jumps"))
num = 2
toadd = 4
while num <= series_range:
    print(num,end=' ')
    num += toadd
    toadd += 4
print()
print()


#5
num = int(input("Enter the number: "))
count = 0
while num > 0:
    r = num//10
    count += 1
    num = r
print(count)

#6
num = int(input("Enter the number: "))
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num//10
print (rev)

#7(a)
n = 5
row = 1
while row <= n:
    col = 1
    while col <= row:
        print("*", end=" ")
        col += 1
    print()
    row += 1

#7(b)
n = 5
row = 1
while row <= n:
    col = 1
    while col <= row:
        print(col, end=" ")
        col += 1
    print()
    row += 1

#7(c)
row = 0
n = 5
while row < n:
    col = 0
    count_for_col = 1
    while col <= row:
        print(count_for_col,end=" ")
        count_for_col += 1
        col += 1
    print()
    row += 1

print()
print()

#7(d)
row = 0
n = 5
while row < n:
    col = 0
    count_for_col = 1
    while col < n + row :
        if col + row < n - 1:
            print(" ", end=" ")
        else:
            print(count_for_col, end=" ")
            if col < n -1:
                count_for_col += 1
            else:
                count_for_col -= 1
        col += 1
    print()
    row += 1

print()
print()

#7(e)
n = 5
for i in range(1, n+1):
    if i == 1:
        j = i
        print(j, end=" ")
    else:
        j = j * 11
        print(j, end=" ")
    print()

#7(f)
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

#7(g)
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

#7(h)
user_inp = 5
row_mirror = 0
row = 0
while row_mirror < 2 * user_inp - 1:
    col = 0
    while col < 2 * user_inp:
        if col > row and col < (2*user_inp) - (row + 1):
            print(" ",end=" ")
        else:
            print("*",end=" ")
        col += 1
    print()
    if row_mirror < user_inp - 1:
        row += 1
    else:
        row -= 1
    row_mirror += 1
print()
print()

#7(i)
a = [[0 for i in range(MAX)]
         for i in range(MAX)]
    while (n != 0):
        for i in range(front, back + 1):
            for j in range(front, back + 1):
                if (i == front or i == back or
                        j == front or j == back):
                    a[i][j] = n
        front += 1
        back -= 1
        n -= 1
    prints(a, size);

n = 5

innerPattern(n)