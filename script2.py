

code = '1234'
entered_code = input("Enter your code : ")

if entered_code != code:
    for i in range(0,3):
        print("\nInvalid Code!!!")
        entered_code = input("Enter your code : ")
    print("Account Blocked !!!")
else:
    print("Access Granted")