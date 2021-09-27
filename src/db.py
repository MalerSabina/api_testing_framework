import pathlib
from dataclasses import asdict

from tinydb import TinyDB, Query

from src.definitions import User

path = pathlib.Path(__file__).parent.parent.absolute()

_js_db = TinyDB(path.joinpath("db.json"))

poly_db = _js_db.table("polydata")
users_db = _js_db.table("user")


users_db.upsert(asdict(User("test", "1234")), cond=Query()["username"] == "test")


# {
#   "object_id": 65656,
#   "data": [
#     {
#       "key": "key1",
#       "val": "val1",
#       "valType": "str"
#     }
#   ]
# }