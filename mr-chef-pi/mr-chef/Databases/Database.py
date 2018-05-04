import MySQLdb as db

class Database:

    def open_dbconneciton(self, database):
        return db.connect("localhost", "root", "root", database)

    def create_table(self, connection, table_name, columns):
        cur = connection.cursor()
        query = "create table {} ({})".format(table_name,columns)
        try:
            cur.execute(query)
        except ConnectionError:
            connection.rollback()

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

    def show_records(self, connection, table_name):
        cur = connection.cursor()
        try:
            cur.execute("select * from {}".format(table_name))
            result = cur.fetchall()
        except ConnectionError:
            connection.rollback()
        if result is not None:
            return result
    def get_ingredients(self,connection,name):
        cur = connection.cursor()
        try:
            cur.execute("select angles from ingredients_tb where name='{}'".format(name))
            result = cur.fetchall()
        except ConnectionError:
            connection.rollback()
        if result is not None:
            return result[0]

    def get_crockery(self, connection, name):
        cur = connection.cursor()
        try:
            cur.execute("select angles from crockery_tb where name='{}'".format(name))
            result = cur.fetchall()
        except ConnectionError:
            connection.rollback()
        if result is not None:
            print(result)
            return result[0]

    def close_dbconnection(self, connection):
        connection.close()
