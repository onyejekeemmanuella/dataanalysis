# for i in "ella":
#     print(i)
# for i in range (100):
#     print(i)
for i in range (1,201):
    if i % 3== 0 and i % 5 == 0:
        print(f"{i} is fizzbuzz")
    elif i % 3 == 0:
        print(f"{i} is fizz")
    elif i % 5 == 0:
        print(f"{i} is buzz")
    else:
        print(i)
        