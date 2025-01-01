# lst = [10,20,30,40,50]
# ast = {10,20,30,40,50}
# bst = (10,20,30,40,50)
# product = 1
# for ele in lst:
#     product*=ele
# print ("product is {}".format(product))

# for i in range(10):
#     print("baby",i)

# for i in range(1,20,2):
#     print("me tera",i)

index1 = 10
index2 = 50
print("prime no. between {0} and {1} are : ".format(index1,index2))

for num in range (index1,index2+1):
    if num>1:
        isDivisible = False
        for index in range (2,num):
            if num % index == 0:
                isDivisible=True
        if not isDivisible:
            print(num)