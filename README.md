# 🎓 Student Scholarship Application and Disbursement Tracker

## 📖 Overview

The **Student Scholarship Application and Disbursement Tracker** is a full-stack web application designed to simplify the scholarship application and management process for educational institutions. The system allows students to apply for scholarships online while enabling administrators to manage, verify, approve, and monitor scholarship applications through an intuitive dashboard.

The project is developed using **FastAPI**, **SQLite**, **SQLAlchemy**, **HTML**, **CSS**, and **JavaScript**, with an integrated **AI-powered Scholarship Assistant** for answering scholarship-related queries.

---

## ✨ Features

### 👨‍🎓 Student Module

- Student Login
- Student Dashboard
- View Student Profile
- Apply for Scholarships
- View My Applications
- Track Application Status
- View Application Details

### 👨‍💼 Admin Module

- Admin Login
- Dashboard with Statistics
- View All Applications
- Search Applications
- Filter Applications by Status
- Update Application Status
- Delete Applications
- View Application History

### 🤖 AI Scholarship Assistant

- Answer scholarship-related questions
- Display scholarship information
- Provide application statistics
- Assist administrators with quick queries

---

## 🛠️ Technology Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- FastAPI
- SQLAlchemy
- Pydantic

### Database
- SQLite

### Tools
- VS Code
- Git & GitHub

---

## 📁 Project Structure

```
Student-Scholarship-Application-and-Disbursement-Tracker
│
├── Backend
│   ├── assistant.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── seed.py
│   ├── scholarship.db
│   └── requirements.txt
│
├── Frontend
│   ├── css
│   │   └── style.css
│   │
│   ├── html
│   │   ├── login.html
│   │   ├── admin.html
│   │   ├── details.html
│   │   ├── student-login.html
│   │   ├── student-dashboard.html
│   │   ├── apply.html
│   │   └── my-application.html
│   │
│   └── js
│       ├── login.js
│       ├── script.js
│       ├── details.js
│       ├── student-login.js
│       ├── student-dashboard.js
│       ├── apply.js
│       └── my-applications.js
│
└── README.md
```

---

## 🗄️ Database Tables

### Student

| Field | Type |
|-------|------|
| id | Integer |
| name | String |
| department | String |
| year | Integer |

### Scholarship

| Field | Type |
|-------|------|
| id | Integer |
| name | String |
| amount | Integer |

### Application

| Field | Type |
|-------|------|
| id | Integer |
| student_id | Integer |
| scholarship_id | Integer |
| status | String |
| applied_date | String |

### Status History

| Field | Type |
|-------|------|
| id | Integer |
| application_id | Integer |
| status | String |
| updated_date | String |

---

## 🚀 API Endpoints

### Student APIs

| Method | Endpoint |
|---------|----------|
| GET | /students |
| POST | /students |
| GET | /students/{student_id}/applications |

### Scholarship APIs

| Method | Endpoint |
|---------|----------|
| GET | /scholarships |
| POST | /scholarships |

### Application APIs

| Method | Endpoint |
|---------|----------|
| GET | /applications |
| POST | /applications |
| GET | /applications/{id} |
| PUT | /applications/{id} |
| DELETE | /applications/{id} |
| GET | /applications/{id}/history |

### AI Assistant API

| Method | Endpoint |
|---------|----------|
| POST | /assistant |

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Student-Scholarship-Application-and-Disbursement-Tracker.git
```

### Navigate to the Project

```bash
cd Student-Scholarship-Application-and-Disbursement-Tracker
```

---

## 🔧 Backend Setup

Navigate to the backend folder:

```bash
cd Backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

Run the FastAPI server:

```bash
uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

## 💻 Frontend Setup

1. Open the **Frontend** folder in VS Code.
2. Install the **Live Server** extension.
3. Right-click **login.html** or **student-login.html**.
4. Select **Open with Live Server**.

Frontend runs at:

```
http://127.0.0.1:5500
```

or

```
http://127.0.0.1:5501
```

---

## 🔄 Application Workflow

### Student Workflow

```
Student Login
      │
      ▼
Student Dashboard
      │
      ├──────────────┐
      │              │
      ▼              ▼
Apply Scholarship   My Applications
      │              │
      └──────┬───────┘
             ▼
     Application Details
```

### Admin Workflow

```
Admin Login
      │
      ▼
Admin Dashboard
      │
      ├── View Applications
      ├── Search & Filter
      ├── Update Status
      ├── Delete Application
      ├── View History
      └── AI Assistant
```

---

## 📸 Screenshots

Include screenshots of:

- Login Page
- Admin Dashboard
- Student Dashboard
- Apply Scholarship Page
- My Applications
- Application Details
- AI Scholarship Assistant

---

## 🔮 Future Enhancements

- Student Registration
- JWT Authentication
- File Upload for Documents
- Email Notifications
- Scholarship Eligibility Validation
- Mobile Responsive Design
- Admin Report Generation (PDF/Excel)
- Analytics Dashboard

---

## 👩‍💻 Author

**Roopa T**

---

## 📄 License

This project is developed for educational and learning purposes. You are free to modify and extend it for academic or personal use.