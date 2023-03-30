import random
from Fight import *

class Pokemon:
    def __init__(self, nom, hp, attack, defense):
        self.__nom = nom
        self.__hp = hp
        self.attack = attack 
        self.defense = defense 
    
    def affichage(self):
        print(f"{self.__nom}: {self.__hp} HP | {self.attack} ATK | {self.defense} DEF")    
    
    def get_nom(self):
        return self.__nom
    
    def get_hp(self):
        return self.__hp
    
    def set_nom(self, nom):
        self.__nom = nom

    def set_hp(self, points):
        self.__hp = points

    
    def jouer(self):
        tour = 1
        print("Début du combat entre {} et {}".format(self.pokemon1.nom, self.pokemon2.nom))
        while not self.est_fini():
            print("Tour {}".format(tour))
            print("{} : {} / {} hp".format(self.pokemon1.__nom, self.pokemon1.__hp, self.pokemon1.max__hp))
            print("{} : {} / {} hp".format(self.pokemon2.__nom, self.pokemon2.__hp, self.pokemon2.max__hp))
            if tour % 2 == 1:
                self.attaque(self.pokemon1, self.pokemon2)
                print("{} attaque {}".format(self.pokemon1.__nom, self.pokemon2.__nom))
            else:
                self.attaque(self.pokemon2, self.pokemon1)
                print("{} attaque {}".format(self.pokemon2.__nom, self.pokemon1.__nom))
            tour += 1
        
        print("Le combat est terminé !")
        vainqueur = self.nom_vainqueur()
        if vainqueur is not None:
            print("{} remporte la victoire !".format(vainqueur))
        else:
            print("Match nul !")

    def nom_perdant(self):
        vainqueur = self.nom_vainqueur()
        if vainqueur == self.pokemon1.__nom:
            return self.pokemon2.__nom
        elif vainqueur == self.pokemon2.__nom:
            return self.pokemon1.__nom
        else:
            return None


    
class Normal(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, hp=80, attack=45, defense=35)

class Feu(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, hp=90, attack=70, defense=30)

class Eau(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, hp=100, attack=40, defense=60)

class Terre(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, hp=90, attack=60, defense=40)

Miaouss = Normal("Miaouss")
Salameche = Feu("Salameche")
Carapuce = Eau("Carapuce")
Taupiqueur = Terre("Taupiqueur")

for pokemon in [Miaouss, Salameche, Carapuce, Taupiqueur]:
    pokemon.affichage()

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
    
    def est_fini(self):
        return self.pokemon1.__hp <= 0 or self.pokemon2.hp <= 0
    
    def nom_vainqueur(self):
        if self.pokemon1.__hp > 0:
            return self.pokemon1.__nom
        elif self.pokemon2.__hp > 0:
            return self.pokemon2.__nom
        else:
            return None
    
    def type_efficace(self, attaquant, defenseur):
        if isinstance(attaquant, Eau):
            if isinstance(defenseur, Eau):
                return 1 
            elif isinstance(defenseur, Feu):
                return 2
            elif isinstance(defenseur, Terre):
                return 1
            else:
                return 1
        elif isinstance(attaquant, Feu):
            if isinstance(defenseur, Eau):
                return 0.5
            elif isinstance(defenseur, Feu):
                return 1
            elif isinstance(defenseur, Terre):
                return 2
            else:
                return 1
        elif isinstance(attaquant, Terre):
            if isinstance(defenseur, Eau):
                return 2
            elif isinstance(defenseur, Feu):
                return 0.5
            elif isinstance(defenseur, Terre):
                return 1
            else:
                return 1
        else:
            if isinstance(defenseur, Eau):
                return 0.75
            elif isinstance(defenseur, Feu):
                return 0.75
            elif isinstance(defenseur, Terre):
                return 0.75
            else:
                return 1
    
    def attaque(self, attaquant, defenseur):
        type_efficace = self.type_efficace(attaquant, defenseur)
        dommages = (attaquant.attack * type_efficace) - defenseur.defense
        defenseur.__hp = max(0, defenseur.__hp - dommages)
    
    
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
        exit(0)

menu = Menu()
menu.display_menu()
menu.start_game()
