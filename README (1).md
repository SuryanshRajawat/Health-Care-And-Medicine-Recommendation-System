
# 🏥 Medical Recommendation System using Flask, AI & ML

This project is a Medical Recommendation System built using **Python**, **Flask**, **Machine Learning**, and **AI**. It allows users to register, log in, and receive health-related recommendations based on input symptoms.

---

## 🔧 Features

- User authentication system (Sign Up / Log In)
- Symptom-based medical recommendation using ML
- Flask-based web interface
- Secure password hashing and input validation
- User dashboard to manage inputs and results
- Optionally: export recommendation, email notification

---

## 📁 Project Structure

```
medical-recommendation-system/
├── app.py                # Main Flask app
├── model.pkl             # Trained ML model
├── static/               # Static files (CSS, JS, images)
├── templates/            # HTML templates (login.html, signup.html, dashboard.html)
├── users.db              # Database (SQLite or other)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🚀 Getting Started

1. **Clone the repository**  
```bash
git clone https://github.com/yourusername/medical-recommendation-system.git
cd medical-recommendation-system
```

2. **Create virtual environment**  
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**  
```bash
pip install -r requirements.txt
```

4. **Run the Flask App**  
```bash
python app.py
```

---

## ⚙️ Technologies Used

- Python
- Flask
- Scikit-learn / Pandas
- HTML / CSS / JS
- SQLite / PostgreSQL (optional)

---

## ✅ To Do

- [ ] Improve UI with Bootstrap/Tailwind
- [ ] Deploy on Heroku/Render
- [ ] Add user-specific recommendation history
- [ ] Chatbot or real-time doctor support

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👤 Author

Your Name – [your.email@example.com](mailto:your.email@example.com)
