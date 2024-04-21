class Record:
    
    def __init__(self, id, ticket, date_start, date_end, activity):
        
        self._id = id    
        self._ticket = ticket
        self._date_start = date_start
        self._date_end = date_end
        self._save_qualitor = False
        self._activity = activity
    
    def __str__(self):
        
        return f'{str(self._id).ljust(4)} | {str(self._ticket).ljust(8)} | {self._date_start.strftime('%d/%m/%Y %H:%M').ljust(20)} | {('Not defined' if not self._date_end else self._date_end).ljust(20)} | {('☐' if not self._save_qualitor else '☑').ljust(11)} | {self._activity}'
    