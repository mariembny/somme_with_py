def somme_nb_pairs(liste):
    s = 0
    for nb in liste:
        if nb % 2 == 0:
            s += nb
    return s

liste_de_nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultat = somme_nb_pairs(liste_de_nombres)
print(f"La somme des nombres pairs dans la liste est : {resultat}")
