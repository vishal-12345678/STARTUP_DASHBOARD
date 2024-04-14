import streamlit as st
import pandas as pd
import time
#1)title
st.title('Startup Dashboard')   # title fuction to add title

#2)header
st.header('this is header')     # header function to a header in the website

#3)subheader
st.subheader('this is subheader')  # subheader will add a subheader in the website

#4)write
st.write('this is just write command text')  # write function to add write into website like a paragraph or simple writing

#5)to add a list into the website with bulletpoint markdown is very useful function
st.markdown("""
### this is markdown list
- elon musk
- jenson huang
- steve jobs
""")

#6)to put code
st.code("""
def foo(input):
  square=input**2
  return square
""")

#7)latex function to convert eqaution to proper math equation
st.latex('ax*2 + bx*2=c')

#8) to create a dataframe pass a row in ech key
df = pd.DataFrame({
    'name': ['Nitish', 'Ankit', 'Anupam'],
    'marks': [50, 60, 70],
    'package': [10, 12, 14]
})

st.dataframe(df)

#9)to print metric to enter a card into webpage

st.metric('Revenue', 'Rs 3L', '-3%')

#10)to enter jason into the webpage jason is a dictionary just like dataframe

st.json({
    'name': ['Nitish', 'Ankit', 'Anupam'],
    'marks': [50, 60, 70],
    'package': [10, 12, 14]
})

#11)to enter side bar into the page
st.sidebar.title('Sidebar ka Title')

#12)to enter column side by side and put some value in them
col1, col2, col3 = st.columns(3)

with col1:
    st.metric('Revenue', 'Rs 3L', '-3%')

with col2:
    st.metric('profit', 'Rs 5l', '-6%')

with col3:
    st.metric('loss', 'Rs 10l', '-8%')

#12) error and succes commands
st.error('Login Failed')
st.success('Login Successful')

st.info('Login Successful')

st.warning('Login Successful')

#13)to put a progress bar inside the website
bar = st.progress(0)

for i in range(1, 50):
    bar.progress(i)

#14)to take something as input text_input command and selectbox command

email = st.text_input('Enter email')
number = st.number_input('Enter age')
st.date_input('Enter regis date')
gender = st.selectbox('Select gender',['male','female','others'])
password=st.text_input('enter the pass')

#15)to put a button in web page if we clicked it what will happens

btn = st.button('Login Karo')
# if the button is clicked
if btn:
    if email == 'nitish@gmail.com' and password == '1234':
        st.balloons()
        st.write(gender)
    else:
        st.error('Login Failed')

#16 to upload a file
file = st.file_uploader('Upload a csv file')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())






