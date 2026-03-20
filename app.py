import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Health Assistant",
    page_icon="🧑‍⚕️",
    layout="wide"
)

# --------------------------------------------------
# Load Models
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_model(model_name):
    with open(os.path.join(BASE_DIR, model_name), "rb") as file:
        return pickle.load(file)

diabetes_model = load_model("diabetes_model.sav")
heart_disease_model = load_model("heart_disease_model.sav")
parkinsons_model = load_model("parkinsons_model.sav")

# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------
with st.sidebar:
    selected = option_menu(
        menu_title="Multiple Disease Prediction System",
        options=[
            "Diabetes Prediction",
            "Heart Disease Prediction",
            "Parkinson's Prediction"
        ],
        icons=["activity", "heart", "person"],
        menu_icon="hospital-fill",
        default_index=0
    )

# ==================================================
# DIABETES PREDICTION
# ==================================================
if selected == "Diabetes Prediction":

    st.title("🩸 Diabetes Prediction using Machine Learning by atifali")

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
        SkinThickness = st.number_input("Skin Thickness", min_value=0.0)
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0)

    with col2:
        Glucose = st.number_input("Glucose Level", min_value=0.0)
        Insulin = st.number_input("Insulin Level", min_value=0.0)
        Age = st.number_input("Age", min_value=1, step=1)

    with col3:
        BloodPressure = st.number_input("Blood Pressure", min_value=0.0)
        BMI = st.number_input("BMI", min_value=0.0)

    if st.button("🔍 Diabetes Test Result"):
        input_data = np.array([[Pregnancies, Glucose, BloodPressure,
                                SkinThickness, Insulin, BMI,
                                DiabetesPedigreeFunction, Age]])

        prediction = diabetes_model.predict(input_data)

        if prediction[0] == 1:
            st.error("⚠️ The person is likely Diabetic")
        else:
            st.success("✅ The person is NOT Diabetic")

# ==================================================
# HEART DISEASE PREDICTION
# ==================================================
if selected == "Heart Disease Prediction":

    st.title("❤️ Heart Disease Prediction using Machine Learning by Atifali")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", min_value=1, step=1)
        trestbps = st.number_input("Resting Blood Pressure", min_value=0.0)
        restecg = st.number_input("Resting ECG", min_value=0.0)
        oldpeak = st.number_input("ST Depression", min_value=0.0)
        ca = st.number_input("Major Vessels", min_value=0.0)

    with col2:
        sex = st.number_input("Sex (1 = Male, 0 = Female)", min_value=0, max_value=1)
        chol = st.number_input("Cholesterol", min_value=0.0)
        thalach = st.number_input("Max Heart Rate", min_value=0.0)
        slope = st.number_input("Slope", min_value=0.0)
        thal = st.number_input("Thal", min_value=0.0)

    with col3:
        cp = st.number_input("Chest Pain Type", min_value=0.0)
        fbs = st.number_input("Fasting Blood Sugar", min_value=0.0)
        exang = st.number_input("Exercise Induced Angina", min_value=0.0)

    if st.button("🔍 Heart Disease Test Result"):
        input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                                restecg, thalach, exang, oldpeak,
                                slope, ca, thal]])

        prediction = heart_disease_model.predict(input_data)

        if prediction[0] == 1:
            st.error("⚠️ The person is likely to have Heart Disease")
        else:
            st.success("✅ The person does NOT have Heart Disease")

# ==================================================
# PARKINSON'S DISEASE PREDICTION
# ==================================================
if selected == "Parkinson's Prediction":

    st.title("🧠 Parkinson's Disease Prediction using Machine Learning by atifali   ")

    cols = st.columns(5)

    features = []
    labels = [
        "Fo(Hz)", "Fhi(Hz)", "Flo(Hz)", "Jitter(%)", "Jitter(Abs)",
        "RAP", "PPQ", "DDP", "Shimmer", "Shimmer(dB)",
        "APQ3", "APQ5", "APQ", "DDA", "NHR",
        "HNR", "RPDE", "DFA", "Spread1", "Spread2",
        "D2", "PPE"
    ]

    for i, label in enumerate(labels):
        with cols[i % 5]:
            features.append(st.number_input(label, value=0.0))

    if st.button("🔍 Parkinson's Test Result"):
        input_data = np.array([features])
        prediction = parkinsons_model.predict(input_data)

        if prediction[0] == 1:
            st.error("⚠️ The person is likely to have Parkinson's Disease")
        else:
            st.success("✅ The person does NOT have Parkinson's Disease")
<<<<<<< HEAD
#1234567890987ygggjnfdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddrre245678
#123456789erfvcrfvgit add .
=======
import math

class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b


class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return 0.5 * self.b * self.h


# Example
shapes = [
    Circle(5),
    Square(4),
    Rectangle(5, 3),
    Triangle(6, 2)
]

for shape in shapes:
    print("Area:", shape.area())
>>>>>>> b5a7fc2ab14cb186f692355767353b83b801389d
#234t5ryhgnbfvdewrtyuyjhgtryuyi 
# my self md from mgmmu jnec i wanted to crack gsoc any how ::""oifhaoaifhwoeifhweoi
hklhklhodhfihso;ifh
akjsfbkajbfboahfoia
jnfnklksklfkhseoi;f

skjfhoifh;oihfaed
