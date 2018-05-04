from Databases import Database as db
if __name__ == '__main__':
    database = db.Database()
    conn = database.open_dbconneciton("mr-chef-db")
    database.insert_recipe(conn, "hi", "hi", "hi", "hi")
