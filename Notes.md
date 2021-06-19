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
- product_unit - text (pcs or kg)
- number_required - real (how many items to purchase)
- shop_id - int

Table shops with fields: 
- ID - int (use standard rowid sqlite)
- shop_name - text

The field products-product_unit is text. for the time being the program fills the field to keep it consistent.  
The table with shops exists to keep everything consistent and easily change shop names
## Considerations operations.  
For the shopping list the operations are:  
- create table(s): to be executed once, starting the database or in case of refreshing the entire content
- add shop
- remove shop
- add item
- change item
- remove item
- change requirement
- reset all requirements
- generate shopping list 
## Class structure
### Menu  
The menu will be as simple as possible. Obviously there will be a main menu with items like maintenance:  
for instance list and create tables to be decided whether database operations get their own (sub)menu.  
In case of changing requirements a submenu might be preferable. 
### Database operations

