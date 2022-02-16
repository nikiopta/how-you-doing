name = input("hi what your name? ")
print("hi", name)
yd = input("how you doing? (only good or not good!) ")
if yd == "good":
    print("nice to hear!")
    input()
    exit(0)
if yd == "not good":
    print("sorry to hear!")
    df = input("do you have friends? (yes or no only!) ")
    if df == "no":
        print("sorry to hear")
        bf = input("do you wanna be friends? (yes or no only!) ")
        if bf == "no":
            print("why not? but i hope tomorrow i am going to see you bey bey")
            input()
            exit(0)
        if bf == "yes":
            print("so we going meet tomorrow!")
            print("we now bff!")
            input()
            exit(0)
    if df == "yes":
        af = input("do you angry at them? (yes or no only!) ")
        if af == "yes":
            print("so do something you love its make you happy!")
            input()
            exit(0)
        if af == "no":
            print("why you don't spend time with them? the going to make you happy!")
            input()
        exit(0)
