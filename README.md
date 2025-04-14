# 🍽️ Restaurant Website

A full-featured **restaurant website** built with **Django** and **Bootstrap**, providing users with an intuitive experience to explore the menu, book tables, and submit feedback.

---

## 📌 Features

### 🏠 Home Page
- Dynamic **carousel slider** showcasing restaurant offers.
- Featured **discounts** and promotional offers.
- Engaging **about section** introducing the restaurant.

### 🍕 Menu Page
- Displays **food categories** and items dynamically.
- Uses **filters** to categorize menu items.
- Each item includes **image, name, description, and price**.

### 📅 Table Booking
- Users can **reserve a table** by providing their details.
- Includes fields for **name, phone number, email, number of persons, and date**.

### ⭐ Customer Feedback
- Customers can **submit reviews** with images and ratings.
- Displays customer reviews dynamically on the **client section**.

### 🖼️ Media Handling
- **Django ImageField** is used to store images.
- Uploaded images are saved inside the `/media/feedback_images/` directory.

### 🔍 Search Functionality
- Users can **search menu items** from the navigation bar.

---

## 🛠️ Technologies Used

### Backend:
- **Django** (Python web framework)
- **SQLite** (Default Django database for development)

### Frontend:
- **Bootstrap** (for styling and responsiveness)
- **HTML/CSS/JavaScript** (for dynamic content rendering)

---

## 🚀 Installation Guide

1️⃣ **Clone the repository:**
```sh
git clone https://github.com/AbdullahRFA/Restaurants_website_project_django.git
cd restaurant-website
```

2️⃣ **Create a virtual environment and activate it:**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3️⃣ **Install dependencies:**
```sh
pip install -r requirements.txt
```

4️⃣ **Run database migrations:**
```sh
python manage.py makemigrations
python manage.py migrate
```

5️⃣ **Create a superuser (optional, for admin access):**
```sh
python manage.py createsuperuser
```

6️⃣ **Run the development server:**
```sh
python manage.py runserver
```

7️⃣ **Access the website at:**
```
http://127.0.0.1:8000/
```

---

## 📂 Project Structure
```
restaurant_project/
│── Base_App/                 # Main Django app
│   │── models.py             # Database models
│   │── views.py              # Django views
│   │── urls.py               # URL routing
│
│── media/                    # Stores uploaded images (Feedback images, Menu images)
│── static/                   # Static assets
│── templates/                # HTML templates
│── db.sqlite3                 # SQLite Database
│── manage.py                  # Django project manager
│── requirements.txt           # Required dependencies
```

---

## ⚙️ Configuration

### 📸 Serving Media Files in Development
Make sure you configure **media settings** in `settings.py`:
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

And include this in `urls.py`:
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 🛠️ Future Improvements
- ✅ **Implement a cart system** for ordering food.
- ✅ **Enhance search functionality** for menu items.
- ✅ **Improve UI/UX** with animations and transitions.
- ✅ **Implement a payment gateway** for online ordering.

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## 🤝 Contributing
Feel free to **fork this repository** and submit a pull request with improvements. 🚀

---


