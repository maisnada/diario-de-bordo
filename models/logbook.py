from datetime import datetime

class LogBook:
    
    def __init__(self):
        
        self._current_date = datetime.now()
        
        self._records = []
        
    
    def __str__(self):
        
        return self._records