# Notes regarding shopping list  
Database = sqlite since goal is "learn to work wit sqlite"  
interface = cli since developing an interface is not a goal
## Database operations    
Chosen for:  "try: except: finally:" for errors in sql commands are not  
easy to find. "except sqlite3.Error as error:" exports the error from  
sqlite to the variable error
## Considerations database structure  
Table products with fields:
- ID - int (use standard rowid sqlite)
- product_name - text 
- product_unit - text (pcs kg, gram)
- number_required - real (how many items to purchase)
- shop_id - int

Table shops with fields: 
- ID - int (use standard rowid sqlite)
- shop_name - text

Table product_shop with fields:  
- prod_id - int
- shop_id - int
- price - real

The field products-product_unit is text. for the time being the program fills the field to keep 
it consistent.  
The table with shops exists to keep everything consistent and easily change shop names
## Considerations operations.  
For the shopping list the operations are:  
- create table(s): to be executed once, starting the database or in case of refreshing the 
  entire content
- add shop
- remove shop
- add item
- change item
- remove item
- change requirement
- reset all requirements
- generate shopping list 
## Class structure
The menu will be as simple as possible. The main menu is a class which holds the database name. Database
operations will be grouped in separate classes each class has its own submenu triggering the methods 
within the class.
Notes regarding menu's:  
- I did not find an easy solution for "press any key", so I used "Press ENTER" instead.
### Class: MainMenu
#### Attributes
- database name: string
#### Methods
- main menu: starts other menus and passes database name to other classes. Also closes the application
### Class: Database operations
#### Attributes
- none
#### Methods
- menu: starts other methods, sets database name, returns to main menu
- list tables: give a list of all table names
- reset database: remove and regenerate all tables in the database. 
### Class: ProductMaintenance
#### Attributes
- none
#### Methods
- menu: starts other methods, sets database name
- List products 
- Add product to table of products note - this is the first method to be defined. Consider re-usability
  - get data from user
  - verify data
  - add to database
### Class: ShoppingList

## Lessons learned
- It is recommended to add a docstring after the definition of a class containing a description of the class. 
The docstring can be called using the special attribute double underscore - doc - double underscore
- An object from a class can be initiated inside another class, or globally
- Classes can be nested
- storing a function in a variable: omit () in the command. Now the command can be called by variable(). 
  Obviously, between brackets all arguments required. 