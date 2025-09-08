# def good():
#     print("you are good in maths")
# good()



# def sum(a,b):
#     print(f"sum of a and b {a+b}")

# sum(7,5)


def palladromic(str):

    rev=""
    for i in range(len(str)-1,-1,-1):
        rev=rev+str[i]

    if rev==str:
        print(f"this a palladromic {rev}")
    else:
        print(f"this is not a palladromic {rev}")


palladromic("RAHUL")
palladromic("rohit")
   

   