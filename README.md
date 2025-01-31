# **FAQ Management System**

This is a Django-based FAQ management system that supports multi-language translations, a WYSIWYG editor, and a REST API. It allows you to store FAQs, translate them into multiple languages, and retrieve them dynamically via API.

---

## **Features**

- **Multi-language Support**: FAQs can be translated into multiple languages (e.g., English, Hindi, Bengali).
- **WYSIWYG Editor**: Rich text formatting for FAQ answers using `django-ckeditor`.
- **REST API**: Retrieve FAQs with language-specific translations via query parameters.
- **Caching**: Improved performance using Redis for caching translations.
- **Admin Panel**: User-friendly interface for managing FAQs.
- **Docker Support**: Easy deployment using Docker and Docker Compose.

---

## **Prerequisites**

- Python 3.8+
- Docker (optional, for containerized deployment)
- Redis (for caching)

---

## **Installation**

### **1. Clone the Repository**

```
git clone https://github.com/your-username/faq-project.git
cd faq-project
2. Set Up a Virtual Environment

python -m venv venv

On Windows: venv\Scripts\activate
On macOS/Linux: source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt
Running the Project
1. Run Redis
Start a Redis server using Docker: docker run -d -p 6379:6379 redis

2. Apply Migrations

python manage.py migrate
3. Create a Superuser

python manage.py createsuperuser
4. Start the Development Server

python manage.py runserver
5. Access the Application
Home Page: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin/

API Endpoint: http://127.0.0.1:8000/api/faqs/

API Usage
Retrieve FAQs
Default (English):

GET /api/faqs/
Hindi:

GET /api/faqs/?lang=hi
Bengali:

GET /api/faqs/?lang=bn
Docker Deployment
1. Build and Run the Containers

docker-compose up --build
2. Apply Migrations

docker-compose exec web python manage.py migrate
3. Create a Superuser

docker-compose exec web python manage.py createsuperuser
4. Access the Application
Home Page: http://localhost:8000/

Admin Panel: http://localhost:8000/admin/

API Endpoint: http://localhost:8000/api/faqs/

Testing
Run Unit Tests
python manage.py test
Contributing
Fork the repository.
Create a new branch:
git checkout -b feature/your-feature-name
Commit your changes:
git commit -m "feat: Add your feature"
Push to the branch:

git push origin feature/your-feature-name
```
