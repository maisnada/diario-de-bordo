from datetime import datetime

from models.record import Record

class LogBook:
    
    def __init__(self):
        
        self._current_date = datetime.now()
        
        self._records = []
        
    
    def insert_record(self):
        
        ticket = input('Enter ticket number: ')
        
        activity = input('\nActivity description: ')

        record = Record(ticket, datetime.now(), None, activity)
                
        print(record)
                
        self._records.append(record)


    def list_records(self):
        
        for record in self._records:
            
            print(record)
        
    
    def __str__(self):
        
        return dir(self)  