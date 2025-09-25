#Name: Siyaa Sathyan
#UID : 433004781
"""
Let the sides be side1, side2 and side3
"""
side1 = int(input("Enter the first number"))
side2= int(input("Enter the second number"))
side3 = int(input("Enter the third number"))
"""
the function is defined as triangle_validator
"""
def triangle_validator():
    if side1 + side2==side3:
        print("True , side1 + side2 = side3")
    elif side2 + side3==side2:
        print("True , side2 + side3 = side2")
    elif side3 + side2==side1:
        print("True , side3 + side2 = side1")
    else:
        print("False")
def main():
    triangle_validator()
main()
