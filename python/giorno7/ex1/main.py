import random
import json
from datetime import datetime

#import high score
def upload_high_score():
    with open("high_scores.json","r") as fd:
        return json.loads(fd)
#save high score
def save_high_score(high_score):
    with open("high_scores.json","w") as fd:
        json.dumps(high_score,fd,indent=4)
def f():
    return f[1]

def indovina_numero():
    high_score = upload_high_score()
    print("Welcome in the game 'Guess the number!' ")
    print("I choose a number between 1 and 100. Try to guess it!")
    numero_da_indovinare = random.randint(1, 100)
    tentativo = 0
    while True:
        try:
            num_input = int(input("Guess the number"))
        except ValueError:
            print("Input Error. Try again")
            continue
        tentativo +=1
        if num_input < numero_da_indovinare:
            print("Too low!")
        elif num_input > numero_da_indovinare:
            print("Too high!")
        elif num_input == numero_da_indovinare:
            print(f"Good Job! You guessed in {tentativo} trials")

            if len(high_score) == 0 or tentativo<high_score[0]["trials"]:
                name = input("New record!! Please enter your nickname:")
                high_score.append({
                    "name" : name,
                    "trials" : tentativo,
                    "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            high_score = sorted(high_score, key=f)

            play_again = input("Do you wanna play again? (yes/no)").strip().lower()
            if play_again == "no":
                print("See you next time!")
                print(f"The winner is {high_score[0]['name']}-{high_score[0]['trials']} trials on {high_score[0]['data']}")
                save_high_score(high_score)
                return  #break
            else:
                print("let's play again")
                numero_da_indovinare = random.randint(1, 100)
                tentativo= 0

indovina_numero()
