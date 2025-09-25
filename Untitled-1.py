def countdown(number):
    total = 0
    while number >= 0:
        print(number)
        total+=number
        number-=1
    return total
def main():
    num = int(input("Enter the number:"))
    result= countdown (num)
    print("The sum of the countdown number is", result)
main()
