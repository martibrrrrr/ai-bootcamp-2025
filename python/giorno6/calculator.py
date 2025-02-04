import re #modulo per espressioni regolari - regex

print("Welcome to the calculator. \nAdd your operation as shown: \na + b \na - b \na * b \na / b \nWrite 'quit' to close the calculator")
while True:
    text = input(">>> ").strip().lower()

    if text == "quit":
        print("Bye Bye!")
        break
    match = re.search(r"(-?\d+)\s*([+\-*/x:])\s*(-?\d+)", text)
    #search cerca una corrispondenza ovunque nella stringa: num-operatore-num
    #match cerca una corrispondenza all'inizio della stringa:  num-operatore-num
    #PATTERN:
    #() nuovo elemento
    #-? per indicare anche i numeri negativi
    #\d+ indica i numeri da 0 a 9 (+ incrementa le unità in decine e centinaia etc)
    #\s* se presente uno spazio
    #[+\-*/:] indico gli operatori disponibili \- è per rappresentare il -

    if match: #se match diverso da None
        a, op, c = match.groups() #.groups: estrae il valore catturato dalla regex
        # se voglio usare text, uno la funzione text.split() per separare il testo con gli spazi
        a, c = int(a), int(c)
        if op == "+":
            print(a + c)
        elif op == "-":
            print(a - c)
        elif op == "*" or op == "x":
            print(a * c)
        elif op == ":" or op == "/":
            if c == 0:
                print("Impossible: Division for zero!") #raise ZeroDivisionError("Division for zero")
            else:
                print(a / c)
    else:
        print(f"Invalid format. \nUse the format a + b (or a+b). \nWrite 'quit' to exit. ")
