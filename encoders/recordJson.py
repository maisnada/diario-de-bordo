from json import JSONEncoder

class RecordJson(JSONEncoder):
    
    def default(self, obj):
        
        return obj.__dict__
    
    def decode(teste):
        
        #print('---->>>SSSS')
        print(teste['_current_date'])