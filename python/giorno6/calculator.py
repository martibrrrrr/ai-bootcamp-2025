while True:
    text = input(">>> ").strip()
    if text.lower() == "quit":
        print("arrivederci")
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
                raise ZeroDivisionError("Divisione per zero")
            result = a / c
            print(result)
        else:
            print("Ti piacerebbbbbbbbbe")
    except ValueError as e:
        print(f"{type(e)}")
    except ZeroDivisionError as e:
        print(f"{type(e)}")
    except Exception as e:
        print(f"{type(e)} ---- OperZIONI NON SUPPORTATE")