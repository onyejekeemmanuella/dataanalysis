for a in range (1,500):
    if a % 7==0 and a % 11==0:
        print(f"{a} is ellachi")
    elif a % 7==0:
        print(f"{a} is ella")
    elif a % 11 ==0:
        print(f"{a} is chi")
    else:
        print(a)