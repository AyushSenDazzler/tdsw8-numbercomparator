import streamlit as st

st.write("""
# Determine the largest number

This app shows largest among the given 3 numbers
""")

st.header('Input the numbers in the field below')

def largest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
        
first_num = st.number_input("First Number")
second_num = st.number_input("Second Number")
third_num = st.number_input("Third Number")

if st.button("Find largest number"):
    result = largest_number(num1, num2, num3)
    st.success("The largest among all is: {}".format(result))
    











