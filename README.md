# 🧠 MediMind AI

### Smart AI Healthcare Disease Prediction System

MediMind AI is an intelligent healthcare web application that predicts possible diseases based on user-selected symptoms using Machine Learning.
The system also provides **confidence levels**, **diet recommendations**, and **personal prediction history** for users.

This project was developed as part of an academic project at **VIT-AP University**.

---

# 🚀 Features

* 🔐 **User Authentication**

  * Login
  * Register new users

* 🤒 **Disease Prediction**

  * Select symptoms from a list
  * Machine Learning model predicts top diseases
  * Displays **Top 3 predicted diseases**

* 📊 **Confidence Levels**

  * Shows probability of each predicted disease

* 🍽 **Food Recommendations**

  * Foods to **eat**
  * Foods to **avoid**

* 📜 **Prediction History**

  * Stores user predictions
  * Users can view past results
  * Option to delete history instantly

* 💻 **Developer Panel**

  * Displays project contributors

* 🌙 **Dark Theme Interface**

  * Modern healthcare UI
  * Gradient prediction cards

---

# 🧠 Machine Learning Model

The disease prediction model was trained using symptom data.

**Libraries used for training:**

* Scikit-learn
* NumPy
* Pandas

The model predicts diseases based on **binary symptom inputs**.

---

# 🛠 Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Backend logic             |
| Streamlit    | Web application framework |
| Scikit-learn | Machine learning model    |
| NumPy        | Data processing           |
| Joblib       | Model storage             |
| JSON         | User & history storage    |

---

# 📂 Project Structure

```
MediMind-AI
│
├── app.py
├── disease_model.pkl
├── label_encoder.pkl
├── symptom_columns.pkl
│
├── users.json
├── history.json
│
└── README.md
```

---

# ⚙ Installation

1️⃣ Clone the repository

```
git clone https://github.com/yourusername/MediMind-AI.git
```

2️⃣ Navigate to the project folder

```
cd MediMind-AI
```

3️⃣ Install required libraries

```
pip install streamlit numpy scikit-learn joblib
```

4️⃣ Run the application

```
streamlit run app.py
```

---

# 📸 Application Workflow

1. Open the application
2. Click **Get Started**
3. Login or Register
4. Select symptoms
5. Click **Predict Disease**
6. View predictions and recommendations

---

# 👩‍💻 Developers

* **Lohitha** – 24MIC7274
* **Divya** – 22MIC7157
* **Satya Sahithi** – 22MIC7064

VIT-AP University

---

# ⚠ Disclaimer

This application is developed **for educational purposes only**.
The predictions are generated using a machine learning model and **should not replace professional medical advice**.
Always consult a qualified doctor for proper diagnosis and treatment.

---

# ⭐ Future Improvements

* AI chatbot for health queries
* Doctor appointment integration
* Real-time symptom analysis
* Mobile responsive interface
* Medical dataset expansion

---

# 📜 License

This project is for academic and educational use.
