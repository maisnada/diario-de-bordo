from json import JSONEncoder
from encoders.recordJson import RecordJson

class LogBookJson(JSONEncoder):
    
    def default(self, obj):
        
        return obj.__dict__
        
        #json.dumps(record, cls=RecordJson)
    
    def decode(teste):
        
        
        #print(type(teste))
        #print('---->>>SSSS')
        print(teste)
        #print(teste["_current_date"])