#Number input
num = int(input("Number: "))

flag = False

#Defining one. One is not a prime number. Any other numbers are in a "for" loop.
if num == 1:
    print(num, "is not a prime number")
    
#Checking if it is a prime number
elif num > 1:
    #Basic "for" loop in range from 2 to the input number
    for i in range(2, num):
        if (num % i) == 0:
            
            flag = True
            
            break

    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
