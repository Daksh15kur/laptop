import streamlit as st
import pickle
import numpy as np

# Load the trained model (ensure DT.pkl exists in the correct directory)
with open("DT.pkl", "rb") as f:
    model = pickle.load(f)

# Dictionary mappings for categorical features
company_dict = {"Dell": 0, "HP": 1, "Apple": 2, "Asus": 3, "Lenovo": 4,"Acer":5}
type_dict = {"Notebook": 0, "Ultrabook": 1, "Gaming": 2, "2-in-1 Convertible": 3, "Workstation": 4}
cpu_dict = {"Intel": 0, "AMD": 1, "Other": 2}
gpu_dict = {"Intel": 0, "Nvidia": 1, "AMD": 2, "Other": 3}
os_dict = {"Windows": 0, "MacOS": 1, "Linux": 2, "Other": 3}

# Streamlit UI elements
st.title("Laptop Price Prediction App")
company = st.selectbox("Select Company", options=list(company_dict.keys()))
TypeName = st.selectbox("Select Type", options=list(type_dict.keys()))
Inches = st.number_input("Enter Screen Size (Inches)", min_value=10.0, max_value=20.0, step=0.1)
RAM = st.number_input("Enter RAM (GB)", min_value=4, max_value=64)
Weight = st.number_input("Enter Weight (kg)", min_value=0.5, max_value=5.0, step=0.1)
TouchScreen = st.selectbox("Touchscreen", options=[0, 1])  # 0 for No, 1 for Yes
FullHD = st.selectbox("Full HD", options=[0, 1])  # 0 for No, 1 for Yes
IPS = st.selectbox("IPS", options=[0, 1])  # 0 for No, 1 for Yes
X_res = st.number_input("Enter X Resolution", min_value=800, max_value=4000)
Y_res = st.number_input("Enter Y Resolution", min_value=600, max_value=3000)
first = st.number_input("Enter First space ", min_value=0, max_value=512)
second = st.number_input("Enter Second space", min_value=0, max_value=512)
HDD = st.selectbox(" HDD ", options=[0,1])
SSD = st.selectbox(" SSD ",options=[0,1])
Flash = st.number_input("Enter Flash Storage (GB)", min_value=0, max_value=512)
Hybrid = st.number_input("Enter Hybrid Storage (GB)", min_value=0, max_value=2000)
CPU = st.selectbox("Select CPU", options=list(cpu_dict.keys()))
Graphics = st.selectbox("Select GPU", options=list(gpu_dict.keys()))
OPSystem = st.selectbox("Select Operating System", options=list(os_dict.keys()))

# Create a button to trigger prediction
if st.button("Predict Price"):
    # Convert the categorical inputs using the predefined mappings
    input_data = np.array([[company_dict[company], type_dict[TypeName], Inches, RAM, Weight, TouchScreen, FullHD, IPS,
                            X_res, Y_res, first, second, HDD, SSD, Flash, Hybrid, cpu_dict[CPU], gpu_dict[Graphics], os_dict[OPSystem]]])

    # Make prediction
    prediction = model.predict(input_data)

    # Display the predicted price
    st.success(f"Predicted Price: Rs.{prediction[0]:.2f}")
