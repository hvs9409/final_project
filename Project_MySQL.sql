CREATE DATABASE product_db;
USE product_db;

CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100) NOT NULL, price DECIMAL(10,2) NOT NULL, stock INT NOT NULL, date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

INSERT INTO products (name, price, stock) VALUES ('Laptop', 799.99, 10);
INSERT INTO products (name, price, stock) VALUES ('Desktop', 29.99, 90);
INSERT INTO products (name, price, stock) VALUES ('Mouse', 19.99, 50);
INSERT INTO products (name, price, stock) VALUES ('Keyboard', 49.99, 30);

SELECT * FROM products;