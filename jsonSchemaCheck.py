import json
from jsonschema import validate

# Load the json file
with open('work_test.json','r') as f:
    example_dict = json.load(f)
schema = {
        "type" : "array",
        "items" : {
        "type" : "object",
        "properties" : {
                "user_id" : {"type" : "number"},
                "symptom" : {"type" : "string"},
                        },
                }
        }
        
validate(instance=example_dict, schema=schema)