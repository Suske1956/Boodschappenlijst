import sqlite3
import shopping_list_constants as constants


class GeneralFunctions:
    """
    GeneralMethods contains static functions:

    To exit the menu, without an error the static method stop() (without content) should be called.
    A function to list te products
    """

    @ staticmethod
    def menu(data):
        """
        Execute a simple cli menu. The parameter data is a dictionary containing the data required to build the menu.
        A typical example of such a dictionary:
            {   'title': 'Database Operations\n', 'options': [
                    {'title': 'Exit', 'function': self.stop},
                    {'title': 'List Tables,', 'function': self.list_tables},
                    {'title': 'Renew Tables', 'function': self.reset_database}
                ]}
        The title contains the menu title, printed at the top of the menu. The options contain the menu items.
        Each option consists of a title and a function.
        :param data: data type dictionary
        :return: nothing
        """
        number = len(data['options'])
        print(data['title'])
        count = 0
        for x in data['options']:
            print(count, '  ', x['title'])
            count += 1

        y = None
        while y != 0:
            try:
                y = int(input('Choose an option\n'))
            except ValueError:
                print('Input Error, integer required')
            else:
                if y < number:
                    data['options'][y]['function']()
                else:
                    print('Input Error, out of scope')
                print(data['title'])
                count = 0
                for x in data['options']:
                    print(count, '  ', x['title'])
                    count += 1

    @staticmethod
    def stop():
        """
        Empty function to stop the menu and return to the higher level.
        :return:
        """
        pass

    @staticmethod
    def list_products(db_name):
        """
        Returns a list of products
        :return:
        """
        conn = None
        try:
            conn = sqlite3.connect(db_name)
            c = conn.cursor()
            c.execute(constants.PRODUCTS_GET_ALL_RECORDS)
            records = c.fetchall()
            spaces = [0, 0, 0]
            print('\nrow id', ' ' * 10, 'Product Name', ' ' * 30, 'Unit', ' ' * 10, 'Quantity required')
            for row in records:
                spaces[0] = 16 - len(str(row[0]))
                spaces[1] = 42 - len(row[1])
                spaces[2] = 14 - len(row[2])
                print(row[0], ' ' * spaces[0], row[1][0:42], ' ' * spaces[1], row[2], ' ' * spaces[2], row[3])
            c.close()
        except sqlite3.Error as error:
            print('failed to read data ', error)
        finally:
            if conn:
                conn.close()
                print()


