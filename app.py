import time

import streamlit as st
# title
st.title("start dashbord")
# header
st.header("i am learn stam ")
st.header("this is a header")
# st.write
st.write("this is a write function")

# markdown
st.markdown("""
### my fav movie 
- irom man 1 
- avenger end game 
## fav hero 
- asur
- money heist
""")
st.code("""
def v(i):
return i
v(2)
""")

# latex
st.latex("x^2+y^2+4=0"
         ""
         "log(x)")
### display element ###

# dataframe
# metrics
# JSON

import pandas as pd
df = pd.DataFrame({"name":["hima","kumar"],
                   "age":[12,13]})
print(df)

st.dataframe(df)
# matric

import numpy as np

mat = np.arange(12).reshape(3,4)

print(mat)
st.metric("revenue",33,'3%')

# JSON



df = pd.DataFrame({
    "name": ["hima", "kumar"],
    "age": [12, 13]
})

# Convert DataFrame to a list of dictionaries (valid JSON format)
json_data = df.to_dict(orient="records")

# Show as JSON
st.json({
    "name": ["hima", "kumar"],
    "age": [12, 13]
})
# dislaying media
st.image('Screenshot (1).png')

# creating layouts
st.sidebar.title("side_bar")

# add a mutiple column

col1,col2=st.columns(2)
with col1:
    st.image('screenshot (1).png')
with col2:
    st.image('screenshot (1).png')


# showing status
# - progress bar
# - error message -> success


st.error('login_failed')

st.success("login sucessful")
st.info("login")
st.warning("warning")


### progress bar
bar = st.progress(0)

for i in range(1, 101):
    time.sleep(0.0000001)  # Sleep for 0.1 seconds (100ms)
    bar.progress(i)

### taking user input


email = st.text_input("enter email")
num = st.number_input("age")
date = st.date_input("enter date ")

import pandas as pd
import streamlit as st
st.header("hello")
email = st.text_input("enter your email")
password = st.text_input("enter your password")
gender =st.selectbox("select gender",["male",'female'])

bt = st.button("login")
# code excute when bt is click
# if the button is click
if bt:
    if email=="hima@gmail.com" and password=="1298":
        st.success("login successful")
        st.balloons()
        st.write(gender)
    else:
        st.error("write correct password")
import pandas as pd
# file uploader
file = st.file_uploader("upload csv file ")
if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df.describe())



