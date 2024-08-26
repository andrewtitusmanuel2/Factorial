import streamlit as st

st.header("Calculator APP")
st.write("This app is created by Andrew Titus Manuel")

num1 = st.number_input(label="Enter the first number",value=0,min_value=0)
btn = st.button("Calculate")

def factorial(num1):
  i=1
  result=1
  while i<=num1:
    result=result*i
    i=i+1
  return(result)

if btn:

  y= factorial(num1)
st.header(f'Factorial of {num1} is {y}')