---

# 🌐 Flask MySQL Web Application

A **beginner-friendly Flask project** that demonstrates how to build a simple web application using **Flask (Python)** and **MySQL** for database connectivity.
This project covers **form submission**, **data storage**, and **success page rendering** — making it a great starting point for learning full-stack web development with Python.

---

## ✅ Features

* ⚙️ Flask-based lightweight backend
* 🗄️ MySQL database integration
* 📥 User data submission via HTML form
* ✅ Success page confirmation
* 🎨 Clean and modern UI using **Bootstrap 5**, **FontAwesome**, and **Google Fonts**
* 💾 Proper database connection handling and error control

---

## 🧩 Technologies Used

| Category          | Technology                      |
| ----------------- | ------------------------------- |
| **Backend**       | Python, Flask                   |
| **Database**      | MySQL                           |
| **Frontend**      | HTML, CSS, Bootstrap 5          |
| **IDE**           | VS Code / PyCharm (recommended) |

---

## 💡 Project Structure

```
flask-mysql-app/
├── templates/
│   └── index.html
├── app.py
└── README.md
```

* **app.py** → Main Flask application (routes, DB connection, and logic)
* **index.html** → User form template (Bootstrap-styled)
* **README.md** → Project documentation

---

## 🚀 How It Works

1. **User Input:**
   The user enters their **name** and **email** in the form.

2. **Data Submission:**
   When submitted, Flask processes the POST request and inserts data into the MySQL table `users`.

3. **Success Message:**
   Upon successful data storage, a confirmation message is displayed.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/seshathri044/flask-mysql-app.git
cd flask-mysql-app
```

### 2️⃣ Install Dependencies

```bash
pip install flask mysql-connector-python
```

### 3️⃣ Configure Database Connection

In `app.py`, update your MySQL credentials:

```python
connection = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='your_DB'
)
```

### 4️⃣ Create Database & Table

```sql
CREATE DATABASE your_DB;
USE your_DB;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
```

### 5️⃣ Run the Application

```bash
python app.py
```

Then open your browser at 👉 **[http://localhost:5000](http://localhost:5000)**

---

## 🧠 Learning Objectives

* Understand how **Flask handles routes and templates**
* Learn **form submission and POST requests**
* Practice **MySQL database connectivity** with Python
* Design responsive UI with **Bootstrap 5**
* Implement **error handling** and clean code structure

---

## 👨‍💻 Author

**Seshathri**
🔗 [GitHub Profile](https://github.com/seshathri044)

> ⭐ If you found this helpful, don’t forget to **star** the repository and share it!

---
