# 🗒️ StickyNotesREST

A Django REST Framework API for managing sticky notes with tagging, filtering, and search functionality.

---

## 🛠️ Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/bitsbuild/StickyNotesREST-drf-backend-basics-reinforcement.git
cd stickynotes

# 2. Create and activate a virtual environment (recommended)
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 5. Start the development server
python manage.py runserver
````

Once the server is running, Swagger UI documentation is available at:

```
http://127.0.0.1:8000/
```

And the API base is available at:

```
http://127.0.0.1:8000/stickynotes/api/
```

---

## 🔗 URL Configuration

### Project-Level (`project/urls.py`)

```python
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Sticky Notes REST API",
      default_version='v1',
      description="A Django REST Framework Backend for Managing Sticky Notes with Tagging, Filtering, and Search Functionality.",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('stickynotes/api/', include('restapi.urls')),
]
```

### App-Level (`restapi/urls.py`)

```python
from django.urls import path
from restapi.views import NoteCR, NoteUD, SearchByTitle, SearchByContent, FilterByTags

urlpatterns = [
    path('cr/', NoteCR.as_view()),
    path('ud/<uuid:id>/', NoteUD.as_view()),
    path('search-by-title/<str:title>', SearchByTitle.as_view()),
    path('search-by-content/<str:content>', SearchByContent.as_view()),
    path('filter-by-tags/<str:tag>', FilterByTags.as_view()),
]
```

---

## 📚 API Endpoints Documentation

All endpoints are prefixed with:

```
http://127.0.0.1:8000/stickynotes/api/
```

---

### 🔹 GET `/cr/`

**Description:** Retrieve all notes.

* **Method:** `GET`
* **Response:** `200 OK`

```json
[
  {
    "id": "uuid-value",
    "note_title": "Meeting Notes",
    "note_body": "Discuss sprint planning",
    "note_tags": ["meeting", "sprint"]
  },
  ...
]
```

---

### 🔹 POST `/cr/`

**Description:** Create a new note.

* **Method:** `POST`
* **Request Body:**

```json
{
  "note_title": "Grocery List",
  "note_body": "Buy fruits and vegetables",
  "note_tags": ["shopping", "personal"]
}
```

* **Success Response:** `201 Created`

```json
{
  "status": {
    "id": "uuid",
    "note_title": "Grocery List",
    "note_body": "Buy fruits and vegetables",
    "note_tags": ["shopping", "personal"]
  }
}
```

* **Failure Response:** `400 Bad Request`

```json
{
  "status": {
    "note_title": ["This field is required."]
  }
}
```

---

### 🔹 PUT `/ud/<uuid:id>/`

**Description:** Update an existing note.

* **Method:** `PUT`
* **Request Body:**

```json
{
  "note_title": "Updated Title",
  "note_body": "Updated Body",
  "note_tags": ["updated", "important"]
}
```

* **Success Response:** `200 OK`

---

### 🔹 DELETE `/ud/<uuid:id>/`

**Description:** Delete a note by UUID.

* **Method:** `DELETE`
* **Success Response:** `200 OK`

```json
{
  "status": "selected item deleted"
}
```

* **Failure Response:** `400 Bad Request`

```json
{
  "status": "deletion process failed"
}
```

---

### 🔹 GET `/search-by-title/<str:title>`

**Description:** Search notes by title (case-insensitive partial match).

* **Method:** `GET`
* **Success Response:** `200 OK`

---

### 🔹 GET `/search-by-content/<str:content>`

**Description:** Search notes by content/body (case-insensitive partial match).

* **Method:** `GET`
* **Success Response:** `200 OK`

---

### 🔹 GET `/filter-by-tags/<str:tag>`

**Description:** Filter notes that include a specific tag.

* **Method:** `GET`
* **Success Response:** `200 OK`

---

## 🧾 Note Model Overview

```python
class Note(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    note_title = models.CharField(max_length=70)
    note_body = models.CharField(max_length=210)
    note_tags = models.JSONField(default=list)
```

### Field Details:

| Field        | Type      | Description                           |
| ------------ | --------- | ------------------------------------- |
| `id`         | UUIDField | Unique ID for the note                |
| `note_title` | CharField | The title of the note                 |
| `note_body`  | CharField | The main content of the note          |
| `note_tags`  | JSONField | List of tags associated with the note |

---

**Build strong backends — because solid foundations power great software. 💡**
