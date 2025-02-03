#1. Indovina il numero tra 1 e 100!
#2. se l'utente non indovina il gioco deve dire se l'input è alto o basso rispetto a quello da indovinare
#3. il gioco deve gestire input errato comunicandolo al giocatore

#indovina il numero tra 1 e 100!
#?67
#Troppo alto
#?ciao
#input errato.Riprova
#?30
#Hai indovinato! Tentativi:2

import random
def indovina_numero():
    numero_da_indovinare = random.randint(1,100)
    tentativo = 0
    print("Benvenuto nel gioco 'Indovina il numero!'")
    print("Ho pensato ad un numero tra 1 e 100. Prova ad indovinare!")
    while True:
        try:
            num_input = int(input("Inserisci il numero"))
            tentativo +=1
           # if num_input.isnumeric():

            if num_input < numero_da_indovinare:
                print("Troppo basso!")
            elif num_input > numero_da_indovinare:
                print("Troppo alto!")
            elif num_input == numero_da_indovinare:
                print(f"Bravissimo! Hai indovinato in {tentativo} tentativi")
                break
        except ValueError:
            print("Input Error.Riprova")
            #continue

indovina_numero()

#if type(int("msfj")) == int #????

#"ciao".isnumeric()



"""
def indovina_numero():
    numero_da_indovinare = random.randint(1,100)
    tentativo = 0
    print("Benvenuto nel gioco 'Indovina il numero!'")
    print("Ho pensato ad un numero tra 1 e 100. Prova ad indovinare!")
    while True:
        try:
            num_input = int(input("Inserisci il numero"))
        except ValueError:
            print("Input Error.Riprova")
            continue
        tentativo +=1
        if num_input < numero_da_indovinare:
            print("Troppo basso!")
        elif num_input > numero_da_indovinare:
            print("Troppo alto!")
        elif num_input == numero_da_indovinare:
            print(f"Bravissimo! Hai indovinato in {tentativo} tentativi")
            break"""