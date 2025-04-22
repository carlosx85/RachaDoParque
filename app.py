import streamlit as st

st.write("Host do MySQL:", st.secrets["mysql"]["host"])
st.write("Host do MySQLuser:", st.secrets["mysql"]["user"])
st.write("Host do MySQL:", st.secrets["mysql"]["database"])