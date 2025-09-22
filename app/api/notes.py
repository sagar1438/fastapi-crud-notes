from fastapi import APIRouter, HTTPException
from app.api.models import NoteSchema, NoteDB
from app.api import crud

router = APIRouter()

# post a note
@router.post("/", response_model=NoteDB)
async def post_note(note: NoteSchema):
    note_id = await crud.post(note)
    response_object = {
        "id": note_id,
        "title": note.title,
        "description": note.description,
        "is_completed": note.is_completed,
        "created_at": note.created_at
    }
    return response_object

# retrieve a note
@router.get("/{id}/", response_model=NoteDB)
async def read_note(id:int):
    note = await crud.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

# get all notes
@router.get("/", response_model=list[NoteDB])
async def read_all_note():
    return await crud.get_all()

# update a note
@router.put("/{id}/",response_model=NoteDB)
async def update_note(id:int , payload: NoteSchema):
    note = await crud.get(id) # checking to see if the note exists or not
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    note_id = await crud.put(id, payload)
    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
        "is_completed": payload.is_completed,
        "created_at": payload.created_at
    }
    return response_object

# deleting a note
@router.delete("/{id}/", response_model=NoteDB)
async def delete_note(id:int):
    note = await crud.get(id) # checking whether the note exists or not
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    await crud.delete(id)
    return note