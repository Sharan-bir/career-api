# NetPy Job Portal API

This is the backend API for the NetPy job portal, built with Django REST Framework.

## Setup Instructions

1. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure email settings:
   - Open `job_portal/settings.py`
   - Update the email configuration with your SMTP settings:
     ```python
     EMAIL_HOST_USER = 'your-email@gmail.com'
     EMAIL_HOST_PASSWORD = 'your-app-password'
     DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
     ```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create initial data:
```bash
python setup.py
```

6. Run the development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

## API Endpoints

- `GET /api/categories/` - List all job categories
- `GET /api/jobs/` - List all jobs
- `GET /api/jobs/?category=Backend` - Filter jobs by category
- `POST /api/applicants/` - Submit a job application

## Admin Interface

Access the admin interface at `http://localhost:8000/admin/`
- Username: admin
- Password: admin123

## Frontend Integration

The frontend is already configured to work with this API. Make sure to:

1. Update the `API_BASE_URL` in `js/career_page.js` if your API is running on a different URL
2. Configure CORS settings in `settings.py` for production use
3. Set up proper email configuration for application notifications

## File Structure

```
job_portal/
├── job_portal_app/
│   ├── models.py      # Database models
│   ├── serializers.py # API serializers
│   ├── views.py       # API views
│   └── urls.py        # URL routing
├── job_portal/
│   ├── settings.py    # Project settings
│   └── urls.py        # Main URL configuration
└── setup.py           # Initial data setup
``` 