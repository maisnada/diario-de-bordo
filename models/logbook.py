from datetime import datetime

import json
import os

from json import JSONDecodeError

from models.record import Record
from encoders.recordJson import RecordJson

class LogBook:
    
    _count_record = 1
    
    def __init__(self):
        
        self._current_date = datetime.now()
        
        self._records = []
                
   
    def insert_record(self):
        
        ticket = input('Enter ticket number: ')
        
        activity = input('\nActivity description: ')
        
        record = Record(self._count_record, ticket, (datetime.now()).timestamp(), None, activity)
                        
        self._records.append(record)        
        
        self.get_record(self._count_record)
        
        self._count_record += 1
                
        file = open("data.json","a+",encoding="utf-8")
        
        teste = []
        
        teste.append(record)
        
        #file.write(json.dumps(record, cls=RecordJson))       
        file.write(json.dumps(teste))
        
                  
        file.close()

        #teste = json.dumps(record, cls=RecordJson)

        #teste = record.__dict__
        #print(teste)
        #print(type(teste))
        #
        #eee = json.loads(teste, object_hook=RecordJson.decode)

        #print(eee)
        #print(type(eee))
            
    def list_records(self):           
             
        p = os.path.join(os.path.abspath(os.getcwd()), 'data', 'data.json')
           
        if True:
                     
            file = open(p,"a+",encoding="utf-8")         
       
            try:            
                
                records = json.load(file, object_hook=RecordJson.decode)

                if records:

                    print(f'{'#ID'.ljust(4)} | {'Ticket'.ljust(8)} | {'Date start'.ljust(20)} | {'Date end'.ljust(20)} | {'In Qualitor'.ljust(10)} | Activity')

                    for record in self._records:

                        print(record)

                else:

                    print('List\'s empty')
                    
            except JSONDecodeError as e:
                
                print(f'-->{e}')
                
            finally:
                
                file.close()
                
            
        else:
            
            print('arq not found')    
            
    def get_record(self, id):
        
        print(f'{'\n#ID'.ljust(5)} | {'Ticket'.ljust(8)} | {'Date start'.ljust(20)} | {'Date end'.ljust(20)} | {'In Qualitor'.ljust(10)} | Activity')
              
        print(self._records[id - 1]) 
        
    
    def update_status_qualitor_record(self):
        
        self.list_records()        
        
        try:
        
            id_selected = int(input('\nPress record\'s ID for update: '))                           
            
            self._records[id_selected - 1].update_save_qualitor()
        
        except IndexError as e:
                        
            raise Exception(f'ID {id_selected} not found in list. Try again!')
        
        except ValueError as e:
            
            raise Exception('ID only number! Try again!')
        
    
    def set_date_end_record(self):
        
        self.list_records()
        
        id_selected = int(input('\nPress record\'s ID for set date end: '))
        
        date_select = input(f'\nPress date or enter for current date [{datetime.now().strftime('%d/%m/%Y %H:%M')}]: ')    
        
        if not date_select:
            
            self._records[id_selected -1].date_end = datetime.now()
            
        else:
            
            datetime_object = datetime.strptime(date_select, '%d/%m/%Y %H:%M')
         
            self._records[id_selected -1].date_end = datetime_object
        
    
    def __str__(self):
        
        return dir(self)  