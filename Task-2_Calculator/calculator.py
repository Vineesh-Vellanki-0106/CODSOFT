def calculator():
    while True:
        print("SIMPLE CALCULATOR")
        print("Select Operation: ")
        print("1. ADDITION(+)")
        print("2. SUBTRACTION(-)")
        print("3. MULTIPLICATION(*)")
        print("4. DIVISION(/)")
        print("5. FLOOR DIVISION(//)")
        print("6. EXIT THE CALCULATOR")

        choice=input("Enter your choice:(1/2/3/4/5/6) ")
        num1 =float(input("Enter first number: "))
        num2 =float(input("Enter second number: "))

        if choice=="1":
            result=num1+num2
            print("Result of ADDITION: ",result)
        elif choice=="2":
            result=num1-num2
            print("Result of SUBTRACTION: ",result)
        elif choice=="3":
            result=num1*num2
            print("Result of MULTIPLICATION: ",result)
        elif choice=="4":
            if num2==0:
                print("Division by 0 is undefined and not allowed")
            else:
                result=num1/num2
                print("Result of DIVISION: ",result)
        elif choice=="5":
            if num2==0:
                print("Division by 0 is undefined and not allowed")
            else:
                result=num1//num2
                print("Result of FLOOR DIVIISON: ",result)
        elif choice=="6":
            print("Exiting the Calculator...Thank you!")
            break
        else:
            print("Invalid Choice. Please select a valid operation.")

if __name__ == "__main__":
    calculator()

