num = int(input("Enter no. : "))

def bettersoln(num):
    result = []
    for i in range(1,num//2):
        if num%i==0:
            result.append(i)
    result.append(num)
    return result

print(bettersoln(num))