# types
menu = 'menu'
command = 'command'
exit_menu = 'exit'

# menu line:   {'title': '<Title>', 'type': menu / command / exit_menu, 'subtitle': '<Subtitle>', 'options': []}

menu_data = {
    'title': 'Main menu', 'type': menu, 'subtitle': 'Select an option', 'options': [
        {'title': 'Database_operations', 'type': menu, 'subtitle': 'Select an option', 'options': [
            {'title': 'sub1_optie1', 'type': command, 'command': 'sub1_comm1'},
            {'title': 'sub1_optie2', 'type': command, 'command': 'sub1_comm2'},
            {'title': 'Back', 'type': exit_menu},
        ]},
        {'title': 'First Command', 'type': command, 'command': 'print_first'},
        {'title': 'Second Command', 'type': command, 'command': 'print_second'},
        {'title': 'Exit', 'type': exit_menu}
    ]}

print(menu_data['title'], menu_data['subtitle'])
count = 1
for x in menu_data['options']:
    print(count, '  ', x['title'])
    count += 1

print(menu_data['options'][0]['options'][0])

'''
Ik ben hiermee begonnen omdat de menustructuur van de boodschappenlijst al heel snel explodeerde. 
In eerste instantie ben ik naar voorbeelden gaan zoeken. Ik kwam er een tegen die de module curses
gebruikt. Interessant daaraan was dat alle menus in een dictionary onder gebracht zijn. Hierdoor kun je met een paar 
commandoregels door het menu itereren. curses ga ik niet gebruiken omdat ik dan beter qt kan toepassen. 
Het menu voorbeeld_curses.py ziet er wel heel gelikt uit, maar is voor mij overdone en ik leer er niets van. 

Begonnen met het hoofdmenu en dat te laten zien. Dat werkt in ieder geval. 
in menu_voorbeeld.py heb ik een menu klasse opgetuigd. Dat is in ieder geval een goed uitgangspunt om het menu
in te kapselen. 
Vraag is hoofd- en submenu's in een dictionary onder brengen of ieder menu apart. 
Mijn gevoel zegt de eerste optie. De code moet dan wel weten waar in het menu hij zich bevind.  
Ik moet nog even goed kijken hoe dat in curses gedaan wordt.  

'''
