class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, titre, auteur):
        livre = Livre(titre, auteur)
        self.livres.append(livre)

    def supprimer_livre(self, titre):
        self.livres = [livre for livre in self.livres if livre.titre != titre]

    def lister_livre(self):
        return [(livre.titre, livre.auteur) for livre in self.livres]

    def rechercher_livre_auteur(self, auteur):
        return [(livre.titre, livre.auteur) for livre in self.livres if livre.auteur == auteur]

    def generation_stat(self):
        nombre_livres = len(self.livres)
        auteurs_uniques = set(livre.auteur for livre in self.livres)
        return {
            'nombre_livres': nombre_livres,
            'auteurs_uniques': auteurs_uniques,
        }