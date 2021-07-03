# Probeersels met de opbouw van een menu, kan later weg
import os


class Scripts:
    def __init__(self):
        pass

    # hier kan ik alle database akties doen. Overweeg verschillende klassen.
    def prog(self, keuze):
        if keuze == 1:
            print('prog 1 heeft gewerkt')
        elif keuze == 2:
            print('prog 2 heeft gewerkt')


    def prog2(self):
        print('prog 2 heeft gewerkt')


class Menu:
    def __init__(self):
        self.test = Scripts()
        # het menu kan in een dictionary menudata vervat zijn. in de items moet een commando zijn dat het
        # goede prog aanstuurt. Zie textblok beneden.
        self.menutxt = 'kies 1 of 2, 0 om te stoppen'
        self.maintxt = 'mainmenu choose 1, 2 or 0 to stop'

    def main(self):
        print(self.maintxt)
        optie = input('geef je keuze')
        while optie != '0':
            if optie == '1':
                self.test.prog(1)
            elif optie == '2':
                self.test.prog(2)
            else:
                print('ongeldige keuze')
            print(self.maintxt)
            optie = input('geef je keuze')

    def sub(self, subtext):
        pass


''''

'''

menu = Menu()
menu.main()
# os.system('clear')  # Dit werkt alleen in een bash terminal
# test.tst()


'''
menu met een dictionary is hier beschreven: 
https://gist.github.com/abishur/2482046

Dit menu werkt wel, alleen snap ik nog niet helemaal hoe. 
Het gebruikt in ieder geval curses en os. Curses is om toestaanslagen af te vangen waardoor je door een menu 
kunt scrollen.  
Ik heb het getest, en het werkt. Voor deze applikatie is het wat te veel van het goede. 
Ik kan wel het principe van een menu in een dictionary gebruiken. 
'''