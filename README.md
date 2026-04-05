# 📝 Notes API

A lightweight REST API built with **FastAPI** to create, read, update, and delete notes — with tag-based filtering and persistent JSON storage.

---

## 🚀 Features

- ✅ Full CRUD operations on notes
- ✅ Filter notes by tag
- ✅ Auto-generated interactive docs (Swagger UI)
- ✅ Persistent storage using JSON (no database setup needed)
- ✅ Input validation with Pydantic
- ✅ Clean error handling with HTTP exceptions

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| FastAPI | Web framework |
| Uvicorn | ASGI server |
| Pydantic | Data validation |
| JSON | Lightweight storage |

---

## 📦 Installation

```bash
pip install fastapi uvicorn
```

---

## ▶️ Running the Server

```bash
python run.py
```

Then open your browser at:
```
http://127.0.0.1:8000/docs
```
You'll see the interactive Swagger UI where you can test all endpoints.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/notes` | Create a new note |
| GET | `/notes` | Get all notes (optional `?tag=` filter) |
| GET | `/notes/{id}` | Get a single note by ID |
| PUT | `/notes/{id}` | Update a note |
| DELETE | `/notes/{id}` | Delete a note |

---

## 📋 Example Usage

### Create a Note
```json
POST /notes
{
  "title": "My First Note",
  "content": "FastAPI is great for building REST APIs!",
  "tag": "learning"
}
```

### Response
```json
{
  "message": "Note created successfully",
  "note": {
    "id": "a1b2c3d4",
    "title": "My First Note",
    "content": "FastAPI is great for building REST APIs!",
    "tag": "learning",
    "created_at": "2026-04-05T10:00:00",
    "updated_at": "2026-04-05T10:00:00"
  }
}
```

---

## 🗂️ Project Structure

```
notes-api/
├── main.py        # FastAPI app & all routes
├── run.py         # Server launcher
├── test_api.py    # API test script
├── notes.json     # Auto-created on first note
└── README.md
```

---

## 🧪 Running Tests

Make sure the server is running first, then:
```bash
python test_api.py
```

---

## 👩‍💻 Author

**Kunchala Kavya** — [github.com/kunchalakavya](https://github.com/kunchalakavya)
