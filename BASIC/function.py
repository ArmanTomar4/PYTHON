# def sum():
#     '''
#     this is a function of addition
#     '''
#     return 1+1
# print(sum())
# print (sum.__doc__)


# def factorial(num):
#     '''
#     this function is for factorial 
#     '''
#     return 1 if num ==1 else (num*factorial(num-1))
# num=int(input("enter the number:"))
# print ("factorial of {0} is {1}".format(num,factorial(num)))


# lst=[1,2,3,4,5]
# new_lst=list(map(lambda x:x*2,lst))
# print (new_lst)
from functools import reduce
lst=[1,2,3,4,5]
new_lst=reduce(lambda x,y:x*y,lst)
print (new_lst)