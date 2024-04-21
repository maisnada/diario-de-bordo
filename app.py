import os

from models.logbook import LogBook

class App:
    
    def __init__(self):
        
        self._logBook = LogBook()
                
        self._show_menu()
      
    
    def _show_title(self, title):
        
        os.system('cls')
                     
        print(f'\n\x1b[5;30;47m☵☵ {title} ☵☵ \x1b[0m\n')
        
    
    def _footerMenu(self):
        
        input('\nPress any key to return menu: ')
            
        self._show_menu()         
    

    def _exit(self):
        
        os.system('cls')
        
        quit()
    

    def _show_menu(self):        

        self._resume_logBook_today()
                
        print('\n\n1 - Insert new record')
            
        print('3 - Exit\n')
        
        option_selected = int(input('Enter a option: '))
        
        if option_selected == 1:
            
            self._show_title('Insert new record')
            
            self._logBook.insert_record()
                        
        else:
            
            self._exit()

        self._footerMenu()
        
        
    def _resume_logBook_today(self):
        
        self._show_title('List today\'s records')
                
        self._logBook.list_records()
                        
runing_app = App()

