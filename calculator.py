try:
    a = int(input("Enter the first number : "))
    
    b = int(input("Enter the second number : "))
    
    print("Which operation do you want to perform? press  + for addition\npress - for substraction\npress * for multiply\npress / for divide")

    o = input("Enter oprestion : ")
    
    match o:
        case "+":
            print(f"The result is adding {a} + {b} : {a+b}")
        case "-":
                    print(f"The result is substring {a} - {b} : {a-b}")
        case "*":
                    print(f"The result is multiplying {a} * {b} : {a*b}")
        case "/":
                    print(f"The result is dividing {a} / {b} : {a/b}")
        case default:
            print(f"There was an error")
except ValueError:
    print("Please don't perform bad typecast")
except ZeroDivisionError:
    print("Hey Don't divide by 0")

    
except Exception as e:
    print("Enter a valid value of a and b ")