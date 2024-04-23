class Record:
    
    def __init__(self, id, ticket, date_start, date_end, activity):
        
        self._id = id    
        self._ticket = ticket
        self._date_start = date_start
        self._date_end = date_end
        self._save_qualitor = False
        self._activity = activity
        
    @property
    def date_end(self):
        
        return self._date_end
    
    @date_end.setter
    def date_end(self, date):
        
        self._date_end = date
        
    def update_save_qualitor(self):
        
        self._save_qualitor = not self._save_qualitor
    
    def __str__(self):
        
        return f'{str(self._id).ljust(4)} | {str(self._ticket).ljust(8)} | {self._date_start.strftime('%d/%m/%Y %H:%M:%S').ljust(20)} | {('Not defined' if not self._date_end else self._date_end.strftime('%d/%m/%Y %H:%M:%S')).ljust(20)} | {('☐' if not self._save_qualitor else '☑').ljust(11)} | {self._activity}'
    