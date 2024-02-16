# Import Modules
import time
import random
import getpass
import string
import os
import sys
import datetime

try:
    import colorama
    from colorama import Fore as Color
except ImportError:
    os.system("pip install colorama")
    import colorama
    from colorama import Fore as Color

# Important variables

__author__ = "Ierzi"
__version__ = "2.5"
__doc__ = "README.md"
__version_date__ = "14/02/2023"
__name__ = "Backspace"
__description__ = "A command panel made by Ierzi the 03/05/2023."

# Functions


def _recovery_keys():
    """
    This function is used to generate the recovery keys.
    """

    print("Creating your recovery keys...")
    if os.path.exists("saves/64chars/64characters_saves.txt"):
        os.remove("saves/64chars/64characters_saves.txt")

    with open("saves/64chars/64characters_saves.txt", "w") as save_file:
        for _ in range(10):
            string_save = ""
            for _ in range(64):
                string_save += random.choice(string.ascii_letters + string.digits)

            save_file.write(f"{string_save}\n")


# Initializing Colorama
colorama.init()

# Resetting the saved characters (saves/64chars/64characters_saves.txt)
# Without using a .bat file, we can delete the file and create a new one with the same name later.
# We prevent triggering an error by putting an if condition if the file doesn't exist.

if os.path.exists("saves/64chars/64characters_saves.txt"):
    os.remove("saves/64chars/64characters_saves.txt")


# Getting the user's name and password


# Connexion to the account

name = input(f"{Color.RESET}Backspace initialisation, please enter your name: ")
password = getpass.getpass("Please write your password: ")

_recovery_keys()

# Setting all the addons to a not downloaded state.
shortit_installed = False
games_installed = False

# Initialization
print(f"Backspace initialisation 100% complete. Welcome {name}!")
time.sleep(0.5)

