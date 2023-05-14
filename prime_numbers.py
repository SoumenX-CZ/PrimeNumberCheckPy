num = int(input("Číslo: "))

flag = False

if num == 1:
    print(num, "není prvočíslo")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            
            flag = True
            
            break

    if flag:
        print(num, "není prvočíslo")
    else:
        print(num, "je prvočíslo")