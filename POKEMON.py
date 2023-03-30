import random
import _random
from Menu import *
from Type import *
from Fight import *

class Pokemon:
    def __init__(self, nom, Hp, attack, defense):
        self.__nom = nom
        self.__Hp = Hp
        self.attack = attack 
        self.defense = defense 

    def set_nom(self, nom):
        self.__nom = nom

    def get_nom(self):
        return self.__nom

    def set_Hp(self, points):
        self.__Hp = points

    def get_Hp(self):
        return self.__Hp
    
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

