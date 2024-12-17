import streamlit as st
import pandas as pd

st.title("HI this is sujit" )

st.subheader("hi this is that")

st.header("I am new header")

st.text("hi i am text function and programmers uses")

st.markdown("**Hello ** World")

code = """

print("hello world")
def fuct():
return 0;
"""

table = pd.DataFrame({'columns 1': [1, 2, 3] , "columns 2": [2, 3, 4]})
st.code(code ,language='python')
st.write('## H2')
st.metric(label="Window Speed" , value='120ms' , delta='1.4ms')
st.table(table)