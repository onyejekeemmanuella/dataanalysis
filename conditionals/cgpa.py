cgpa =float(input("enter cgpa: "))

if cgpa >= 4.5 and cgpa<=5.0:
    print("you are a first class student") 

elif cgpa>=3.5 and cgpa<= 4.49:
    print("second class upper student")
elif cgpa>=2.5 and cgpa<= 3.49:
    print("second class lower student")
elif cgpa >= 5.0 or cgpa < 1:
    print("invalid cgpa") 
 
else:
    print("you are a failure")
    
    


