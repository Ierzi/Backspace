import time
import random

prefix = "g."

def number():
    

    # Explainations

    print("Bienvenue dans le jeu du Divin Chanceux !")
    time.sleep(3)
    print(" Je vais penser à un nombre entre 1 et 20 et tu dois donner un nombre plus petit que celui là !")
    time.sleep(3)
    print("Le problème est que tu ne connais pas le nombre !")
    input()

    # Choosing a random number between 1 and 20

    g4_number= random.randint(1, 20)

    g4_usernumber = int(input("Tape ton nombre ici : "))


    # Show The Numbers

    print("Vous avez choisi : ", g4_usernumber)
    print("J'ai choisi : ", g4_number)

    # Winning Conditions

    if g4_usernumber > g4_number :
        print("J'ai gagné ! Bien joué !")
    elif g4_number == g4_usernumber :
        print("Personne n'a gagné, c'est une égalité...")
    elif g4_number > g4_usernumber :
        print("Tu as gagné ! Bravo ! ")
        
        