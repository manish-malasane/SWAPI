from pydantic import BaseModel
from datetime import datetime


class Base(BaseModel):

    url: str
    created: datetime
    edited: datetime


if __name__ == "__main__":
    data = {
        "url": "https://swapi.dev/api/people/1",
        "edited": "2014-12-10T16:36:50.509000Z",
        "created": "2014-12-10T16:36:50.509000Z"
    }
    obj = Base(**data)
    print(obj)
