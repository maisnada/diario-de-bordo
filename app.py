import os

from models.logbook import LogBook

class App:
    
    def __init__(self):
        
        self._logBook = LogBook()
                
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

    
    def _show_subtitle(self, subtitle):
        
        os.system('cls')
        
        print(f'\x1b[6;30;42m☵☵ {subtitle} ☵☵ \x1b[0m\n')
        
    
    def _headerMenu(self):
        
        os.system('cls')
        
        self._show_title()
        
    
    def _footerMenu(self):
        
        input('Press any key to return menu: ')
            
        self._show_menu()         
    
    
    def _show_menu(self):        
        
        self._headerMenu()
        
        print('\n1 - Insert new record')
        print('2 - List today\'s records')
        print('3 - Exit\n')
        
        option_selected = int(input('Enter a option: '))
        
        if option_selected == 1:
            
            self._show_subtitle('Insert new record')
            
            self._logBook.insert_record()
                        
        elif option_selected == 2:
            
            self._show_subtitle('List today\'s records')
            
            self._logBook.list_records()    

        self._footerMenu()        
                        
runing_app = App()

