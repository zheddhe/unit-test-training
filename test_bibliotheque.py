from bibliotheque import Livre, Bibliotheque
import pytest

@pytest.fixture
def livre1():
    return Livre("Fondation", "Asimov")

@pytest.fixture
def livre2():
    return Livre("Les Robots", "Asimov")

@pytest.fixture
def livre3():
    return Livre("Les 3 mousquetaires", "Alexandre Dumas")

@pytest.fixture
def bibl_vide():
    '''Retourne une instance Bibliotheque vide'''
    return Bibliotheque()

@pytest.fixture
def bibl_non_vide(livre1, livre2, livre3):
    '''Retourne une instance Bibliotheque contenant 3 livres'''
    bibliotheque = Bibliotheque()
    bibliotheque.ajouter_livre(livre1.titre, livre1.auteur)
    bibliotheque.ajouter_livre(livre2.titre, livre2.auteur)
    bibliotheque.ajouter_livre(livre3.titre, livre3.auteur)
    return bibliotheque

def test_ajouter_livre(bibl_vide, livre1, livre2, livre3):
    bibl_vide.ajouter_livre(livre1.titre, livre1.auteur)
    bibl_vide.ajouter_livre(livre2.titre, livre2.auteur)
    bibl_vide.ajouter_livre(livre3.titre, livre3.auteur)
    assert bibl_vide.lister_livre() == [(livre1.titre, livre1.auteur),
                                        (livre2.titre, livre2.auteur),
                                        (livre3.titre, livre3.auteur)] 

@pytest.mark.parametrize(
    "titre_suppr, livres_attendus",
    [
        ("Les 3 mousquetaires", [("Fondation", "Asimov"), ("Les Robots", "Asimov")]),
        ("Fondation", [("Les Robots", "Asimov"), ("Les 3 mousquetaires", "Alexandre Dumas")]),
    ]
)
def test_supprimer_livre(bibl_non_vide, titre_suppr, livres_attendus):
    bibl_non_vide.supprimer_livre(titre_suppr)
    assert bibl_non_vide.lister_livre() == livres_attendus

def test_lister_livre(bibl_non_vide, livre1, livre2, livre3):
    assert bibl_non_vide.lister_livre() == [(livre1.titre, livre1.auteur),
                                            (livre2.titre, livre2.auteur),
                                            (livre3.titre, livre3.auteur)]

# NB : le decorateur parametrize est évalué avant les fixtures donc le code suivant ne pourrait pas fonctionner
# @pytest.mark.parametrize(
#     "auteur, livres_attendus",
#     [
#         ("Asimov", [livre1, livre2]),
#         ("Alexandre Dumas", [livre3]),
#     ]
# )
# def test_rechercher_livre_auteur(bibl_non_vide, auteur, livres_attendus):
#     assert bibl_non_vide.rechercher_livre_auteur(auteur) == [(livre.auteur, livre.titre) for livre in livres_attendus]

@pytest.mark.parametrize(
    "auteur, livres_attendus",
    [
        ("Asimov", [("Fondation", "Asimov"), ("Les Robots", "Asimov")]),
        ("Alexandre Dumas", [("Les 3 mousquetaires", "Alexandre Dumas")]),
    ]
)
def test_rechercher_livre_auteur(bibl_non_vide, auteur, livres_attendus):
    assert bibl_non_vide.rechercher_livre_auteur(auteur) == livres_attendus

def test_generation_stat(bibl_non_vide):
    assert bibl_non_vide.generation_stat() == {
        'nombre_livres': 3,
        'auteurs_uniques': {'Asimov', 'Alexandre Dumas'},
    }

