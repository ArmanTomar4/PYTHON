
num = int (input("enter the no. : "))
isDivisible=False
i=2
while i < num :
    if num % i == 0:
        isDivisible = True
        print ("{} is divisible with {}".format(num,i))
        break
    i += 1
if isDivisible:
    print ("{} is not prime no.".format(num))
else :
    print ("{} is a prime no.".format(num))