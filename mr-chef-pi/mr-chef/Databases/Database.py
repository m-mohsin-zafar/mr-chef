import MySQLdb as db

class Database:

    def open_dbconneciton(self, database):
        return db.connect("localhost", "root", "root", database)


    def insert_recipe(self, connection, data):
        cur = connection.cursor()
        query = "insert into recipe_tb (name,ingredients,utensils,instructions) values (%s,%s,%s,%s)"
        try:
            cur.execute(query,data)
            connection.commit()
            return True
        except ConnectionError:
            connection.rollback()
        return False

    def get_recipe(self, connection, recipe_name):
        cur = connection.cursor()
        try:
            cur.execute("select instructions from recipe_tb where name='{}'".format(recipe_name))
            result = cur.fetchall()
        except ConnectionError:
            connection.rollback()
        if result is not None:
            return result
        else:
            return None

    def get_recipe_ingredients(self, connection, recipe_name):
        cur = connection.cursor()
        try:
            cur.execute("select ingredients from recipe_tb where name='{}'".format(recipe_name))
            result = cur.fetchall()
        except ConnectionError:
            connection.rollback()
        if result is not None:
            return result
        else:
            return None

    def get_recipe_utensils(self, connection, recipe_name):
        cur = connection.cursor()
        try:
            cur.execute("select utensils from recipe_tb where name='{}'".format(recipe_name))
            result = cur.fetchall()
        except ConnectionError:
            connection.rollback()
        if result is not None:
            return result
        else:
            return None

    def get_ingredients_angles(self,connection,name):
        cur = connection.cursor()
        try:
            cur.execute("select angles from ingredients_tb where name='{}'".format(name))
            result = cur.fetchall()
        except ConnectionError:
            connection.rollback()
        if result is not None:
            return result[0]

    def get_crockery_angles(self, connection, name):
        cur = connection.cursor()
        try:
            cur.execute("select angles from crockery_tb where name='{}'".format(name))
            result = cur.fetchall()
        except ConnectionError:
            connection.rollback()
        if result is not None:
            return result[0]

    def close_dbconnection(self, connection):
        connection.close()
