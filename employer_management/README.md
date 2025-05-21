Employer Management System API

A RESTful API built with Django REST Framework for managing employer data with custom user authentication using email and Simple JWT.

Features:
- Email-based user authentication
- Token-based authentication with Simple JWT
- CRUD operations for employers (user-specific)
- Input validation and error handling

Tech Stack:
- Django, Django REST Framework
- Simple JWT
- SQLite (default)

Setup Instructions:
1. Clone the repository (if using Git):
   git clone <repository-url>
   cd employer_management

2. Create and activate a virtual environment:
   python -m venv venv
   For Windows: venv\Scripts\activate
   For Mac/Linux: source venv/bin/activate
   
3. Install dependencies:
   pip install -r requirements.txt

4. Apply database migrations:
   python manage.py makemigrations
   python manage.py migrate

5. Run the server:
   python manage.py runserver


API Endpoints:
- GET / - Welcome to the Employer Management System (points to /api/)
- GET /api/ - Welcome to the Employer Management API (lists endpoints)
- POST /api/auth/signup/ - Register a new user
- POST /api/auth/login/ - Login and get JWT tokens
- GET /api/auth/profile/ - Get user profile (requires token)
- POST /api/employers/ - Create an employer (requires token)
- GET /api/employers/ - List user’s employers (requires token)
- GET /api/employers/<id>/ - Get specific employer (requires token)
- PUT /api/employers/<id>/ - Update employer (requires token)
- DELETE /api/employers/<id>/ - Delete employer (requires token)

Testing:
Use Postman or curl to test endpoints. Example:
- Signup: curl -X POST http://127.0.0.1:8000/api/auth/signup/ -d '{"email":"test@example.com","first_name":"John","last_name":"Doe","password":"password123","password_confirm":"password123"}' -H "Content-Type: application/json"
- Login: curl -X POST http://127.0.0.1:8000/api/auth/login/ -d '{"email":"test@example.com","password":"password123"}' -H "Content-Type: application/json"
- Use "Authorization: Bearer <access_token>" for authenticated requests.

Notes:
- Users can only manage their own employers.
- SQLite is used by default; configure settings.py for other databases.
- Ensure dependencies are installed and migrations are applied before running.