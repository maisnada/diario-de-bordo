class Record:
    
    def __init__(self, ticket, date_start, date_end, activity):
            
        self._ticket = ticket
        self._date_start = date_start
        self._date_end = date_end
        self._save_qualitor = False
        self._activity = activity
    
    def __str__(self):
        
        return f'{self._ticket} | {self._date_start} | {self._date_end} | {self._save_qualitor} | {self._activity}'
    