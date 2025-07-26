# Mamar Bank

A modern, full-featured Django banking web application for user registration, authentication, and account management.

## Features
- User registration with custom fields (account type, gender, address, etc.)
- Secure login/logout with Django authentication
- Profile page with user details
- Landing page/dashboard with quick access to Report, Withdraw, Deposit
- Responsive, professional UI using Tailwind CSS
- Custom navigation bar with dynamic links based on authentication
- Withdraw, Deposit, and Report placeholder pages (ready for business logic)

## Project Structure
```
mamar_bank/
├── accounts/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── accounts/
│           ├── login.html
│           ├── user_registration.html
│           ├── profile.html
│           ├── withdraw.html
│           ├── deposit.html
│           └── report.html
├── core/
│   └── templates/
│       ├── base.html
│       ├── navbar.html
│       └── landing.html
├── mamar_bank/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── db.sqlite3
├── manage.py
└── README.md
```

## Setup Instructions
1. **Clone the repository**
2. **Install dependencies**
   - Python 3.11+
   - Django 5.x
   - `pip install django django-widget-tweaks`
3. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```
5. **Run the development server**
   ```bash
   python manage.py runserver
   ```
6. **Access the app**
   - Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser

## Usage
- Register a new user via the registration page
- Login to access the dashboard and profile
- Use the navigation bar to access Report, Withdraw, Deposit, Profile, and Logout

## Customization
- Update `accounts/views.py` to add business logic for Withdraw, Deposit, and Report
- Edit `core/templates/landing.html` for dashboard content
- Modify `core/templates/navbar.html` for navigation changes

## License
This project is for educational purposes.
