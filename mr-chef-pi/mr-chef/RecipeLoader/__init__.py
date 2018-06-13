from RecipeLoader import Loader
if __name__ == '__main__':
    recipe = Loader.Recipe_Loader()
    recipe.load_recipe('test_recipe')
    instructions = recipe.instructions[0].split(",")
    for x in range(instructions.__len__()):
        if instructions[x].split(" ")[0] == "add":
            print(recipe.ing_angles[instructions[x].split(" ")[1]].split(":"))
        elif instructions[x].split(" ")[0] == "switch" or instructions[x].split(" ")[0] == "place":
            print(recipe.utn_angles[instructions[x].split(" ")[1]].split(":"))
