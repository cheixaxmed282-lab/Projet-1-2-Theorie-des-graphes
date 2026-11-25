from collections import deque

def bfs(graphe, depart):
    visites = {depart}
    file = deque([depart])
    ordre = []

    while file:
        sommet = file.popleft()
        ordre.append(sommet)

        for voisin in graphe[sommet]:
            if voisin not in visites:
                visites.add(voisin)
                file.append(voisin)

    return ordre

def dfs(graphe, depart):
    visites = {depart}
    pile = [depart]
    ordre = []

    while pile:
        sommet = pile.pop()
        ordre.append(sommet)

        # On inverse les voisins pour les visiter dans l’ordre indiqué
        for voisin in reversed(graphe[sommet]):
            if voisin not in visites:
                visites.add(voisin)
                pile.append(voisin)

    return ordre


# Exemple 1 : graphe en forme de branches
graphe1 = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

# Exemple 2 : graphe avec un cycle
graphe2 = {
    "G": ["H", "I"],
    "H": ["G", "J"],
    "I": ["G", "J"],
    "J": ["H", "I", "K"],
    "K": ["J"]
}


# Exécution des deux algorithmes sur chaque graphe
for numero, graphe, depart in [
    (1, graphe1, "A"),
    (2, graphe2, "G")
]:
    print(f"\nGraphe {numero} — départ du sommet {depart}")
    print("BFS :", bfs(graphe, depart))
    print("DFS :", dfs(graphe, depart))
