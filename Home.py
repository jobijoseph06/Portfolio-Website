import streamlit as st
import pandas



col1, col2 = st.columns(2)

with col1:
     st.image("images/my photo.jpg",  use_container_width=True)

with col2:
    st.title("Jobi Joseph S".upper())
    st.markdown("""
        ### Hey there! 👋
        I'm currently pursuing a **B.E. in Computer Science and Engineering**, with a growing passion for **web development**.  
        I love designing user-friendly, visually appealing websites and enjoy exploring new technologies to improve my skills.  
        Excited about solving problems and creating innovative solutions that make life easier!
        """)



col3, col4 = st.columns(2)
df = pandas.read_csv("data.csv", sep=";")

with col3:
     for index , row in df[0:10].iterrows():
         st.header(row["title"])
         st.write(row["description"])
         st.image("images/" + row["image"])
         st.write(f"[Source]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source]({row['url']})")