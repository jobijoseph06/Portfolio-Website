import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
     st.image("image/my photo.jpg")

with col2:
    st.title("Jobi Joseph")
    content = """A recent B.E. graduate in Computer Science and Engineering, exploring the world of software development with a focus on Python. Eager to learn and grow as a beginner in the field, bringing a passion for technology and problem-solving."
"""
    st.info(content)

st.write("A recent B.E. graduate in Computer Science and Engineering, exploring the world of software development with a focus on Python.")