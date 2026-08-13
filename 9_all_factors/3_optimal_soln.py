from math import sqrt
num = int(input("Enter no. : "))

def optimalsoln(num):
    result = []
    for i in range(1,int(sqrt(num) +1)):
        if num % i == 0:
            result.append(i)
            if num//i !=i:
                result.append(num//i)
    result.sort()
    return result

print(optimalsoln(num))