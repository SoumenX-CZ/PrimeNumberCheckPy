#Number input
num = int(input("Number: "))

flag = False

if num == 1:
    print(num, "is not a prime number")
    
#Checking if it is a prime number
elif num > 1:
    #Basic for loop
    for i in range(2, num):
        if (num % i) == 0:
            
            flag = True
            
            break

    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
