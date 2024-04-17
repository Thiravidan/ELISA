import streamlit as st
import random
from PIL import Image
import webbrowser as wb
import subprocess

def launch_streamlit():
    subprocess.Popen(["streamlit", "run", "lovec.py"])

def count_same_letters(string1, string2):
    count = 0
    for char in string1:
        if char in string2:
            count += 1
    return count

def main():
    launch_streamlit()
    logo = Image.open('D:\\th-removebg-preview.png') 

    st.sidebar.title("Mode Selection")
    mode = st.sidebar.radio("Select Mode", ( "Normal Mode", "Change Mode"))

    if mode == "Change Mode":
        st.markdown(
            """
            <style>
            [data-testid="stAppViewContainer"] > .main {
                background-color: #2C3E50;
                color: white;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    
    

    st.image(logo, width=200) 
    st.title("Love Calculator")

    boy_name = st.text_input("Enter Boy name:")
    girl_name = st.text_input("Enter Girl name:")

    if boy_name and girl_name:
        result = count_same_letters(boy_name, girl_name)
        combined_names = boy_name + girl_name
        difference = len(combined_names) - (2 * result)

        if difference % 2 == 0:
            random_number = random.randint(60, 100)
            st.success(f"Yes, there is a chance to get committed with your partner. The percentage of love is {random_number}%.")
        else:
            st.warning("vaipilla raja (Go and study hard)")
            if st.button("Click here for motivation"):
                link = "https://youtu.be/PiAzfOz40t0?si=Axmic-P35yUKPhhU"
                wb.open(link)
            elif st.button("click here for real motivation"):
                link = "https://youtu.be/pjpYf8KZ7TE?si=XmKjecOoMpr_qk7w"
                wb.open(link)
    
if __name__ == "__main__":
    main()
