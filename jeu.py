class Creature:
    def __init__(self, nom, pv, resistance):
        self.nom = nom
        self.points_de_vie = pv
        self.resistance = resistance

    def attaquer(self, cible):
        degats = self.arme.degats if hasattr(self, 'arme') else 0
        degats -= cible.resistance
        if degats < 0:
            degats = 0
        cible.points_de_vie -= degats
        print(f"{self.nom} attaque {cible.nom} et lui inflige {degats} points de dégâts.")


class Personnage(Creature):
    def __init__(self, nom, pv, resistance):
        super().__init__(nom, pv, resistance)
        self.arme = None

    def choisir_arme(self, arme):
        self.arme = arme
        print(f"{self.nom} a choisi l'arme : {self.arme.nom}")


class Monstre(Creature):
    def __init__(self, nom, pv, resistance, cri):
        super().__init__(nom, pv, resistance)
        self.cri = cri

    def rugir(self):
        print(f"{self.nom} rugit : {self.cri}")


class Arme:
    def __init__(self, nom, degats):
        self.nom = nom
        self.degats = degats


def demander_nombre_personnages():
    while True:
        try:
            nombre = int(input("Combien de personnages vont combattre ? "))
            if nombre > 0:
                return nombre
            else:
                print("Veuillez entrer un nombre positif.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")


def selectionner_personnages(liste_personnages):
    for i in range(len(liste_personnages)):
        print(f"{i+1}. {liste_personnages[i].nom}")
    choix = input("Choisissez un personnage par son numéro : ")
    try:
        choix = int(choix) - 1
        if 0 <= choix < len(liste_personnages):
            return liste_personnages[choix]
        else:
            print("Choix invalide.")
            return selectionner_personnages(liste_personnages)
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        return selectionner_personnages(liste_personnages)


def selectionner_arme(liste_armes):
    for i in range(len(liste_armes)):
        print(f"{i+1}. {liste_armes[i].nom} (Dégâts : {liste_armes[i].degats})")
    choix = input("Choisissez une arme par son numéro : ")
    try:
        choix = int(choix) - 1
        if 0 <= choix < len(liste_armes):
            return liste_armes[choix]
        else:
            print("Choix invalide.")
            return selectionner_arme(liste_armes)
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        return selectionner_arme(liste_armes)


def combat(personnage, monstre):
    while personnage.points_de_vie > 0 and monstre.points_de_vie > 0:
        personnage.attaquer(monstre)
        if monstre.points_de_vie > 0:
            monstre.attaquer(personnage)
    if personnage.points_de_vie > 0:
        print(f"{personnage.nom} a vaincu {monstre.nom}!")
    else:
        print(f"{monstre.nom} a vaincu {personnage.nom}!")


# Création de quelques personnages et armes
personnages_disponibles = [
    Personnage("Guerrier", 100, 10),
    Personnage("Mage", 80, 5),
    Personnage("Archer", 90, 7)
]

armes_disponibles = [
    Arme("Épée", 20),
    Arme("Bâton", 15),
    Arme("Arc", 18)
]

monstres_disponible = [
Monstre ("Dragon",120, 25, "roooar") ,
Monstre("Ogre", 125, 20 , "j'ai faiiiiiiiim"),
Monstre("Minotaure", 110, 15, "meuuuuh"),
Monstre("Gobelin", 50, 5, "Grrr!")
]

# Accueil de l'utilisateur
nombre_personnages = demander_nombre_personnages()
personnages = []


for i in range(nombre_personnages):
    print(f"\nSélection du personnage {i+1}:")
    personnage = selectionner_personnages(personnages_disponibles)
    print(f"\nSélection de l'arme pour {personnage.nom}:")
    arme = selectionner_arme(armes_disponibles)
    personnage.choisir_arme(arme)
    personnages.append(personnage)

# Affichage des personnages sélectionnés
print("\nPersonnages sélectionnés :")
for p in personnages:
    print(f"{p.nom} avec {p.arme.nom} (Dégâts : {p.arme.degats})")

# Exemple de combat
monstre = Monstre("Gobelin", 50, 5, "Grrr!")
print("\nUn monstre apparaît :")
monstre.rugir()

for personnage in personnages:
    print(f"\nCombat entre {personnage.nom} et {monstre.nom} :")
    combat(personnage, monstre)
    if monstre.points_de_vie <= 0:
        print("Le monstre est vaincu !")
    if personnage.points_de_vie <= 0:
        print("le personnage est vaincu")
        break
