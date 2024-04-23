from datetime import datetime

from models.record import Record

class LogBook:
    
    _count_record = 1
    
    def __init__(self):
        
        self._current_date = datetime.now()
        
        self._records = []
        
    
    def insert_record(self):
        
        ticket = input('Enter ticket number: ')
        
        activity = input('\nActivity description: ')

        record = Record(self._count_record, ticket, datetime.now(), None, activity)
                
        self._records.append(record)        
        
        self.get_record(self._count_record)
        
        self._count_record += 1


    def list_records(self):
        
        if len(self._records) > 0:
            
            print(f'{'#ID'.ljust(4)} | {'Ticket'.ljust(8)} | {'Date start'.ljust(20)} | {'Date end'.ljust(20)} | {'In Qualitor'.ljust(10)} | Activity')
                    
            for record in self._records:
                
                print(record)
                
        else:
            
            print('List\'s empty')
            
            
    def get_record(self, id):
        
        print(f'{'\n#ID'.ljust(5)} | {'Ticket'.ljust(8)} | {'Date start'.ljust(20)} | {'Date end'.ljust(20)} | {'In Qualitor'.ljust(10)} | Activity')
              
        print(self._records[id - 1]) 
        
    
    def update_status_qualitor(self):
        
        self.list_records()
        
        id_selected = int(input('\nPress record\'s ID for update: '))
        
        self._records[id_selected]._save_qualitor = not self._records[id_selected]._save_qualitor            
        
    
    def __str__(self):
        
        return dir(self)  