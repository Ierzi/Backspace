# Import Modules
import time, random



# Connnexion to the account

name = input("Inisialisation du panel de commande Python, veuillez entrer votre nom: ")
password = input("Veuillez rentrez votre mot de passe: ")

# Initialization
time.sleep(3)
print("Initialisation du panel de commande Python terminé. Redirection automatique vers le menu.")
time.sleep(0.5)




# Program Loop
while True : 
    # Asking For A Command
    commande = input("Panel De Commande Python, Veuillez Entrez Votre Commande: ")


    if commande == "quit" :
    # Quitting The Control Panel
        quit()

    # OPS
    if commande == "calcul" :
        # Type of Operations
        time.sleep(2)
        calcultype = input("Quel type de calcul ? Addition ou soustraction (A ou S) ? ")
        if calcultype == "A" :
            # Addition: Asking For The Numbers
            time.sleep(1)
            a = int(input("Quel est ton premier nombre ? "))
            b = int(input("Quel est ton deuxième nombre ? "))
            # Result
            result = a + b 
            print("Le résultat est: ", result)
            

        if calcultype == "S" :
            # Soustraction: Asking For The Numbers
            time.sleep(1)
            a = int(input("Quel est ton premier nombre ? "))
            b = int(input("Quel est ton deuxième nombre ? "))
            # Result
            result = a - b
            print("Le résultat est: ", result)
            


    # Settings Command
    if commande == "Settings" :
        time.sleep(2)

        # Checking The Password
        passworkcheck = input("Bienvenue dans les paramètres utilisateurs. Veuillez entrez votre mot de passe aveant de continuer: ")
        if passworkcheck == password :
            # Password Checked
            commandesettings = input("Que voulez-vous changez dans l'application Settings ?  ")
            if commandesettings == "quit" :
                # Quitting The Program
                pass
            
            if commandesettings == "password" :
                
                #Changing The Password
                changingpassword = input("Voulez-vous changez de mot de passe ? Y = Oui, N = Non  ")
                
                # Changing The Password: Conditions
                if changingpassword == "Y" :
                    password = input("Ecris ici ton nouveau mot de passe: ")
                    print("Changement du mot de passe effectué ! Redirection vers le menu du panel de commande Python.")

                else : 
                    if changingpassword == "N" :
                        print("Redirection automatique vers le menu du panel de commande Python...")
                        time.sleep(1)

                    else :
                        print("Settings Error. Wrong User Input.")
                        time.sleep(1)

        else :
            # Wrong Password
            print("Settings Error. Wrong Passwword.")
            time.sleep(1)





    # About The Control Panel
    if commande == "About" :
        print("Le Panel De Commande Python est un panel de commande à usage multiple depuis la v2.0 ! Crée par Ierzi le 03/05/2023.")
 

    # Control Panel Version
    if commande == "versions" or commande == "v" or commande == "ver" :
        print("PDCP v2.3 BETA - DC Update - 05/05/2023")

    # Game1: The Guesses Game
    if commande == "The Random Game" or commande == "The Guesses Game" or commande == "game1" or commande == "Game1":
        randomnum = random.randint(1, 20)
        tries = 0
        is_playerwongame1 = False

        # Commentator Speech
        print("Bienvenue ",name," dans le jeu de la chance !")
        time.sleep(1)
        print("Je vais penser à un nombre entre 1 et 20 et tu dois essayer de le deviner !")
        
        # Asking for the tries
        tries = int(input("Combien veux-tu d'essais ?  "))
        
        # Game Starts: Game Loop
        while tries != 0  and is_playerwongame1 == False :
            guess = int(input("Entre ici ton choix: "))
            tries -= 1
        
            if guess == randomnum :
                # Win
                print("Tu as gagné !")
                is_playerwongame1 = True
                is_askingforcommand = True
            else :
                if guess < randomnum :
                    # Too Low
                    print("Trop petit !")
                else: 
                    # Too High
                    print("Trop Grand !")
        else :
            # Ran Out Of Tries
            if tries == 0 : 
                print("Tu n'as plus d'essais ! Dommage ! Le nombre était ", randomnum)
                





    # Rock Paper Scissors
    if commande == "game2" or commande == "Game2" or commande == "PFC" or commande == "PPC" :
        # Game Options and Init'
        ppcoptions = ["Pierre", "Papier", "Ciseaux"]
        PPCuserchoice = 0
        
        # Computer Logic
        PPCcomputer = random.choice(ppcoptions)

        # User Choice
        PPCchoisetransfer = input("Pierre (R), Papier (P) ou ciseaux (S) ?  ")
    
        if PPCchoisetransfer == "R" :
            PPCuserchoice = "Pierre"
        if PPCchoisetransfer == "P" :
            PPCuserchoice = "Papier"  
        if  PPCchoisetransfer == "S" :
            PPCuserchoice == "Ciseaux"
        
        # Show computer's choice and user's choice
        print("L'ordinateur à choisi ", PPCcomputer)
        print("Vous avez choisi ", PPCuserchoice)

        time.sleep(2)

        # Decide Who Won
        if PPCuserchoice == "Pierre" and PPCcomputer == "Ciseaux" :
            print("Vous avez gagné !")
        elif PPCuserchoice == "Ciseaux" and PPCcomputer == "Papier" :
            print("Vous avez gagné !")
        elif PPCuserchoice == "Papier" and PPCcomputer == "Pierre" :
            print("Vous avez gagné !")
        elif PPCuserchoice == PPCcomputer :
            print("Egalité !")
        else:
            print("L'ordinateur a gagné !")

        # Return To The Menu (automatically)


    # Simple Random Number Generator Program

    if commande == "RNG" :
        RNGnum = random.randint(1, 100)
        print(RNGnum)





    # The Restaurant Game (Biggest Game So Far)

    if commande == "Restaurant Game" or commande == "Game 3" or commande == "game3" or commande == "g3" :
        time.sleep(2)

        # Restaurant Name
        print("Beinvenue dans le jeu du restaurant !")
        g3_resname = input("Comment veux-tu apeller ton restaurant ? ")
        
        time.sleep(2)

        # First recepie
        print("Pour commencer à avoir des clients dans ton restaurant, tu dois créer des recettes")
        g3_recette1 = input("Comment veux-tu nommer ta première recette ? ")
        
        # Ingredients in the recepie
        time.sleep(2)

        print("Il y aura 3 ingrédients dans ta recette :")
        g3_ing1r1 = input("Quel est le premier ingrédient de cette recette? ")
        g3_ing2r1 = input("Quel est le deuxième élément de cette recette ? ")
        g3_ing3r1 = input("Quel est le dernier ingrédient de cette recette ? ")

        # Recepie Price 
        time.sleep(2)

        g3_prixr1 = int(input("Quel sera le prix de cette recette ? "))
        
        # Getting the money
        if g3_prixr1 > 20 :
            print("Le prix est trop élevé ! Attention à vos ventes !")
            time.sleep(3)
            print("Vous avez votre première cliente ! Elle a acheté votre ", g3_recette1, " et n'a rien payé car le prix était trop élevé...")
            g3_money = 0

        elif g3_prixr1 > 10 :
            time.sleep(3)
            print("Vous avez votre première cliente ! Elle a acheté votre ", g3_recette1, " et vous a donné ", g3_prixr1, " !")
            g3_money = g3_prixr1
        else:
            print("Vous avez votre première cliente ! Elle a acheté votre ", g3_recette1, " et vous a donné ", g3_prixr1, " et même un pourboire de 5 !" )
            g3_money = g3_prixr1 + 5

        # Showing User's Money
        print("Vous avez actuellement: ", g3_money)
        time.sleep(0.2)
        print("Pensez à gardez un oeil sur cet argent !")

        time.sleep(2)

        # Asking User To Do Something + Game Loop For After The Tutorial
        is_askingforcommandg3 = True
        
        while is_askingforcommandg3 == True :
            print("Que voulez-vous faire ? Tapez R pour créer une nouvelle recette, S pour voir son argent, P pour changez le prix d'une recette et W pour attendre les clients (Q pour quitter)")
            g3_todo = input()
            is_askingforcommandg3 = False

            # Quit Game
            if g3_todo == "Q" :
                is_askingforcommand = True
        
            # Wait For The Custormers
            if g3_todo == "W" :
                g3_customerswhenwait = random.randint(1, 2)

                # Random and Loop
                g3_typeofcustomers = ["Une cliente", "Un client"]
                g3_customersmeal = [g3_recette1]


                while g3_customerswhenwait != 0 :

                    g3_rtoctophrase = random.choice(g3_typeofcustomers)
                    g3_cmtophrase = random.choice(g3_customersmeal)
                    g3_waitmoney = random.randint(1, g3_prixr1)

                    print(g3_rtoctophrase, "a acheté ", g3_cmtophrase, " et vous avez gagné ", g3_waitmoney, ".")
                    g3_customerswhenwait -= 1
                    g3_money += g3_waitmoney 
                    time.sleep(0.5)

                    if g3_customerswhenwait == 0 :
                        is_askingforcommandg3 = True
            
            
            # See User's Money
            if g3_todo == "S" :
                print("Vous avez actuellement ", g3_money, ".")
                is_askingforcommandg3 = True


    # I WILL CONTINUE THE CODE HERE AFTER

    # Lucky Number Finder

    if commande == "Divin Chanceux" or commande == "DC" or commande == "Game 4" or commande == "game4" or commande == "g4" :

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
        
        

    
    # Commands Examples

    if commande == "Exemples de commande" or commande == "EDC" or commande == "edc" :
        
        # Choosing a Random Command

        edc_random = ["game1, game2, game3, g4, settings, quit, versions, about"]
        edc_text = random.choice(edc_random)

        # Print the Random Command
        print(edc_text)
