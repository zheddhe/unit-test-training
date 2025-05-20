from code1 import total

def test_total () :
    # Vérifie le fonctionnement de base :
    a = total([1, 2 ,3]) == 6

    # Vérifie que la somme marche avec un nombre négatif et un positif :
    b = total([1, -1]) == 0

    # Vérifie que la somme marche avec deux négatifs :
    c = total([-1, -1]) == -2

    # Vérifie que la somme marche avec un seul élément :
    d = total([1]) == 1

    # Vérifie que la liste vide renvoie bien 0 :
    e = total([]) == 0

    return (a, b, c, d, e)

print(test_total())