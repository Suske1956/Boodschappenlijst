import sqlite3


class MenuExec:
    """
    todo: write documentation for this class
    """
    @ staticmethod
    def menu(data):
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
                    data['options'][y]['command']()
                else:
                    print('wrong')
                print(data['title'])
                count = 0
                for x in data['options']:
                    print(count, '  ', x['title'])
                    count += 1


class ShoppingList:
    """
    ShoppingList is the main class basically it holds the main menu and controls the different database operations
    Within ShoppingList subclasses DataBaseOperations, ProductMaintenance and ShoppingList exists. Each of them
    holds its own submenu and the operations belonging to the group of operations.
    The last subclass is GeneralFunctions containing functions not having a relation with the database.
    The menu consists of a dictionary variable containing all menu items and a function object to start the appropriate
    code.
    todo: Document use of MenuExec?
    """
    class GeneralFunctions:
        """
        The class GeneralFunctions holds methods required in the main menu. The method stop is a dummy doing nothing.
        This avoids an error in the main menu.
        todo: consider to have the function stop in every class containing a menu
        """
        def stop(self):
            pass

    class DataBaseOperations:
        """
        The class DataBaseOperations holds functions
        todo: add functionality

        """
        def __init__(self, dbname):
            self.db_name = dbname
            self.menu_func = MenuExec
            self.menu_data = {
                'title': 'Database Operations\n', 'options': [
                    {'title': 'Exit', 'command': self.stop},
                    {'title': 'List Tables,', 'command': self.list_tables},
                ]
            }

        def stop(self):
            pass

        def menu_db_opr(self):
            self.menu_func.menu(self.menu_data)

        def list_tables(self):
            conn = None
            try:
                conn = sqlite3.connect(self.db_name)
                c = conn.cursor()
                c.execute("SELECT name FROM sqlite_master WHERE type='table';")
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

    class ProductMaintenance:
        """

        """
        def __init__(self, dbname):
            self.db_name = dbname
            pass

        def test(self):
            print('in maintenance')

    class ShoppingList:
        def __init__(self, dbname):
            self.db_name = dbname
            pass

        def test(self):
            print('in shopping list')

    def __init__(self):
        self.db_name = 'shopping_list.db'
        self.general = self.GeneralFunctions()
        self.db_operations = self.DataBaseOperations(self.db_name)
        self.prod_maintenance = self.ProductMaintenance(self.db_name)
        self.shopping_list = self.ShoppingList(self.db_name)
        self.menu_func = MenuExec()
        self.menu_data = {
            'title': 'Main Menu\n', 'options': [
                {'title': 'Exit', 'command': self.general.stop},
                {'title': 'Database Operations,', 'command': self.db_operations.menu_db_opr},
                {'title': 'Product maintenance', 'command': self.prod_maintenance.test},
                {'title': 'Shopping list', 'command': self.shopping_list.test}
            ]
        }
        self.menu_func.menu(self.menu_data)

    def menu_main(self):
        number = len(self.menu_data['options'])
        print(self.menu_data['title'])
        count = 0
        for x in self.menu_data['options']:
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
                    self.menu_data['options'][y]['command']()
                else:
                    print('wrong')
                print(self.menu_data['title'])
                count = 0
                for x in self.menu_data['options']:
                    print(count, '  ', x['title'])
                    count += 1


shopping_list = ShoppingList()
