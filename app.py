import streamlit as st

st.write("""
# Find the largest number

Enter three numbers and find largest among them
""")

def largest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
        
first_num = st.number_input("Enter first Number", value=0, step=1, format="%d", value_type="int")
second_num = st.number_input("Enter second Number", value=0, step=1, format="%d", value_type="int")
third_num = st.number_input(("Enter third Number", value=0, step=1, format="%d", value_type="int")

if st.button("Find largest number"):
    result = largest_number(first_num,second_num,third_num)
    st.success("The largest among all is: {}".format(result))
    











