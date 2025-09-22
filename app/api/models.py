from pydantic import BaseModel
from datetime import date

# for payload Validation
class NoteSchema(BaseModel):
    title:str
    description:str
    is_completed: bool = False
    created_at: date   # YYYY-MM-DD 

# for DB integration
class NoteDB(NoteSchema):
    id: int 