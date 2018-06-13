from Databases import Database as db


class Recipe_Loader:
    instructions = ""
    ing_angles = {}
    utn_angles = {}

    def __init__(self):
        self.database = db.Database()
        self.conn = None

    def load_recipe(self, recipe_name):
        print("Loading Recipe from Database...")
        self.conn = self.database.open_dbconneciton("mr-chef-db")
        instr = self.database.get_recipe(self.conn, recipe_name)
        if instr.__len__() != 0:
            self.instructions = instr[0]
        else:
            print("Recipe Not Found!")
            return
        ingredients = self.database.get_recipe_ingredients(self.conn, recipe_name)[0]
        utensils = self.database.get_recipe_utensils(self.conn, recipe_name)[0]
        # print("Inst: {}\nIngre: {}\nUtensils: {}".format(self.instructions, self.ingredients, self.utensils))
        self.load_angles(ingredients, utensils)
        self.database.close_dbconnection(self.conn)

    def load_angles(self, ingredients, utensils):
        ings = str(ingredients[0]).split(",")
        for x in range(ings.__len__()):
            self.ing_angles[ings[x]] = self.database.get_ingredients_angles(self.conn, ings[x])[0]
        utens = str(utensils[0]).split(",")
        for x in range(utens.__len__()):
            if(utens[x] == "stove"):
                temp_angle = self.database.get_crockery_angles(self.conn, utens[x])[0]
                self.utn_angles['on']=temp_angle.split(';')[0]
                self.utn_angles['off']=temp_angle.split(';')[1]

            else:
                self.utn_angles[utens[x]] = self.database.get_crockery_angles(self.conn, utens[x])[0]
        # print(self.instructions)
        # print(self.ing_angles)
        # print(self.utn_angles)
