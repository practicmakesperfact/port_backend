# Portfolio Backend API

A Django REST API backend for a personal portfolio website with contact form, projects management, and profile data.

## 🚀 Features

- **Contact Form** - Email notifications with Django's built-in email system
- **Projects Management** - CRUD operations for portfolio projects with image uploads
- **Profile Management** - Personal information and skills management
- **Skills Management** - Technical skills categorization
- **Media File Handling** - Image uploads and serving
- **Admin Panel** - Django admin for content management

## 🛠️ Tech Stack

- **Backend**: Django 4.2+
- **Database**: SQLite (development)
- **Email**: Django Email Backend
- **File Storage**: Django Media Files
- **API**: Django REST Framework style endpoints

## 📋 Prerequisites

- Python 3.8+
- pip package manager
- Gmail account (for email notifications)

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <your-backend-repo-url>
cd portfolio-backend
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Setup
Create a `.env` file with the following:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=your-email@gmail.com
CONTACT_EMAIL=your-email@gmail.com
```

### 5. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000`

## 📡 API Endpoints

### Projects
- `GET /api/projects/data/` - Get all projects
- Admin panel available at `/admin/projects/project/`

### Profile
- `GET /api/profile/data/` - Get profile information
- Admin panel available at `/admin/profiles/`

### Skills
- `GET /api/skills/data/` - Get all skills
- Admin panel available at `/admin/skills/`

### Contact
- `POST /api/contact/` - Submit contact form
- Admin panel available at `/admin/contact/`

## 📧 Email Configuration

### Gmail Setup
1. Enable 2-Factor Authentication on your Gmail account
2. Generate an App Password:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate a new app password
3. Use the app password in `EMAIL_HOST_PASSWORD`

### Email Features
- Automatic email notifications for contact form submissions
- Professional email templates
- Error handling and logging

## 🖼️ Media Files

### Project Images
- Upload project images via Django admin
- Images are served from `/media/`
- Supported formats: JPG, PNG, AVIF
- Automatic image optimization

### File Structure
```
media/
├── projects/
│   ├── project1.jpg
│   └── project2.png
└── profile/
    └── profile.jpg
```

## 🔧 Development

### Running Tests
```bash
python manage.py test
```

### Database Reset
```bash
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Collect Static Files
```bash
python manage.py collectstatic
```

## 📝 Admin Panel

Access the Django admin panel at `http://localhost:8000/admin/`

### Features:
- Manage projects and their images
- Edit profile information
- Organize skills by category
- View contact form submissions
- Full CRUD operations

## 🚀 Deployment

### Environment Variables
Set `DEBUG=False` in production:
```env
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

### Static Files
Configure static files serving for production:
```python
STATIC_ROOT = '/path/to/static/files'
MEDIA_ROOT = '/path/to/media/files'
```

### Security
- Use environment variables for sensitive data
- Configure CORS for frontend domain
- Set up SSL/HTTPS
- Use strong secret keys

## 📊 Project Structure

```
portfolio-backend/
├── manage.py              # Django management script
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables
├── db.sqlite3            # SQLite database
├── portfolio/            # Main Django project
│   ├── settings.py      # Django settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI configuration
├── projects/             # Projects app
│   ├── models.py        # Project models
│   ├── views.py         # Project views
│   └── urls.py          # Project URLs
├── profiles/             # Profile app
├── skills/               # Skills app
├── contact/              # Contact app
└── media/                # Uploaded files
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For issues and questions:
- Create an issue in the repository
- Contact via the portfolio website contact form

---

**Built with Django ❤️**
