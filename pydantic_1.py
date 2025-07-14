from datetime import datetime
from pydantic import BaseModel, PositiveInt, ValidationError

class User(BaseModel):
    id:int
    name: str = "John Doe"
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]


external_data = {
    'id' : 123, 
    'signup_ts': '2019-06-01 12:22', 
    'tastes': {'water': 9, b'cheese': 7, 'cabbage': 8}, 
}

external_data_2 = {'id': "not an int", 'tastes': {}, }


try: 
    User(**external_data_2)

except ValidationError as e:
    print(e.errors())

user = User(**external_data)
print(user.id)
print(user.model_dump())

