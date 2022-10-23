import streamlit as st

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

number = st.number_input('Insert a number')
st.write('The current number is ', number)