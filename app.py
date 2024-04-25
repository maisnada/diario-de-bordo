import os

from models.logbook import LogBook

class App:
    
    def __init__(self):
        
        self._logBook = LogBook()

        self._main()     
        
    def _show_title(self):
        
        os.system('cls')
                     
        print(f'\n\x1b[6;30;42m>> BookLog <<\x1b[0m\n') 
                  
            
    def _show_subtitle(self, title):

        self._show_title()
                 
        print(f'\x1b[6;30;47m> {title}\x1b[0m\n')  
    

    def _exit(self):
        
        os.system('cls')
        
        quit()
    

    def _main(self):
        
        self._show_title()
        
        self._resume_logBook_today()
        
        self._show_menu()
      

    def _show_menu(self):        
                
        print('\n\n1 - Insert new record')
        
        print('2 - Set date end in record')
        
        print('3 - Update status Qualitor in record')
            
        print('4 - Exit\n')
        
        try:
            
            option_selected = int(input('Enter a option: '))
            
            if option_selected == 1:                  
                
                self._show_subtitle('Insert new record')
                
                self._logBook.insert_record()
            
                input('\nPress any key to return menu: ')
                
                self._main()
                
                
            elif option_selected == 2:
                
                self._show_subtitle('Set date end in record')
                
                self._logBook.set_date_end_record()
                
                self._main()
            
            elif option_selected == 3:
                
                self._show_subtitle('Update status Qualitor')
                
                self._logBook.update_status_qualitor_record()
                
                self._main()
                
            else:
                
                self._exit()
                
        except Exception as e:
            
            print(f'\x1b[2;30;41m> {e}\x1b[0m\n')  
                   
            
    def _resume_logBook_today(self):
        
        self._show_subtitle('Record\'s list today\'s')
                
        self._logBook.list_records()
                        
runing_app = App()

