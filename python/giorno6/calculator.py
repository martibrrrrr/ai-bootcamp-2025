print("Welcome to the calculator. \nAdd your operation as shown: \na + b \na - b \na * b \na / b \nWrite 'quit' to close the calculator")
while True:

    text = input(">>> ").strip()
    if text.lower() == "quit":
        print("Bye Bye!")
        break
    try:
        a, b, c = text.split()
        a, c = int(a), int(c)
        if b == "+":
            result = a + c
            print(result)
        elif b == "-":
            result = a - c
            print(result)
        elif b == "*":
            result = a * c
            print(result)
        elif b == ":" or b == "/":
            if c == 0:
                print("Impossible: Division for zero!") #raise ZeroDivisionError("Division for zero")
            else:
                result = a / c
                print(result)
    except ValueError as e:
        print(f"Be sure to put a space between the operators. Write 'quit' to close the program ")
