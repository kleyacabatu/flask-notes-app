# Flask Notes App – Tags API Feature

## 🆕 Feature: Tags API

This feature adds a new **Tags system** to the Flask Notes App, allowing users to associate multiple tags with a notebook.

### ✅ Summary of Changes

- Introduced a `Tag` model with the following fields:
  - `id`: Primary key
  - `name`: Name of the tag (e.g., "Work", "Personal")
  - `notebook_id`: Foreign key linking the tag to a notebook
- Added a **one-to-many** relationship between `Notebook` and `Tag`
  - Each `Notebook` can have many `Tags`
- Created a RESTful **Tags API** under `/api/tags` with full CRUD support:
  - `POST /api/tags`: Create a new tag
  - `GET /api/tags`: Get all tags
  - `GET /api/tags/<id>`: Get a specific tag by ID
  - `PUT /api/tags/<id>`: Update a tag
  - `DELETE /api/tags/<id>`: Delete a tag

### 🔧 Files Modified

- `app.py`: Added the `Tag` model and tag API routes
- `test_tags.py`: Added 5 tests for the tags API using `pytest`

### 🧪 Testing

To test the new tag feature:

1. Make sure you're in a virtual environment
2. Install dependencies if needed:
   ```bash
   pip install -r requirements.txt
