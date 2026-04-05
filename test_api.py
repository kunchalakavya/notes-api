"""
test_api.py — Run this AFTER the server is started (run.py)
Tests all endpoints of the Notes API.
"""
import requests

BASE = "http://127.0.0.1:8000"

def separator(title):
    print(f"\n{'─'*45}")
    print(f"  {title}")
    print(f"{'─'*45}")

# ── 1. Health Check ───────────────────────────────
separator("1. Health Check")
r = requests.get(f"{BASE}/")
print(r.json())

# ── 2. Create Notes ───────────────────────────────
separator("2. Create Note 1")
r = requests.post(f"{BASE}/notes", json={
    "title": "My First Note",
    "content": "FastAPI is awesome for building REST APIs!",
    "tag": "learning"
})
print(r.json())
note1_id = r.json()["note"]["id"]

separator("3. Create Note 2")
r = requests.post(f"{BASE}/notes", json={
    "title": "Shopping List",
    "content": "Milk, Eggs, Bread",
    "tag": "personal"
})
print(r.json())

# ── 3. Get All Notes ──────────────────────────────
separator("4. Get All Notes")
r = requests.get(f"{BASE}/notes")
print(r.json())

# ── 4. Filter by Tag ──────────────────────────────
separator("5. Filter Notes by tag=learning")
r = requests.get(f"{BASE}/notes?tag=learning")
print(r.json())

# ── 5. Get Single Note ────────────────────────────
separator(f"6. Get Single Note (id={note1_id})")
r = requests.get(f"{BASE}/notes/{note1_id}")
print(r.json())

# ── 6. Update Note ────────────────────────────────
separator(f"7. Update Note (id={note1_id})")
r = requests.put(f"{BASE}/notes/{note1_id}", json={
    "content": "FastAPI + Pydantic + Uvicorn = powerful backend stack!"
})
print(r.json())

# ── 7. Delete Note ────────────────────────────────
separator(f"8. Delete Note (id={note1_id})")
r = requests.delete(f"{BASE}/notes/{note1_id}")
print(r.json())

# ── 8. Confirm Deletion ───────────────────────────
separator("9. Get All Notes After Deletion")
r = requests.get(f"{BASE}/notes")
print(r.json())

print("\n✅ All tests passed!")
