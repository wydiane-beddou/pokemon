import random
import sys

class Pokemon:
    def __init__(self, nom, hp, attack, defense):
        self.nom = nom
        self.hp = hp
        self.max_hp = hp
        self.attack = attack 
        self.defense = defense 
    
    def affichage(self):
        print(f"{self.nom}: {self.hp} HP | {self.attack} ATK | {self.defense} DEF")    
    def joueur(self,nom, hp):
        self.pokemon1.nom = self.nom
        self.pokemon2.nom = self.nom
def jouer(self):
    tour = 1
    print("Début du combat entre {} et {}".format(self.pokemon1.nom, self.pokemon2.nom))
    while not self.est_fini():
        print("Tour {}".format(tour))
        print("{} : {} / {} hp".format(self.pokemon1.nom, self.pokemon1.hp, self.pokemon1.max_hp))
        print("{} : {} / {} hp".format(self.pokemon2.nom, self.pokemon2.hp, self.pokemon2.max_hp))
        if tour % 2 == 1:
            self.attaque(self.pokemon1, self.pokemon2)
            print("{} attaque {}".format(self.pokemon1.nom, self.pokemon2.nom))
        else:
            self.attaque(self.pokemon2, self.pokemon1)
            print("{} attaque {}".format(self.pokemon2.nom, self.pokemon1.nom))
        tour += 1
    
    print("Le combat est terminé !")
    vainqueur = self.nom_vainqueur()
    if vainqueur is not None:
        print("{} remporte la victoire !".format(vainqueur))
    else:
        print("Match nul !")

def nom_perdant(self):
    vainqueur = self.nom_vainqueur()
    if vainqueur == self.pokemon1.nom:
        return self.pokemon2.nom
    elif vainqueur == self.pokemon2.nom:
        return self.pokemon1.nom
    else:
        return None

def est_fini(self):
    return self.hp <= 0 or self.hp <= 0

def nom_vainqueur(self):
    if self.pokemon1.hp > 0:
        return self.pokemon1.nom
    elif self.pokemon2.hp > 0:
        return self.pokemon2.nom
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
        return self.pokemon1.hp <= 0 or self.pokemon2.hp <= 0
    
   
def quit(self):
    print("Au revoir !")
    sys.exit(0)

def start_game(self):
    while True:
        print("Choisissez le Pokémon du Joueur 1:")
        print("1. Miaouss")
        print("2. Salameche")
        print("3. Carapuce")
        print("4. Taupiqueur")
        choice1 = input("Entrez le numéro de votre choix: ")
        if choice1 not in ["1", "2", "3", "4"]:
            print("Choix invalide, veuillez entrer un numéro valide.")
            continue
        break
    
    while True:
        print("Choisissez le Pokémon du Joueur 2:")
        print("1. Miaouss")
        print("2. Salameche")
        print("3. Carapuce")
        print("4. Taupiqueur")
        choice2 = input("Entrez le numéro de votre choix: ")
        if choice2 not in ["1", "2", "3", "4"]:
            print("Choix invalide, veuillez entrer un numéro valide.")
            continue
        break
    
    pokemon1 = None
    pokemon2 = None
    
    if choice1 == "1":
        pokemon1 = Normal("Miaouss")
    elif choice1 == "2":
        pokemon1 = Feu("Salameche")
    elif choice1 == "3":
        pokemon1 = Eau("Carapuce")
    elif choice1 == "4":
        pokemon1 = Terre("Taupiqueur")

    if choice2 == "1":
        pokemon2 = Normal("Miaouss")
    elif choice2 == "2":
        pokemon2 = Feu("Salameche")
    elif choice2 == "3":
        pokemon2 = Eau("Carapuce")
    elif choice2 == "4":
        pokemon2 = Terre("Taupiqueur")
    
combat = Combat(pokemon1, pokemon2)
combat.jouer()


start_game()

