"""
JSON => JavaScript Object Notation

{"name": "Jon", "age": 25, "id":1}  => This is a valid JSON
[{"name": "Jane", "age": 21,}, {"name": "Harry", "age": 43}]  => This is also a valid JSON

{'name': 'Harry', 'age':2}  => It is an invalid JSON because it has single quotes in key-value

Extension of JSON files is .JSON

"""
import json

# JSON dumps
student = {'name': 'Jon', 'age': 21, 'id': 1}
json_obj = json.dumps(student)
with open("students.json", "w") as fp:
    fp.write(json_obj)


# JSON loads
with open("students.json", "r") as fp:
    # data = fp.read()
    data = json.loads(fp.read())
    print(type(data))
    print(data)
    # print(data['age'])
