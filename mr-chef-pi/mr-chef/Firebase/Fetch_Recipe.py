from firebase import firebase as fb
from ast import literal_eval


class fetchRecipe:

    def __init__(self,url):
        try:
            self.conn = fb.FirebaseApplication(url, None)
        except ConnectionError:
            print("Firebase could not connect!")

    def fetch_recipe(self,recipe_name):
        try:
            return self.conn.get(recipe_name, None)
        except ConnectionRefusedError:
            print("Could not get recipe!")

    def get_recipe(self, recipe_name):
        recipe = self.fetch_recipe("Recipes/{}".format(recipe_name))
        ingredients = ""
        instructions = ""
        utensils = ""
        result = ()
        result+=(recipe_name,)
        for x in range(len(recipe['ingredients'])):
            if x != len(recipe['ingredients'])-1:
                ingredients += "{},".format(recipe['ingredients']["ing_{:02}".format(x+1)])
            else:
                ingredients += "{}".format(recipe['ingredients']["ing_{:02}".format(x+1)])
        result+=(ingredients,)
        for x in range(len(recipe['utensils'])):
            if x != len(recipe['utensils'])-1:
                utensils += "{},".format(recipe['utensils']["ute_{:02}".format(x+1)])
            else:
                utensils += "{}".format(recipe['utensils']["ute_{:02}".format(x+1)])
        result += (utensils,)
        for x in range(len(recipe['instructions'])):
            if x!=len(recipe['instructions'])-1:
                instructions += "{},".format(recipe['instructions']["ins_{:02}".format(x+1)])
            else:
                instructions += "{}".format(recipe['instructions']["ins_{:02}".format(x+1)])
        result += (instructions,)
        if(ingredients is not None and utensils is not None and instructions is not None):
            return result
        else:
            return None
