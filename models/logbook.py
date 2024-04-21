from datetime import datetime

from models.record import Record

class LogBook:
    
    _count_record = 0
    
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
        
        print(f'{'#ID'.ljust(4)} | {'Ticket'.ljust(8)} | {'Date start'.ljust(20)} | {'Date end'.ljust(20)} | {'In Qualitor'.ljust(10)} | Activity')
                
        for record in self._records:
            
            print(record)
            
            
    def get_record(self, id):
        
        print(f'{'\n#ID'.ljust(5)} | {'Ticket'.ljust(8)} | {'Date start'.ljust(20)} | {'Date end'.ljust(20)} | {'In Qualitor'.ljust(10)} | Activity')
              
        print(self._records[id])   
             
    
    def __str__(self):
        
        return dir(self)  