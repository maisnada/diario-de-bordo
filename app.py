import os

from models.logbook import LogBook

class App:
    
    def __init__(self):
        
        self._logBook = LogBook()
                
        self._show_menu()
      
            
    def _show_title(self, title):
        
        os.system('cls')
                     
        print(f'\n\x1b[6;30;42m☵☵ {title} ☵☵ \x1b[0m\n')
        
    
    def _footerMenu(self):
        
        input('\nPress any key to return menu: ')
            
        self._show_menu()         
    

    def _exit(self):
        
        os.system('cls')
        
        quit()
    

    def _show_menu(self):        

        self._resume_logBook_today()
                
        print('\n\n1 - Insert new record')
        
        print('2 - Set date end in record')
        
        print('3 - Update status Qualitor in record')
            
        print('4 - Exit\n')
        
        option_selected = int(input('Enter a option: '))
        
        if option_selected == 1:
            
            self._show_title('Insert new record')
            
            self._logBook.insert_record()
        
            self._footerMenu()
            
        elif option_selected == 2:
            
            self._show_title('Set date end in record')
            
            self._logBook.set_date_end_record()
            
            self._show_menu()
        
        elif option_selected == 3:
            
            self._show_title('Update status Qualitor')
            
            self._logBook.update_status_qualitor_record()
            
            self._show_menu()
            
        
                        
        else:
            
            self._exit()        
        
    def _resume_logBook_today(self):
        
        self._show_title('Record\'s list today\'s')
                
        self._logBook.list_records()
                        
runing_app = App()

