class Pizza:
    nom = ""
    ingredients = ""
    prix = 0.0
    vegetarienne = False

    def __init__(self, nom, ingredient, prix, vegetarienne):
        self.nom = nom
        self.ingredients = ingredient
        self.prix=prix
        self.vegetarienne=vegetarienne

    def get_dictionary(self):

        return {"nom": self.nom,
                 "ingredients": self.ingredients,
                 "prix": self.prix,
                 "vegetarienne": self.vegetarienne
                }
