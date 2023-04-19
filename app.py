import streamlit as st

st.write("""
# Determine the largest number

This app shows largest among the given 3 numbers
""")

st.header('Input the numbers in the field below')

def largest_number():
    first_num = st.number_input("First Number")
    second_num = st.number_input("Second Number")
    third_num = st.number_input("Third Number")

    numbers = [first_num,second_num,third_num]

    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
            return largest

st.write("""
### The largest among all is : 
""" largest)













