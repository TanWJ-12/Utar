import streamlit as st

#Set the app title
st.title('My first streamlit app')

#streamlit run [filename].py
#display text output
st.write('Welcome to my first streamlit app')

#display a button
st.button("Reset", type = "primary")
if st.button('Sey Hello'):
  st.write('Why helllo there')
else:
  st.write('Goodbye')