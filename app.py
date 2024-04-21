import os

class App:
    
    def __init__(self):
        
        os.system('cls')
        
        self._show_title()
        self._show_menu()
        
        
    def _show_title(self):
        
        print('''\x1b[6;30;42m              
        ╔╗────────╔══╗──────╔╗
        ║║────────║╔╗║──────║║
        ║║──╔══╦══╣╚╝╚╦══╦══╣║╔╗
        ║║─╔╣╔╗║╔╗║╔═╗║╔╗║╔╗║╚╝╝
        ║╚═╝║╚╝║╚╝║╚═╝║╚╝║╚╝║╔╗╗
        ╚═══╩══╩═╗╠═══╩══╩══╩╝╚╝
        ───────╔═╝║
        ───────╚══╝\x1b[0m''')

    def _show_menu(self):
        
        print('\n1 - Insert new record')
        print('2 - List today\'s records')
        print('3 - Exit')