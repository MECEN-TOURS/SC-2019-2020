"""
Bibliothèque contenant des fonctions abstraites de manipulation de graphes.
"""
from collections import deque

def transformation_voisinage(sommets, arretes):
    resultat = dict()
    for sommet in sommets:
        resultat[sommet] = list()
    for sommet1, sommet2 in arretes:
        resultat[sommet1].append(sommet2)
    return resultat

def transformation_ensembles(voisinage):
    sommets = list()
    arretes = list()
    for sommet, voisins in voisinage.items():
        sommets.append(sommet)
        for voisin in voisins:
            arretes.append((sommet, voisin))
    
    return sommets, arretes

def remonte_arbre(arbre, depart, arrivee):
    resultat = list()
    noeud_courant = arrivee
    while noeud_courant in arbre:
        resultat.append(noeud_courant)
        if noeud_courant == depart:
            resultat.reverse()
            return resultat
        noeud_courant = arbre[noeud_courant]
    raise ValueError("Pas de chemin")
    
def bfs(voisinage, depart, arrivee):
    """Breadth First Search"""
    visites = list()
    vus = deque()
    vus.append(depart)
    vus_part = dict()
    vus_part[depart] = None
    while vus:
        noeud_courant = vus.popleft()
        if not noeud_courant in visites:
            visites.append(noeud_courant)
            for voisin in voisinage[noeud_courant]:
                vus.append(voisin)
                if not voisin in vus_part:
                    vus_part[voisin] = noeud_courant

    return remonte_arbre(vus_part, depart, arrivee)

def dfs(voisinage, depart, arrivee):
    """Depth First Search"""
    visites = list()
    vus = list()
    vus.append(depart)
    vus_part = dict()
    vus_part[depart] = None
    while vus:
        noeud_courant = vus.pop()
        if not noeud_courant in visites:
            visites.append(noeud_courant)
            for voisin in voisinage[noeud_courant]:
                vus.append(voisin)
                if not voisin in vus_part:
                    vus_part[voisin] = noeud_courant

    return remonte_arbre(vus_part, depart, arrivee)