# Portfolio Multipage Django App

**Description:**  
This is a **multi-page Django web application** designed to showcase a portfolio with an integrated chatbot feature. It demonstrates modular Django development, combining dynamic content management with interactive frontend components.

---

## Features

- Multi-page portfolio site (Home, About, Projects, Contact, etc.)
- Interactive chatbot feature (`chatbot` app)
- Database-backed content using SQLite (`db.sqlite3`)
- Static files management (CSS, JS, images)
- HTML templates for dynamic page rendering
- Built with **Django 5.2.6**
- Ready for deployment on PythonAnywhere or any WSGI-compatible server

---

## Project Structure

portfolio_multipage/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── main/ # Core Django app for pages and views
├── chatbot/ # App handling chatbot functionality
├── portfolio_site/ # Django project folder (settings, urls, wsgi)
├── static/ # CSS, JS, and images
├── templates/ # HTML templates
└── venv/ # Python virtual environment (excluded from Git)

