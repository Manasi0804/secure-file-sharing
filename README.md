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

## ⚠️ Testing Note

Due to a local issue with MongoDB startup (`WinError 10061` / `1067`), I was unable to fully test the API endpoints on my system.

However:
- All backend logic and route structures are implemented as per the requirements
- API responses were verified manually using Swagger UI where possible
- A complete Postman collection (`secure-file-sharing.postman_collection.json`) is included for easy testing
- The `tests/` folder contains test cases written using `pytest` and FastAPI’s TestClient

You can easily run and test the API by starting the MongoDB service and running the FastAPI app.

