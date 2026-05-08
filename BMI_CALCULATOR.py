import streamlit as st
from datetime import datetime
st.title("Maintenance Calorie Calculator")
Name=st.text_input("Enter Your Name")
age=st.number_input("Enter your Age",min_value=10,max_value=50)
gender=st.radio("Gender",["Male","Female"])
height=st.number_input("Enter your Height in cm")
weight=st.number_input("Enter your Weight in kg")
activity_level=st.radio("Enter your activity level",["sedentary","lightly active","Moderately active","very active","Extra active"],horizontal=True)

if height == 0 or weight == 0:
    st.error("Please enter height and weight")
    st.stop()

if age<10:
    st.error("Please enter a valid age")
    st.stop()

if st.button("submit"):
    if gender=="Male":
        BMR = (10*weight)+(6.25*height)-(5*age)+5
    elif gender=="Female":
        BMR = (10*weight)+(6.25*height)-(5*age)-161
    ans=BMR
    st.success(f"your BMR is:{ans} kcal")

    activity_values={"sedentary":1.2,"lightly active":1.375,"Moderately active":1.55,"very active":1.725,"Extra active":1.9}
    maintenance_calorie=BMR*activity_values[activity_level]
    st.success(f"To maintain this weight take {maintenance_calorie} kcal/day")
    st.info(f"Weight loss calories: {maintenance_calorie-500:} kcal/day")
    st.info(f"Weight gain calories: {maintenance_calorie+500:} kcal/day")

    log_message =Name,age,gender,BMR
    with open("app.log", "a") as file:  
        file.write(f"{log_message} - {datetime.now()}\n")