# Program Loop
while True:
    # Asking For A Command
    commande = input(f"{Color.RESET}Please enter a command: ").strip().lower()

    # Installing optional modules
    if commande.startswith("install"):
        demanded_package = commande.lstrip("install").strip().lower()
        if demanded_package == "shortit":
            shortit_installed = True
            from addons import shortit
            print(f"{Color.GREEN}Sucessfully installed ShortIt!{Color.RESET}")
        elif demanded_package == "games":
            games_installed = True
            from addons import games
            print(f"{Color.GREEN}Sucessfully installed Games!{Color.RESET}")

    elif (commande.startswith("quit") or
            commande.startswith("exit") or commande.startswith("stop")
    ):
        # Quitting The Control Panel
        if commande.endswith(" --force"):
            # Nobody asked for a complicated exit as that
            sys.exit(random.seed(datetime.datetime.now().second * .42))

        print("Are you sure you want to quit?")
        print(f"{Color.RED}Yes (Y) \n{Color.GREEN}No (N){Color.RESET}")
        quit_confirmation = input("").lower().strip()

        if quit_confirmation == "y":
            print("Quitting...")
            sys.exit()
        else:
            print("Returning to the main menu...")
            time.sleep(1)
    # OPS
    elif commande == "calcul":
        # Type of Operations
        time.sleep(2)
        calcultype = input("Quel type de calcul ? Addition ou soustraction (A ou S) ? ")
        if calcultype == "A":
            # Addition: Asking For The Numbers
            time.sleep(1)
            a = int(input("Quel est ton premier nombre ? "))
            b = int(input("Quel est ton deuxième nombre ? "))
            # Result
            result = a + b 
            print("Le résultat est: ", result)
            
        if calcultype == "S":
            # Soustraction: Asking For The Numbers
            time.sleep(1)
            a = int(input("Quel est ton premier nombre ? "))
            b = int(input("Quel est ton deuxième nombre ? "))
            # Result
            result = a - b
            print("Le résultat est: ", result)

    # Settings Command
    elif commande == "settings":
        time.sleep(2)

        # Checking The Password
        passworkcheck = input("Welcome to the settings. Please enter your password.")
        if passworkcheck == password:
            # Password Checked
            commandesettings = input("What do you want to do ? Change the password (password) or quit (quit) ?")
            if commandesettings == "quit":
                # Quitting The Program
                pass
            
            if commandesettings == "password":
                
                # Changing The Password
                changingpassword = input(f"Change the password? \n {Color.GREEN}"
                                         f"Yes (Y) \n {Color.RED}"
                                         f"No (N) \n{Color.RESET}"
                ).upper().strip()
                
                # Changing The Password: Conditions
                if changingpassword == "Y":
                    password = input("New password: ")
                    print("Changing password...")
                    _recovery_keys()
                    print("Password changed successfully.")

                else:
                    if changingpassword == "N":
                        print("Returning to the main menu...")
                        time.sleep(1)

                    else:
                        print("Settings Error. Wrong User Input.")
                        time.sleep(1)

        else:
            # Wrong Password
            print("Settings Error. Wrong Passwword.")
            time.sleep(1)

    # About The Control Panel
    elif commande == "about":
        print("Backspace is a command panel made by Ierzi the 03/05/2023. "
              "It includes various commands like calcul, settings, about, versions, game1, game2, game3, g4, quit. "
              "You can also use the EDC command to get an example of a command."
        )
 
    # Control Panel Version
    elif (commande.startswith("versions") or commande.startswith("version") or commande.startswith("ver") or
            commande.startswith("v")):
        print("PDCP v2.5 - SHortIt! - 14/02/24")
        if commande.endswith(" --message"):
            print("Added the ShortIt addon.")

    # Game1: The Guesses Game
    elif commande == "The Random Game" or commande == "The Guesses Game" or commande == "game1" or commande == "g1":
        randomnum = random.randint(1, 20)
        tries: int = 0
        is_playerwongame1 = False

        # Commentator Speech
        print("Bienvenue ", name, " dans le jeu de la chance !")
        time.sleep(1)
        print("Je vais penser à un nombre entre 1 et 20 et tu dois essayer de le deviner !")
        
        # Asking for the tries
        tries = int(input("Combien veux-tu d'essais ?  "))

        # Game Starts: Game Loop
        while tries != 0 and not is_playerwongame1:
            guess = int(input("Entre ici ton choix: "))
            tries -= 1

            if guess == randomnum:
                # Win
                print("Tu as gagné !")
                is_playerwongame1 = True
                is_askingforcommand = True
            else:
                if guess < randomnum:
                    # Too Low
                    print("Trop petit !")
                else: 
                    # Too High
                    print("Trop Grand !")
        else:
            # Ran Out Of Tries
            if tries == 0:
                print("Tu n'as plus d'essais ! Dommage ! Le nombre était ", randomnum)

    # Rock Paper Scissors
    elif commande == "game2" or commande == "Game2" or commande == "PFC" or commande == "PPC":
        # Game Options and Init
        ppcoptions = ["Pierre", "Papier", "Ciseaux"]
        PPCuserchoice = 0
        
        # Computer Logic
        PPCcomputer = random.choice(ppcoptions)

        # User Choice
        PPCchoisetransfer = input("Pierre (R), Papier (P) ou ciseaux (S) ?  ")
    
        if PPCchoisetransfer == "R":
            PPCuserchoice = "Pierre"
        if PPCchoisetransfer == "P":
            PPCuserchoice = "Papier"  
        if PPCchoisetransfer == "S":
            PPCuserchoice = "Ciseaux"
        
        # Show computer's choice and user's choice
        print("L'ordinateur à choisi ", PPCcomputer)
        print("Vous avez choisi ", PPCuserchoice)

        time.sleep(2)

        # Decide Who Won
        if PPCuserchoice == "Pierre" and PPCcomputer == "Ciseaux":
            print("Vous avez gagné !")
        elif PPCuserchoice == "Ciseaux" and PPCcomputer == "Papier":
            print("Vous avez gagné !")
        elif PPCuserchoice == "Papier" and PPCcomputer == "Pierre":
            print("Vous avez gagné !")
        elif PPCuserchoice == PPCcomputer:
            print("Egalité !")
        else:
            print("L'ordinateur a gagné !")

        # Return To The Menu (automatically)

    # Simple Random Number Generator Program
    elif commande == "RNG":
        RNGnum = random.randint(1, 100)
        print(RNGnum)

    # The Restaurant Game (Biggest Game So Far)
    elif commande == "Restaurant Game" or commande == "Game 3" or commande == "game3" or commande == "g3":
        time.sleep(2)

        # Restaurant Name
        print("Beinvenue dans le jeu du restaurant !")
        g3_resname = input("Comment veux-tu apeller ton restaurant ? ")
        
        time.sleep(2)

        # First recipie
        print("Pour commencer à avoir des clients dans ton restaurant, tu dois créer des recettes")
        g3_recette1 = input("Comment veux-tu nommer ta première recette ? ")
        
        # Ingredients in the recipie
        time.sleep(2)

        print("Il y aura 3 ingrédients dans ta recette :")
        g3_ing1r1 = input("Quel est le premier ingrédient de cette recette? ")
        g3_ing2r1 = input("Quel est le deuxième élément de cette recette ? ")
        g3_ing3r1 = input("Quel est le dernier ingrédient de cette recette ? ")

        # Recepie Price 
        time.sleep(2)

        g3_prixr1 = int(input("Quel sera le prix de cette recette ? "))
        
        # Getting the money
        if g3_prixr1 > 20:
            print("Le prix est trop élevé ! Attention à vos ventes !")
            time.sleep(3)
            print("Vous avez votre première cliente ! Elle a acheté votre ", g3_recette1,
                  " et n'a rien payé car le prix était trop élevé...")
            g3_money = 0

        elif g3_prixr1 > 10:
            time.sleep(3)
            print("Vous avez votre première cliente ! Elle a acheté votre ", g3_recette1,
                  " et vous a donné ", g3_prixr1, " !")
            g3_money = g3_prixr1
        else:
            print("Vous avez votre première cliente ! Elle a acheté votre ", g3_recette1,
                  " et vous a donné ", g3_prixr1, " et même un pourboire de 5 !")
            g3_money = g3_prixr1 + 5

        # Showing User's Money
        print("Vous avez actuellement: ", g3_money)
        time.sleep(0.2)
        print("Pensez à gardez un oeil sur cet argent !")

        time.sleep(2)

        # Asking User To Do Something + Game Loop For After The Tutorial
        is_askingforcommandg3 = True
        
        while is_askingforcommandg3:
            print("Que voulez-vous faire ? "
                  "Tapez R pour créer une nouvelle recette, "
                  "S pour voir son argent, "
                  "P pour changez le prix d'une recette et "
                  "W pour attendre les clients (Q pour quitter)"
                  )
            g3_todo = input()
            is_askingforcommandg3 = False

            # Quit Game
            if g3_todo == "Q":
                is_askingforcommand = True
        
            # Wait For The Custormers
            if g3_todo == "W":
                g3_customerswhenwait = random.randint(1, 2)

                # Random and Loop
                g3_typeofcustomers = ["Une cliente", "Un client"]
                g3_customersmeal = [g3_recette1]

                while g3_customerswhenwait != 0:

                    g3_rtoctophrase = random.choice(g3_typeofcustomers)
                    g3_cmtophrase = random.choice(g3_customersmeal)
                    g3_waitmoney = random.randint(1, g3_prixr1)

                    print(g3_rtoctophrase, "a acheté ", g3_cmtophrase, " et vous avez gagné ", g3_waitmoney, ".")
                    g3_customerswhenwait -= 1
                    g3_money += g3_waitmoney 
                    time.sleep(0.5)

                    if g3_customerswhenwait == 0:
                        is_askingforcommandg3 = True

            # See User's Money
            if g3_todo == "S":
                print("Vous avez actuellement ", g3_money, ".")
                is_askingforcommandg3 = True

    # I WILL CONTINUE THE CODE HERE AFTER

    # Lucky Number Finder

    # Commands Examples
    elif commande == "Exemples de commande" or commande == "EDC" or commande == "edc":
        
        # Choosing a Random Command

        edc_random = ["game1, game2, game3, g4, settings, quit, versions, about"]
        edc_text = random.choice(edc_random)

        # Print the Random Command
        print(edc_text)

    elif commande == "gettime" or commande == "gt":
        print(f"We are the {datetime.datetime.now().time()}")

    # The Addons Commands
    # See the "install" command

    # ShortIt!
    elif commande.startswith("shortit") or commande.startswith("s-it"):
        # Checks if we installed the shortit package
        if shortit_installed:
            # Strips the command and gets the link to shortify
            # Using the shortit extension, shorts it.
            link_to_shortify = commande.lstrip("shortit").strip().lower()
            shortit.short(link_to_shortify)
        else:
            print(f"{Color.RED}You didn't install the ShortIt package.")
            print(f'Please install it using the command "install shortit"{Color.RESET}')
