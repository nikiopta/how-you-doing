name = input("hi what your name? ")
print("hi", name)
yd = input("how you doing? (for best result say good or not good!) ")
if yd == "good" or yd == "awesome" or yd == "great":
    print("nice to hear,")
    print(name, "have a nice day!")
    input()
    exit(0)
if yd == "not good" or yd == "awful" or yd == "angry" or yd == "bad" or yd == "Negative":
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
