# 🔐 Secure File Sharing System 

A secure file-sharing backend system built using **FastAPI** and **MongoDB**, with role-based authentication, file uploads, and secure download links.

---
## 🧪 API Testing

A complete Postman collection is included:

📄 `secure-file-sharing.postman_collection.json`

You can import it into Postman to test all key endpoints: signup, login, upload, and secure download.


## ✅ Features

- 🔐 JWT-based login/signup system
- 🧾 Role-based access control (`ops`, `client`)
- 📤 Upload support (`.docx`, `.pptx`, `.xlsx`) for Ops
- 🔗 Secure encrypted download links for Clients
- 🌐 Fully documented Swagger UI: `http://127.0.0.1:8000/docs`

---


## 🛠 Setup Instructions

### 1. Clone & Install
```bash
cd secure-file-share
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
