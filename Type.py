
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