class ShoppingList:
    """
    ShoppingList is the main class basically it holds the main menu of the application and the name of the
    database
    Within ShoppingList subclasses DataBaseOperations, ProductMaintenance and ShoppingList exist. Each of them
    holds its own submenu and the operations belonging to the group of operations.
    For documentation regarding the cli menu see MenuExec
    todo: Consider one or a few try - except constructions to perform database operations, in class GeneralFunctions.
    todo: Next actions
        - populate sub class ShoppingList
        - add table for units in product maintenance
        - add shops and connect them with products.
    """

    class DataBaseOperations:
        """
        The class DataBaseOperations holds a method to list the tables in the database and one to renew
        the database tables, deleting all data.
        """
        def __init__(self, dbname):
            self.db_name = dbname
            self.general = GeneralFunctions
            self.menu_data = {
                'title': '\n   >>Database Operations', 'options': [
                    {'title': 'Exit', 'function': self.general.stop},
                    {'title': 'List Tables,', 'function': self.list_tables},
                    {'title': 'Renew Tables', 'function': self.reset_database}
                ]
            }

        def menu_db_opr(self):
            self.general.menu(self.menu_data)

        def list_tables(self):
            conn = None
            try:
                conn = sqlite3.connect(self.db_name)
                c = conn.cursor()
                c.execute(constants.LIST_TABLES)
                conn.commit()
                tables = (c.fetchall())
                print('\nList of tables:')
                for item in tables:
                    print(item[0])
                print('Press ENTER to continue')
                input()
                c.close()
            except sqlite3.Error as error:
                print("Error while listing tables", error)
            finally:
                if conn:
                    conn.close()

        def reset_database(self):
            answer = input('ATTENTION:\nAfter resetting the database all data will be lost \n'
                           'Do you want to continue? (yes/No\n')
            if answer.upper() == 'YES':
                conn = None
                try:
                    conn = sqlite3.connect(self.db_name)
                    c = conn.cursor()
                    c.execute(constants.PRODUCTS_DROP_TABLE)
                    c.execute(constants.SHOPS_DROP_TABLE)
                    c.execute(constants.PROD_SHOP_DROP_TABLE)
                    conn.commit()
                    print('Tables successfully removed')
                except sqlite3.Error as error:
                    print('Error while removing a table', error)
                finally:
                    if conn:
                        conn.close()
                try:
                    conn = sqlite3.connect(self.db_name)
                    c = conn.cursor()
                    c.execute(constants.PRODUCTS_CREATE_TABLE)
                    c.execute(constants.SHOPS_CREATE_TABLE)
                    c.execute(constants.PROD_SHOP_CREATE_TABLE)
                    conn.commit()
                    print('Empty tables successfully created')
                    c.close()
                except sqlite3.Error as error:
                    print("Error while creating a sqlite table", error)
                finally:
                    if conn:
                        conn.close()

            else:
                print('\nABORTED!!\n')

    class ProductMaintenance:
        """
        methods to list, add and delete records from the product table
        """
        def __init__(self, dbname):
            self.db_name = dbname
            self.general = GeneralFunctions
            self.menu_data = {
                'title': '\n   >>Product maintenance', 'options': [
                    {'title': 'Exit', 'function': self.general.stop},
                    {'title': 'List Products,', 'function': self.list_products},
                    {'title': 'Add Product', 'function': self.add_product},
                    {'title': 'Delete Product', 'function': self.delete_product}
                ]
            }

        def menu_prod_main(self):
            self.general.menu(self.menu_data)

        def list_products(self):
            self.general.list_products(self.db_name)

        def add_product(self):
            """
            Add a new product in the database. The product name and unit are given by the user. Next step is
            verification of the data by the user. Finally the record is inserted into the database.
            todo: input prod unit based on a list (dictionary, 2D list or from database) to improve flexibility.
            :return:
            """
            conn = None
            prod_name = input('Give product name: ')
            while True:
                prod_unit = input('give unit: p = pieces, k = kg, g = gram\n  p, k or g?')
                if prod_unit == 'p' or prod_unit == 'P':
                    prod_unit = 'pieces'
                    break
                elif prod_unit == 'k' or prod_unit == 'K':
                    prod_unit = 'kg'
                    break
                elif prod_unit == 'g' or prod_unit == 'G':
                    prod_unit = 'gram'
                    break
                else:
                    print('wrong input')

            print('Record to be added: \nProduct name: ', prod_name, '\nProduct unit: ',
                  prod_unit)
            x = input('Add this product? (y/n)')
            if x.upper() == 'Y':
                add_tuple = (prod_name, prod_unit, 0)
                try:
                    conn = sqlite3.connect(self.db_name)
                    c = conn.cursor()
                    print('connected to database')
                    c.execute(constants.PRODUCTS_ADD_RECORD, add_tuple)
                    conn.commit()
                    print('record inserted successfully')
                    c.close()
                except sqlite3.Error as error:
                    print('failed to add record', error)
                finally:
                    if conn:
                        conn.close()
                        print('connection closed')

        def delete_product(self):
            """
            Delete a product from the database products based on rowid
            :return:
            """
            conn = None
            self.list_products()
            delete_id = input('choose product to be deleted, ENTER to abort')
            if delete_id != '':
                try:
                    conn = sqlite3.connect(self.db_name)
                    c = conn.cursor()
                    c.execute(constants.PRODUCTS_GET_ONE_RECORD, delete_id)
                    row = c.fetchall()
                    if (len(row)) == 1:
                        for field in row:
                            print('number:      ', field[0])
                            print('description: ', field[1])
                        answer = input('Delete this record? (y/n)\n')
                        if answer.upper() == 'Y':
                            c.execute(constants.PRODUCTS_DELETE_ONE_RECORD, delete_id)
                        conn.commit()
                except sqlite3.Error as error:
                    print('failed to delete record', error)
                finally:
                    if conn:
                        conn.close()

    class ShoppingList:
        """
        Add or remove products to your shopping list
        """
        def __init__(self, dbname):
            self.db_name = dbname
            self.general = GeneralFunctions
            self.menu_data = {
                'title': '\n   >>Shopping list functions', 'options': [
                    {'title': 'Exit', 'function': self.general.stop},
                    {'title': 'Change shopping list', 'function': self.change_shopping_list},
                    {'title': 'Show shopping list', 'function': self.show_shopping_list},
                    {'title': 'Empty shopping list', 'function': self.empty_shopping_list}
                ]
            }

        def menu_prod_main(self):
            self.general.menu(self.menu_data)

        def change_shopping_list(self):
            """
            todo: complete code
            :return:
            """
            conn = None
            # show list of products
            self.general.list_products(self.db_name)
            # choose product
            change_id = input('choose product to be deleted, ENTER to abort')
            if change_id != '':
                try:
                    conn = sqlite3.connect(self.db_name)
                    c = conn.cursor()
                    # show record
                    c.execute(constants.PRODUCTS_GET_ONE_RECORD, change_id)
                    row = c.fetchall()
                    if len(row) == 1:
                        for field in row:
                            print('Description: ', field[1])
                            print('Quantity:    ', field[3], field[2])
                    # input quantity
                    # create data tuple
                    # change record
                    conn.commit()
                    """
                    van voorbeeld: 
                    sql_update_query = constants.PRODUCT_CHANGE_QUANTITY
                    data = (salary, id)
                    cursor.execute(sql_update_query, data)
                    sqliteConnection.commit()
                    print("Record Updated successfully")
                    cursor.close()
                    """
                    print('change')
                    c.close()
                except sqlite3.Error as error:
                    print('failed to change list, ', error)
                finally:
                    if conn:
                        conn.close()

        def show_shopping_list(self):
            print('list products')

        def empty_shopping_list(self):
            print('empty list')

    def __init__(self):
        self.db_name = 'shopping_list.db'
        self.db_operations = self.DataBaseOperations(self.db_name)
        self.prod_maintenance = self.ProductMaintenance(self.db_name)
        self.shopping_list = self.ShoppingList(self.db_name)
        self.general = GeneralFunctions
        self.menu_data = {
            'title': '\n   >>Main Menu', 'options': [
                {'title': 'Exit', 'function': self.general.stop},
                {'title': 'Database Operations,', 'function': self.db_operations.menu_db_opr},
                {'title': 'Product maintenance', 'function': self.prod_maintenance.menu_prod_main},
                {'title': 'Shopping list functions', 'function': self.shopping_list.menu_prod_main}
            ]
        }
        self.general.menu(self.menu_data)


shopping_list = ShoppingList()
