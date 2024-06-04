import os

class LogBookDao:
    
    _path = os.path.join(os.path.abspath(os.getcwd()), 'data', 'data.json')
    _file = None
    
    def __init__(self):
        pass
    
    def open(self):
    
        self._file = open(self._path, "a+", encoding="utf-8")
        
    def close(self):
        
        self._file.close()
        
    def addRecord(record):
        
        