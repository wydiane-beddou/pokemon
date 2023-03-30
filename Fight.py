import random
from Menu import *
from POKEMON import *
from Type import *

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
    
    def est_fini(self):
        return self.pokemon1.hp <= 0 or self.pokemon2.hp <= 0
    
    def nom_vainqueur(self):
        if self.pokemon1.hp > 0:
            return self.pokemon1.nom
        elif self.pokemon2.hp > 0:
            return self.pokemon2.nom
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
        defenseur.hp = max(0, defenseur.hp - dommages)
    
    