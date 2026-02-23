airtime_balance=200.23
data_balance='100mb'
code = input("Enter ussd code: ")
if code=="*312#":
    code=input("select\n 1)daily\n 2)monthly\n 3)weekly\n choose: ") 
    if code=="1":
        code=input("select\n 1)#100 for 100mb\n 2)#200 for 230mb\n 3)#350 for 500mb\n choose: ") 
        if code=="1":
            print("100mb purchases was successful")
        elif code == "2":
            print("230mb purchases was successful")
        elif code == "3":
            print("500mb purchases was successful")
        
    elif code=="2":
        code=input("select\n 1) \n 2)monthly\n 3)weekly\n choose: ") 

    elif code=="3":
        print("you have selected weekly")
    else :
        print("unavailable")
elif code=="*323#":
    print(f"your data balance is {data_balance}")
elif code=="*310#":
    print(f"your airtime balance is {airtime_balance}")
else : 
    print("invalid ussd code")
