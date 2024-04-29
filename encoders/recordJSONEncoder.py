from json import JSONEncoder

class RecordJSONEncoder(JSONEncoder):
    
    def default(self, obj):
        
        return obj.__dict__