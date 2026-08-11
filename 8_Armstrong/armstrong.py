n = int(input("Enter Your no. :"))
total = 0
def armstrong():
    global total
    num = n
    no_of_digit = len(str(n))
    while num>0:
        last_digit = num%10
        total = total + (last_digit**no_of_digit)
        num = num//10

armstrong()


if total == n:
    print("No is Armstrong")
else:
    print("No. is not armstrong")

