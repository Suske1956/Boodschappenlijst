class Scripts:
    def __init__(self):
        pass

    def prog1(self):
        print('prog 1 heeft gewerkt')

    def prog2(self):
        print('prog 2 heeft gewerkt')


class Menu(Scripts):
    def __init__(self):
        super().__init__()
        self.menutxt = 'kies 1 of 2, 0 om te stoppen'
        self.maintxt = 'mainmenu choose 1, 2 or 0 to stop'

    def main(self, maintext):
        print(maintext)
        optie = input('geef je keuze')
        while optie != '0':
            if optie == '1':
                self.prog1()
            elif optie == '2':
                self.prog2()
            else:
                print('ongeldige keuze')
            print(maintext)
            optie = input('geef je keuze')

    def sub(self, subtext):
        pass

''''
class Test(Menu):
    def __init__(self):
        super().__init__()
        self.menutxt = 'kies 1 of 2, 0 om te stoppen'
        self.maintxt = 'mainmenu choose 1, 2 or 0 to stop'

    def print(self):
        self.menu_print(self.menutxt)

    def tst(self):
        self.main(self.maintxt)

    def opr1(self):
        print('een gekozen')

    def opt2(self):
        print('twee gekozen')

'''

menu = Menu()
menu.main('kies 1 of 2')
# test.tst()
# menu.menu_print('kies 1 of 2, 0 om te stoppen')





'''
def menu():
    print('kies 1, 2 of 3 - 0 om te stoppen')

menu()
optie = input('geef je keuze')
while optie != '0':
    if optie == '1':
        print('1 gekozen')
    elif optie == '2':
        print('2 gekozen')
    elif optie == '3':
        print('3 gekozen')
    else:
        print('verkeerde keuze')
    menu()
    optie = input('geef je keuze')
'''