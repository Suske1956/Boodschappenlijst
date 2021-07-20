"""
This a collection of constants belonging to shopping_list.py.

sqlite constants:
Basically field names only are parametrized. since sqlite does not accept this for table names.
Using string formatting makes it possible to parametrize table names as well. For the time being string
formatting is not used: introduces an additional risk.
To be considered string formatting for getting data and maybe inserting or changing records.
"""

# sqlite constants
LIST_TABLES = """SELECT name FROM sqlite_master WHERE type='table';"""
PRODUCTS_GET_ONE_RECORD = """SELECT rowid, * from products WHERE rowid = ?"""
PRODUCTS_GET_ALL_RECORDS = """SELECT rowid, * FROM products"""
PRODUCTS_GET_RECORDS_WITH_QUANTITY = """SELECT rowid, * FROM products WHERE prod_required != 0"""
PRODUCTS_DELETE_ONE_RECORD = """DELETE FROM products WHERE rowid = ?"""
PRODUCTS_ADD_RECORD = """INSERT INTO products
                            (prod_name, prod_unit, prod_required)
                            VALUES (?, ?, ?);"""
PRODUCTS_DROP_TABLE = """DROP TABLE products"""
PRODUCTS_CREATE_TABLE = """CREATE TABLE products (
                            prod_name TEXT NOT NULL,
                            prod_unit text NOT NULL,
                            prod_required REAL);"""
PRODUCT_CHANGE_QUANTITY = """UPDATE products SET prod_required = ? where rowid = ?"""
SHOPS_DROP_TABLE = """DROP TABLE shops"""
SHOPS_CREATE_TABLE = """CREATE TABLE shops (
                            shop_name TEXT);"""
PROD_SHOP_DROP_TABLE = """DROP TABLE prod_shop"""
PROD_SHOP_CREATE_TABLE = """CREATE TABLE prod_shop (
                            prod_id INTEGER,
                            shop_id INTEGER,
                            prod_price REAL);"""
