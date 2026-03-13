import streamlit as st
import numpy as np
import joblib
import json
import os
from datetime import datetime

st.set_page_config(
    page_title="MediMind AI",
    page_icon="🧠",
    layout="wide"
)


model = joblib.load("disease_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")
symptom_columns = joblib.load("symptom_columns.pkl")

# ---------------- DATABASE ----------------
USER_FILE = "users.json"
HISTORY_FILE = "history.json"

if not os.path.exists(USER_FILE):
    with open(USER_FILE,"w") as f:
        json.dump({},f)

if not os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE,"w") as f:
        json.dump({},f)

def load_users():
    with open(USER_FILE,"r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE,"w") as f:
        json.dump(users,f)

def load_history():
    with open(HISTORY_FILE,"r") as f:
        return json.load(f)

def save_history(history):
    with open(HISTORY_FILE,"w") as f:
        json.dump(history,f)

# ---------------- FOOD RECOMMENDATIONS ----------------
food_recommendations = {
"AIDS":{"eat":["Fruits","Leafy vegetables"],"avoid":["Raw eggs","Unpasteurized milk"]},
"Diabetes":{"eat":["Whole grains","Vegetables"],"avoid":["Sugary food","Soft drinks"]},
"Tuberculosis":{"eat":["Protein rich food","Nuts"],"avoid":["Alcohol","Fried food"]},
"Migraine":{"eat":["Magnesium foods","Plenty of water"],"avoid":["Caffeine","Processed food"]},
"Typhoid":{"eat":["Boiled vegetables","Rice porridge"],"avoid":["Spicy food","Street food"]},
"Peptic_ulcer":{"eat":["Oatmeal","Bananas"],"avoid":["Alcohol","Spicy food"]},
"Paralysis":{"eat":["High fiber food","Omega 3 rich food"],"avoid":["Salty food","Junk food"]},
"Jaundice":{"eat":["Fresh fruits","Vegetable soup"],"avoid":["Oily food","Alcohol"]}
}


if "page" not in st.session_state:
    st.session_state.page="landing"

if "user" not in st.session_state:
    st.session_state.user=None

st.markdown("""
<style>
body{
background-color:#0e1117;
color:white;
}

.hero{
text-align:center;
padding:120px;
background:linear-gradient(120deg,#0f2027,#203a43,#2c5364);
border-radius:20px;
}

.hero-title{
font-size:60px;
font-weight:800;
background:linear-gradient(90deg,#00c6ff,#0072ff);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.hero-sub{
font-size:20px;
color:#cfd8ff;
margin-top:20px;
}

.prediction-card{
background:linear-gradient(135deg,#00c6ff,#0072ff,#8e2de2);
padding:20px;
border-radius:15px;
margin-top:15px;
color:white;
}

.stButton>button{
background:linear-gradient(45deg,#00c6ff,#0072ff);
border-radius:25px;
padding:10px 30px;
font-size:16px;
color:white;
}
</style>
""",unsafe_allow_html=True)

# ---------------- LANDING PAGE ----------------
if st.session_state.page=="landing":

    st.markdown("""
    <div class="hero">
    <div class="hero-title">MediMind AI</div>
    <div class="hero-sub">
    Smart AI Healthcare Disease Prediction System
    </div>
    </div>
    """,unsafe_allow_html=True)

    col1,col2,col3=st.columns([2,1,2])

    with col2:
        if st.button("🚀 Get Started"):
            st.session_state.page="login"
            st.rerun()

# ---------------- LOGIN PAGE ----------------
elif st.session_state.page=="login":

    st.title("🔐 Login")

    username=st.text_input("Username")
    password=st.text_input("Password",type="password")

    col1,col2=st.columns(2)

    with col1:
        if st.button("Login"):

            users=load_users()

            if username in users and users[username]==password:

                st.session_state.user=username
                st.session_state.page="dashboard"
                st.rerun()

            else:
                st.error("Invalid credentials")

    with col2:
        if st.button("Register"):
            st.session_state.page="register"
            st.rerun()

# ---------------- REGISTER PAGE ----------------
elif st.session_state.page=="register":

    st.title("📝 Register")

    new_user=st.text_input("Create Username")
    new_pass=st.text_input("Create Password",type="password")

    if st.button("Create Account"):

        users=load_users()

        if new_user in users:
            st.warning("User already exists")

        else:
            users[new_user]=new_pass
            save_users(users)

            st.success("Account created")

            st.session_state.page="login"
            st.rerun()

# ---------------- DASHBOARD ----------------
elif st.session_state.page=="dashboard":

    st.title("🩺 MediMind AI")
    st.write(f"Welcome **{st.session_state.user}** 👋")

    menu=st.sidebar.selectbox(
        "Navigation",
        ["Disease Prediction","Past History","Developer Panel","Logout"]
    )

# ---------------- DISEASE PREDICTION ----------------
    if menu=="Disease Prediction":

        st.subheader("🤒 Select Symptoms")

        selected_symptoms=st.multiselect("Choose symptoms",symptom_columns)

        if st.button("🔍 Predict Disease"):

            if len(selected_symptoms)==0:
                st.warning("Please select symptoms")

            else:

                input_vector=np.zeros(len(symptom_columns))

                for symptom in selected_symptoms:
                    input_vector[symptom_columns.index(symptom)]=1

                probabilities=model.predict_proba([input_vector])[0]

                top3=np.argsort(probabilities)[-3:][::-1]

                st.subheader("🧠 Predicted Diseases")

                history=load_history()
                user=st.session_state.user

                for i in top3:

                    disease=label_encoder.inverse_transform([i])[0]
                    confidence=probabilities[i]*100

                    st.markdown(f"""
                    <div class="prediction-card">
                    <h3>{disease}</h3>
                    <p>Confidence: {confidence:.2f}%</p>
                    """,unsafe_allow_html=True)

                    if disease in food_recommendations:

                        eat=", ".join(food_recommendations[disease]["eat"])
                        avoid=", ".join(food_recommendations[disease]["avoid"])

                        st.markdown(f"<p>🍽 Eat: {eat}</p>",unsafe_allow_html=True)
                        st.markdown(f"<p>🚫 Avoid: {avoid}</p>",unsafe_allow_html=True)

                    st.markdown("</div>",unsafe_allow_html=True)

                record={
                "symptoms":selected_symptoms,
                "prediction":disease,
                "confidence":round(confidence,2),
                "date":datetime.now().strftime("%Y-%m-%d %H:%M")
                }

                history.setdefault(user,[]).append(record)
                save_history(history)

# ---------------- HISTORY ----------------
    elif menu=="Past History":

        st.subheader("📜 Your Past History")

        history=load_history()
        user=st.session_state.user

        if user in history and len(history[user])>0:

            for record in history[user]:

                st.write("🕒 Date:",record["date"])
                st.write("🤒 Symptoms:",", ".join(record["symptoms"]))
                st.write("🦠 Prediction:",record["prediction"])
                st.write("📊 Confidence:",record["confidence"],"%")
                st.markdown("---")

            if st.button("🗑 Delete All Past History"):

                history[user]=[]
                save_history(history)

                st.success("History deleted successfully")
                st.rerun()

        else:
            st.info("No past history available")

# ---------------- DEVELOPERS ----------------
    elif menu=="Developer Panel":

        st.subheader("💻 Developers")

        st.markdown("👩‍💻 **Lohitha - 24MIC7274**")
        st.markdown("👩‍💻 **Divya - 22MIC7157**")
        st.markdown("👩‍💻 **Satya Sahithi - 22MIC7064**")

# ---------------- LOGOUT ----------------
    elif menu=="Logout":

        st.session_state.user=None
        st.session_state.page="landing"

        st.success("Logged out successfully")

        st.rerun()

# ---------------- FOOTER ----------------
st.markdown("---")
st.info("⚠️ MediMind AI is for educational purposes only. Always consult a doctor for diagnosis.")