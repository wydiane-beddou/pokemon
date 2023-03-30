from Type import *
from POKEMON import *
from Fight import *
import random 


class Menu:
    def __init__(self):
        self.choices = {
            "1": self.start_game,
            "2": self.quit
        }
    
    def display_menu(self):
        print("""
        Bienvenue dans le jeu Pokemon !
        
        1. Lancer une partie
        2. Quitter
        """)

    def choisir_pokemon(self):
        print("Choisissez votre Pokémon :")
        print("1 - Miaouss")
        print("2 - Salameche")
        print("3 - Carapuce")
        print("4 - Taupiqueur")
        choix = input("Entrez le numéro correspondant au Pokémon que vous voulez choisir : ")
        if choix == "1":
            return Miaouss()
        elif choix == "2":
            return Salameche()
        elif choix == "3":
            return Carapuce()
        elif choix == "4":
            return Taupiqueur()
        else:
            print("Choix invalide")
            return self.choisir_pokemon()

    def start_game(self):
        pokemon1 = self.choisir_pokemon()
        nom_pokemon1 = input("Entrez le nom de votre premier Pokemon : ")
        type_pokemon1 = input("Entrez le type de votre premier Pokemon (normal, feu, eau, terre) : ")
        if type_pokemon1.lower() == "normal":
            pokemon1 = Normal(nom_pokemon1)
        elif type_pokemon1.lower() == "feu":
            pokemon1 = Feu(nom_pokemon1)
        elif type_pokemon1.lower() == "eau":
            pokemon1 = Eau(nom_pokemon1)
        elif type_pokemon1.lower() == "terre":
            pokemon1 = Terre(nom_pokemon1)
        else:
            print("Type de Pokemon invalide, veuillez réessayer.")
            return self.start_game()
    
        pokemon2 = random.choice([Miaouss(), Salameche(), Carapuce(), Taupiqueur()])
        
        combat = Combat(pokemon1, pokemon2)
        combat.jouer()
        
        perdant = combat.nom_perdant()
        if perdant == pokemon1.__nom:
            print("Dommage, vous avez perdu.")
        else:
            print("Félicitations, vous avez gagné !")

    def quit(self):
        print("Merci d'avoir joué !")
        sys.exit(0)
