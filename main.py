from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import json
import os
import uuid
from datetime import datetime

app = FastAPI(
    title="Notes API",
    description="A simple REST API to create, read, update and delete notes.",
    version="1.0.0"
)

# ── Storage ──────────────────────────────────────────────────────────────────
DB_FILE = "notes.json"

def load_notes() -> dict:
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_notes(notes: dict):
    with open(DB_FILE, "w") as f:
        json.dump(notes, f, indent=2)

# ── Schemas ───────────────────────────────────────────────────────────────────
class NoteCreate(BaseModel):
    title: str
    content: str
    tag: Optional[str] = "general"

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    tag: Optional[str] = None

# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/", tags=["Health"])
def root():
    """Health check endpoint."""
    return {"status": "running", "message": "Welcome to the Notes API!"}


@app.post("/notes", status_code=201, tags=["Notes"])
def create_note(note: NoteCreate):
    """Create a new note."""
    notes = load_notes()
    note_id = str(uuid.uuid4())[:8]  # short unique ID
    notes[note_id] = {
        "id": note_id,
        "title": note.title,
        "content": note.content,
        "tag": note.tag,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }
    save_notes(notes)
    return {"message": "Note created successfully", "note": notes[note_id]}


@app.get("/notes", tags=["Notes"])
def get_all_notes(tag: Optional[str] = None):
    """Get all notes. Optionally filter by tag."""
    notes = load_notes()
    all_notes = list(notes.values())
    if tag:
        all_notes = [n for n in all_notes if n.get("tag") == tag]
    return {"total": len(all_notes), "notes": all_notes}


@app.get("/notes/{note_id}", tags=["Notes"])
def get_note(note_id: str):
    """Get a single note by ID."""
    notes = load_notes()
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    return notes[note_id]


@app.put("/notes/{note_id}", tags=["Notes"])
def update_note(note_id: str, update: NoteUpdate):
    """Update an existing note."""
    notes = load_notes()
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    note = notes[note_id]
    if update.title is not None:
        note["title"] = update.title
    if update.content is not None:
        note["content"] = update.content
    if update.tag is not None:
        note["tag"] = update.tag
    note["updated_at"] = datetime.now().isoformat()
    save_notes(notes)
    return {"message": "Note updated successfully", "note": note}


@app.delete("/notes/{note_id}", tags=["Notes"])
def delete_note(note_id: str):
    """Delete a note by ID."""
    notes = load_notes()
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    deleted = notes.pop(note_id)
    save_notes(notes)
    return {"message": "Note deleted successfully", "deleted_note": deleted}
