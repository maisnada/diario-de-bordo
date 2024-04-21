class Record:
    
    def __init__(self, ticket, date_start, date_end, activity):
            
        self._ticket = ticket
        self._date_start = date_start
        self._date_end = date_end
        self._save_qualitor = False
        self._activity = activity
    
    def __str__(self):
        
        return f'{self._ticket.ljust(8)} | {self._date_start.strftime('%d/%m/%Y %H:%M')} | {('Not defined' if not self._date_end else self._date_end).ljust(20)} | {('Not save' if not self._save_qualitor else 'Save').ljust(1)} | {self._activity}'
    