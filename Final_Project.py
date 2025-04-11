import mysql.connector
from mysql.connector import Error


def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Reset123**',
            database='product_db'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None


def insert_product(name, price, stock):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        sql = "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)"
        values = (name, price, stock)
        cursor.execute(sql, values)
        connection.commit()
        print("Product inserted successfully.")
        cursor.close()
        connection.close()


def update_product(product_id, name, price, stock):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        sql = "UPDATE products SET name = %s, price = %s, stock = %s WHERE id = %s"
        values = (name, price, stock, product_id)
        cursor.execute(sql, values)
        connection.commit()
        print("Product updated successfully.")
        cursor.close()
        connection.close()


def delete_product(product_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        sql = "DELETE FROM products WHERE id = %s"
        values = (product_id,)
        cursor.execute(sql, values)
        connection.commit()
        print("Product deleted successfully.")
        cursor.close()
        connection.close()


def search_product(product_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        sql = "SELECT * FROM products WHERE id = %s"
        values = (product_id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        if result:
            print("Product Details:", result)
        else:
            print("Product not found.")
        cursor.close()
        connection.close()


def list_products():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        sql = "SELECT * FROM products"
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print(row)
        cursor.close()
        connection.close()

if __name__ == "__main__":
    while True:
        print("\nProduct Management System")
        print("1. Insert Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. Search Product")
        print("5. List Products")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            insert_product(name, price, stock)
        elif choice == '2':
            product_id = int(input("Enter product ID: "))
            name = input("Enter new product name: ")
            price = float(input("Enter new product price: "))
            stock = int(input("Enter new product stock: "))
            update_product(product_id, name, price, stock)
        elif choice == '3':
            product_id = int(input("Enter product ID: "))
            delete_product(product_id)
        elif choice == '4':
            product_id = int(input("Enter product ID: "))
            search_product(product_id)
        elif choice == '5':
            list_products()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
