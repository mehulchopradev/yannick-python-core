import json

with open('student_data.json', mode='r') as fp:
    obj = json.load(fp)
    print(obj)
    print(type(obj)) # dictionary
    # deserialization
