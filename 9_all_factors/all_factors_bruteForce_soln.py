num = int(input("Enter no. : "))

def bruteforce():
    global num
    result = []
    for i in range(1, num + 1):
        if num % i==0:
            result.append(i)
    return result


print(bruteforce())