chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769

money = int(input())

if money >= sheep:
    num = money // sheep
    print("%d sheep" % num)
elif money >= cow:
    num = money // cow
    if num > 1:
        print("%d cows" % num)
    else:
        print("1 cow")
elif money >= pig:
    num = money // pig
    if num > 1:
        print("%d pigs" % num)
    else:
        print("1 pig")
elif money >= goat:
    num = money // goat
    if num > 1:
        print("%d goats" % num)
    else:
        print("1 goat")
elif money >= chicken:
    num = money // chicken
    if num > 1:
        print("%d chickens" % num)
    else:
        print("1 chicken")
else:
    print("None")
