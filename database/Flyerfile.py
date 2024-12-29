import mysql.connector

# Example scraped data
scraped_data = [
    {"name": "Bananas", "brand" : "dole", "price": 0.59, "oldPrice": 1.00, "discount": .4},
    {"name": "grapes", "brand" : "sunny", "price": 4.50, "oldPrice": 6.00, "discount": .2},
]


def insert_scraped_data(scraped_data):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="9qb3bk4g",
        database="itemDb"
    )

    mycursor = mydb.cursor()

    # mycursor.execute("SHOW DATABASES")
    # mycursor.execute("CREATE TABLE items (item_id INT UNSIGNED PRIMARY KEY, name VARCHAR(255) NOT NULL, brand VARCHAR(255), price DECIMAL(10, 2) NOT NULL, oldPrice DECIMAL(10,2) NOT NULL, discount NUMERIC (5,4) NOT NULL, UNIQUE (name, brand))")
    mycursor.execute("SHOW TABLES")

    for x in mycursor:
        print(x)
