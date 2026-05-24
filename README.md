# Contact Book

A simple contact management system (mini CRM) built with Django. Users can save contacts, attach images, categorize them, and filter/search.

## Features

- Full CRUD for contacts and categories
- Image upload for contact avatars
- Category-based filtering
- Search by name, phone, or email
- Sort by name or date
- Pagination (10 per page)
- Dashboard with statistics
- REST API (DRF) with full CRUD endpoints
- Bootstrap 5 UI

## How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/contact-book-app.git
cd contact-book-app

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create a superuser (optional)
python manage.py createsuperuser

# Start the server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/contacts/` | List contacts |
| POST | `/api/contacts/` | Create contact |
| GET | `/api/contacts/<id>/` | Contact detail |
| PUT/PATCH | `/api/contacts/<id>/` | Update contact |
| DELETE | `/api/contacts/<id>/` | Delete contact |
| GET | `/api/categories/` | List categories |
| POST | `/api/categories/` | Create category |
| GET | `/api/contacts/?search=&category=` | Filter/Search |

## Project Structure

```
contact_book/
├── contacts/          # Main app
├── templates/         # HTML templates
├── static/            # Static files
├── media/             # Uploaded images
├── contact_book/      # Project settings
├── manage.py
└── README.md
```
