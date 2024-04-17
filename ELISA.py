import streamlit as st
import google.generativeai as genai
import pyperclip
from PIL import Image

genai.configure(api_key="AIzaSyDxi7prxlhaId6lza3plJc4n6hyoQ7x7BU")


generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
    model_name="gemini-1.0-pro", generation_config=generation_config, safety_settings=safety_settings
)


user_persona = "You:"
ai_persona = "Elisa:"
logo = Image.open('D:\\icon_1_-removebg-preview.png') 



st.image(logo, width=200) 

st.title("Elisa chatbot")


user_input = st.text_input("You say:")


def display_chat_response(persona, response):
    st.write(f'<div class="{persona}">{persona}</div> {response}', unsafe_allow_html=True)


def display_code_output(code):
    copy_button = st.button("Copy code")

   
    with st.expander("View code"):
        st.code(code, language="java")

   
    if copy_button:
        pyperclip.copy(code)
        st.success("Code copied to clipboard!")


st.markdown('<link rel="stylesheet" type="text/css" href="styles.css">', unsafe_allow_html=True)


if user_input:
 
    st.markdown('<div class="personas"><div class="user">You:</div> {0}</div>'.format(user_input), unsafe_allow_html=True)
    
    
    convo = model.start_chat(history=[])
    convo.send_message(user_input)
    response = convo.last.text

    
    if "code" in user_input.lower():
        
        display_chat_response(ai_persona, "Here's the code I found:")
        display_code_output(response)
    else:
        
        display_chat_response(ai_persona, response)
