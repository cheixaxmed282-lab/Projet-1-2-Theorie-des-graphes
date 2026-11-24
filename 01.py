from collections import deque  # Importe deque, une file efficace pour ajouter et retirer des éléments.

graphe = {  # Représente le graphe sous forme de dictionnaire d'adjacence.
    "A": ["B", "C"],  # Depuis A, on peut aller vers B et C.
    "B": ["A", "D", "E"],  # Depuis B, on peut aller vers A, D et E.
    "C": ["A", "F"],  # Depuis C, on peut aller vers A et F.
    "D": ["B"],  # Depuis D, on peut aller vers B.
    "E": ["B", "F"],  # Depuis E, on peut aller vers B et F.
    "F": ["C", "E"]  # Depuis F, on peut aller vers C et E.
}  # Termine la définition du graphe.

def bfs(graphe, depart):  # Définit le parcours en largeur à partir du sommet de départ.
    visites = set()  # Crée un ensemble pour retenir les sommets déjà visités.
    file = deque([depart])  # Initialise une file deque avec le sommet de départ.
    visites.add(depart)  # Marque le sommet de départ comme déjà visité.

    while file:  # Continue tant que la file contient des sommets à traiter.
        sommet = file.popleft()  # Retire le premier sommet entré dans la file.
        print(sommet)  # Affiche le sommet traité.

        for voisin in graphe[sommet]:  # Parcourt les voisins du sommet actuel.
            if voisin not in visites:  # Vérifie si le voisin n'a pas encore été visité.
                visites.add(voisin)  # Marque le voisin comme visité.
                file.append(voisin)  # Ajoute le voisin à la fin de la file.

def dfs(graphe, depart):  # Définit le parcours en profondeur à partir du sommet de départ.
    visites = set()  # Crée un ensemble pour retenir les sommets déjà visités.
    pile = deque([depart])  # Initialise une pile deque avec le sommet de départ.

    while pile:  # Continue tant que la pile contient des sommets à traiter.
        sommet = pile.pop()  # Retire le dernier sommet ajouté à la pile.
        if sommet not in visites:  # Vérifie si ce sommet n'a pas encore été visité.
            visites.add(sommet)  # Marque le sommet comme visité.
            print(sommet)  # Affiche le sommet traité.

            for voisin in reversed(graphe[sommet]):  # Parcourt les voisins en ordre inverse.
                if voisin not in visites:  # Vérifie si le voisin n'a pas encore été visité.
                    pile.append(voisin)  # Ajoute le voisin sur la pile pour le traiter ensuite.

print("Parcours BFS :")  # Affiche un titre avant le parcours en largeur.
bfs(graphe, "A")  # Lance le BFS à partir du sommet A.

print("Parcours DFS :")  # Affiche un titre avant le parcours en profondeur.
dfs(graphe, "A")  # Lance le DFS à partir du sommet A.
