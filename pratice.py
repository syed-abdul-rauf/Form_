import pyodbc
import streamlit as st
import time
connection_string = "DRIVER={SQL SERVER};SERVER=LAPTOP-ECFADG26\SQLEXPRESS;DATABASE=FORM;Trusted_connection=yes"
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

st.title("FORM!!!!")

Name = st.text_input("Enter your Name:")
Phone_number = st.text_input("Enter your Phone number:")


try:
        if st.checkbox("Is the webpage good."):
            st.text("thanks for your feedback!!!👍😍👌💕😁")
            st.balloons()

        if st.checkbox("Is the webpage bad."):
            st.text("thanks for your feedback!!!😒😒😒😒😒")
except:
        st.text("Please click on the feedback icon")





if st.button("Submit"):
    try:
        connection.execute("INSERT INTO Verification_form (Name, Phone_number) VALUES(?, ?)", (Name, Phone_number))
        connection.commit()
        st.success("data transfered")
    except:
        st.error("Something went wrong please check your program")