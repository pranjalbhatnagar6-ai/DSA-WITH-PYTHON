
def counter():
    n = int(input("Enter the no.: "))
    num = n
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

print(counter())