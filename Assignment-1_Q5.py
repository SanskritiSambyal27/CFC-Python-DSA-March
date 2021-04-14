num = int(input("Enter the number: "))
count = 0
while num > 0:
    r = num//10
    count += 1
    num = r
print(count)