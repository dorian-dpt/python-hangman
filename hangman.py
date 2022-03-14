# Jeu du Pendu (qui marche cette fois)
class Pendu:
    
    def __init__(self, mot:str):
        '''Crée le jeu à partir du mot entré en argument.'''
        self.liste_lettres = [lettre.capitalize() for lettre in mot] # Liste des lettres du mot
        self.trouve = ["_"]*len(self.liste_lettres) # Liste des lettres trouvées
        self.mauvaises_lettres = [] # Liste des mauvaises lettres
        self.essais = 11 # Nombre d'essais
        self.alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                         'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] # Lettres valides
        for caracter in self.liste_lettres:
            assert caracter in self.alphabet, "Merci de n'utiliser que des lettres sans accents et sans caractères spéciaux."
        self.play() # Lance le jeu automatiquement
        
    
    def statut_du_jeu(self):
        '''Affiche le statut actuel du jeu.'''
        print("--------------------------------")
        print("Lettres trouvées :", "".join(self.trouve),"\n")
        print("Mauvaises lettres :", " ".join(self.mauvaises_lettres))
        print("Essais restants :",str(self.essais),"\n")
    
    
    def verification(self, proposition:str):
        '''Vérifie que la lettre proposée soit correcte.'''
        
        lettre = proposition.capitalize() # Miniscule > Majuscule
        
        if lettre not in self.alphabet: # Si la proposition n'est pas une lettre de l'alphabet
            print("--------------------------------")
            return print("Ta proposition n'est pas valide.")
        
        elif len(lettre) != 1: # Vérifie que la proposition ne contient qu'une seule lettre
            print("--------------------------------")
            return print("Tu ne peux proposer qu'une seule lettre à la fois.")
        
        elif lettre in self.trouve: # Lettre déjà trouvée
            print("--------------------------------")
            return print("Lettre déjà trouvée !")
        
        elif lettre in self.mauvaises_lettres: # Lettre fausse et déjà proposée
            print("--------------------------------")
            return print("Déjà proposé, et faux !")
        
        elif lettre in self.liste_lettres: # Bonne lettre
            print("--------------------------------")
            print("Correct !")
            for i in range(len(self.liste_lettres)):
                if self.liste_lettres[i] == lettre:
                    self.trouve[i] = lettre
                    
        else: # Mauvaise lettre
            print("--------------------------------")
            print("Eh non !")
            self.essais -= 1
            self.mauvaises_lettres.append(lettre)
    
    
    def play(self):
        '''Permet de lancer le jeu.'''
        end = False
        while end == False:
        
            if self.essais == 0: # Si le nombre d'essais est nul (défaite)
                print("--------------------------------")
                print("Perdu, c'était","".join(self.liste_lettres))
                end = True
                
            elif self.liste_lettres == self.trouve: # Si le mot a été trouvé (victoire)
                print("--------------------------------")
                print("Gagné ! Le mot était bien","".join(self.liste_lettres),"!")
                end = True
                
            else: # Déroulement du jeu
                self.statut_du_jeu()
                self.verification(input("Propose une lettre ! "))


game = Pendu(input("Bienvenue dans le jeu du Pendu ! Donne moi un mot ! : ")) # Crée une nouvelle partie
