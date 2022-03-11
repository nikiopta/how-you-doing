while True:
    name = input("hi what your name? ")
    print("hi", name)
    yd = input("how you doing? (good or not good only!) ")
    if yd in ('good', 'not good'):
        break
if yd == "good":
    print("nice to hear,")
    print(name, "have a nice day!")
    input()
    exit(0)
if yd == "not good":
    print("sorry to hear!")
    input("what happen? ")
    hy = input("does something can help you? (yes or no) ")
    if hy == "yes":
        wis = input("what it is?")
        print("amm you can look it on google something like: how to", wis, "or something like that")
        print("happy to help", name)
        print("bey")
        input()
        exit(0)
    if hy == "no":
        print("its ok i recommend to [lzy some games talk to your friends or something like that its help me!")
        input()
        exit(0)
else:
    print("what do you want to say?")
    input()
    exit(0)