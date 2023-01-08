class Etudiant:
    def __init__(self, nom, prenom, numero_carte, moyenne):
        self.nom = nom
        self.prenom = prenom
        self.numero_carte = numero_carte
        self.moyenne = moyenne
        self.suiv = None

class ListeChainee:
    def __init__(self):
        self.tete = None
        
    def afficher(self):
        current = self.tete
        while current is not None:
            print(f"Nom et prénoms : {current.nom} {current.prenom} / ID : {current.numero_carte} / Moyenne = {current.moyenne}")
            current = current.suiv

    def ajout(self, etudiant):
        new = Etudiant(etudiant.nom, etudiant.prenom, etudiant.numero_carte, etudiant.moyenne)
        new.suiv = self.tete
        self.tete = new
    
    def supprimer(self, numero_carte):
        current = self.tete
        etudiant_precedent = None
        # Recherche de l'étudiant à supprimer
        while current is not None and current.numero_carte != numero_carte:
            etudiant_precedent = current
            current = current.suiv
        # Si l'étudiant a été trouvé
        if current is not None:
            # Si l'étudiant à supprimer est en tête de liste
            if etudiant_precedent is None:
                self.tete = current.suiv

    #La fonction insère direcetement le new etudiant dans son emplacement par ordre alphabetique
    def inserer(self, etudiant):
        new = Etudiant(etudiant.nom, etudiant.prenom, etudiant.numero_carte, etudiant.moyenne)
        current = self.tete

        # Si la liste est vide ou que l'étudiant doit être inséré en tête de liste
        if current is None or current.nom > new.nom:
            new.suiv = current
            self.tete = new
        else:
            # Recherche de l'emplacement où insérer l'étudiant
            while current.suiv is not None and current.suiv.nom < new.nom:
                current = current.suiv
            new.suiv = current.suiv
            current.suiv = new

    #On inverse les elts de la liste en commencant par le dernier après l'avoir trier dans l'ordre avec l'algo de tri par fusion
    def inverser(self):
        self.Tri()
        etudiant_precedent = None
        current = self.tete
        while current is not None:
            etudiant_suiv = current.suiv
            current.suiv = etudiant_precedent
            etudiant_precedent = current
            current = etudiant_suiv
        self.tete = etudiant_precedent

    #Fonction de calcul des admis
    def PromoFinale(self):
        current = self.tete
        precedent = None
        while current is not None:
            if current.moyenne < 12:
                # Retirer l'étudiant de la liste chaînée
                if precedent is not None:
                    precedent.suiv = current.suiv
                else:
                    self.tete = current.suiv
            else:
                precedent = current
            current = current.suiv
            
    def Tri(self):
        # On recupere et mettre les instances d'Etudiants dans une liste
        elements = []
        current = self.tete
        while current is not None:
            elements.append(current)
            current = current.suiv
        # Trier la liste dans l'ordre decroissant vue que c'est une liste chainée (pile)
        elements.sort(key=lambda x: x.nom, reverse=True)
        # Convertir notre liste en une liste chainée
        self.tete = elements[0]
        current = self.tete
        for i in range(1, len(elements)):
            current.suiv = elements[i]
            current = current.suiv
        current.suiv = None
        self.afficher()
        
        return self

    def fusion(self, liste):
        # Créer une nouvelle liste chaînée qui contiendra les éléments fusionnés
        nouvelle_liste = ListeChainee()
        queue = None

        # Parcourir les deux listes chaînées et ajouter chaque élément à la nouvelle liste
        courant1 = self.tete
        courant2 = liste.tete
        while courant1 is not None or courant2 is not None:
            if courant1 is not None:
                noeud = courant1
                courant1 = courant1.suiv
            elif courant2 is not None:
                noeud = courant2
                courant2 = courant2.suiv

            # Ajouter le nouveau noeud à la nouvelle liste
            if nouvelle_liste.tete is None:
                nouvelle_liste.tete = noeud
                queue = noeud
            else:
                queue.suiv = noeud
                queue = noeud
        return nouvelle_liste


liste = ListeChainee()

# Ajout d'un étudiant à la liste
etudiant1 = Etudiant("A", "1", 1, 16)
liste.ajout(etudiant1)

# Ajout d'un autre étudiant à la liste
etudiant2 = Etudiant("B", "2", 2, 12)
liste.ajout(etudiant2)

# Ajout d'un autre étudiant à la liste
etudiant3 = Etudiant("Luc", "G", 3, 11)
liste.ajout(etudiant3)

# Ajout d'un autre étudiant à la liste
etudiant4 = Etudiant("Boris", "T", 4, 13)
liste.ajout(etudiant4)

print("Liste initial : ")
liste.afficher()



# Inversion de la liste
liste.inverser()

# Affichage de la liste après inversion
print("\nAprès inversion:")
liste.afficher()

# Suppression d'un étudiant de la liste
liste.supprimer(1)

# Affichage de la liste après suppression
print("\nAprès suppression:")
liste.afficher()



print("\nAprès admission:")
liste.PromoFinale()
liste.afficher()
