### Basic data serialization in protobuf with Python

import person_pb2

person = person_pb2.Person()
person.name = "Sam"
person.id = 343
person.email = "sam@randommail.com"

data = person.SerializeToString()

new_person = person_pb2.Person()
new_person.ParseFromString(data)

print(new_person)
