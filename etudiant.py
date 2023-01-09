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


def afficherOption(liste):
    print("Vous etes sur la liste suivant :")
    print(liste.afficher()) 
    print("Tapez 1 pour ajouter")
    print("Tapez 2 pour inserer")
    print("Tapez 3 pour inverser")
    print("Tapez 4 pour supprimer un element")
    print("Tapez 5 pour obtenir la promotion finale")
    
def option1():
    nom = input("Saisissez le nom de votre etudiant :\n")
    prenom = input("Saisissez le prenom de votre etudiant :\n")
    id = input("Saisissez l'id de votre etudiant :\n")
    moy = input("Saisissez la moyenne de votre etudiant :\n")
    etudiant = Etudiant(nom=nom, prenom=prenom, numero_carte=id, moyenne=moy)
    return etudiant

def option2():
    print("Cette option va enregistrer l'etudiant a une position pour etre dans l'ordre")
    nom = input("Saisissez le nom de votre etudiant : ")
    prenom = input("Saisissez le prenom de votre etudiant :")
    id = input("Saisissez l'id de votre etudiant : ")
    moy = input("Saisissez la moyenne de votre etudiant : ")
    etudiant = Etudiant(nom=nom, prenom=prenom, numero_carte=id, moyenne=moy)
    return etudiant

def option3(liste):
    print("La liste a été inversée")
    liste.inverser()
    liste.afficher()
    
def option4(liste):
    liste.afficher
    result = input("Saisissez l'id de l'etudiant a supprimer : ")
    return result

def option5(liste):
    print("La liste a été mise a jour. Voici la nouvelle liste avec que les admis")
    liste.afficher()    
    

def main():
    continuer = True
    liste = ListeChainee()
    while continuer == True:
        print("---------------------------")
        afficherOption(liste)
        option = input("Je choisis l'option : ")
        if option == "1" :
            result = option1()
            liste.ajout(result)
        elif option == "2" :
            result = option2()
            liste.inserer(result)
        elif option == "3" :
            option3(liste)
        elif option == "4" :
            result = option4()
            liste.supprimer(result)
        elif option == "5" :
            liste.PromoFinale()
            option5(liste)
        
        response = input("Voulez vous continuer ? (y/n) :")
        while response != "y" and response != "n" :
            print("Reponse incorrecte")
            response = input("Voulez vous continuer ? (y/n) :")
        if response == "y" :
            continuer = True
        elif response == "n" :
            continuer = False
    print("Activité terminée !!!")
    
main()