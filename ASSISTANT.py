import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
import pyautogui
import psutil

from spotipy.oauth2 import SpotifyOAuth
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Ellipse
from PIL import Image
import subprocess
import qrcode
import time
import webbrowser

import ctypes


import streamlit as st  

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 




def wishme():
   
    
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        st.write("Good morning sir!")
    elif 12 <= hour < 18:
        st.write("Good afternoon sir")
    elif 18 <= hour < 24:
        st.write("Good Evening sir")
    else:
        st.write("Good night sir")

    st.write("ELISA at your service. Please tell me how can i help you?")


def take_command():
    option = st.radio("Choose input mode:", ("Text", "Voice"))

    if option == "Voice":
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.write("Listening...")
            audio = recognizer.listen(source)
        try:
            st.write("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            st.write("You said:", query)
            return query.lower()
        except Exception as e:
            st.write("Error:", e)
            st.write("Say that again please...")
            return None  # Return None if recognition fails

    elif option == "Text":
        user_input = st.text_input("Enter your command:")
        return user_input.lower()

    else:
        st.write("Invalid choice.")
        return None


def screenshot():
    try:
        img = pyautogui.screenshot()
        screenshot_path = "D:/screenshot/open-cv/screenshot.png"
        img.save(screenshot_path)
        return screenshot_path
    except Exception as e:
        st.error(f"Error taking screenshot: {e}")
        return None


def cpu():
    usage = str(psutil.cpu_percent())
    
    battery = psutil.sensors_battery()
   

def take_notes(text):
    try:
        print("Transcribing...")
        note = text
        print("Note:", note)
        
        with open("notes.txt", "a") as file:
            file.write(note + "\n")
        st.success("Note saved successfully.")

    except:
        st.error("Error saving note.")

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def restore_window():
    
    pyautogui.press('win')
    time.sleep(0.5) 

   
    pyautogui.press('up')
    time.sleep(0.5)

   
    pyautogui.press('enter')
    print("Window restored successfully.")
def lock_laptop():
   
    ctypes.windll.user32.LockWorkStation()
    print("Laptop locked.")
    os.system("rundll32.exe user32.dll,LockWorkStation")
def open_search_bar():
    pyautogui.hotkey('winleft', 's')
    print("Search bar opened.")

def switch_between_tabs():
    
    pyautogui.hotkey('alt', 'tab')
    print("Switched between tabs.")

def launch_streamlit():
    subprocess.Popen(["streamlit", "run", "ELISA.py"])
import subprocess
def launch_streamlit():
    subprocess.Popen(["streamlit", "run", "ELISA.py"])

def main():
    logo = Image.open('D:\\bg.png') 


    st.image(logo, width=100) 
    st.title("Elisa - Your AI Assistant")

    st.sidebar.title("Elisa's Options")
    choice = st.sidebar.selectbox("Choose a function", 
                              ["select an option", "Screenshot", 
                               "Logout", "Shutdown", "Restart", "Open Application",
                               "Open URL", "Remember", "Recall",
                               "Battery", "Take Notes", "Link to QR",
                               "I am upset", "I am happy", "I need motivation",
                               "Love calculator",  "Open Windows bar",
                               "Lock the screen", "Open search bar", 
                               "Switch tabs", 
                               "Chatbot mode"])
    if choice == "select an option":
        wishme()
    elif choice == "Screenshot":
        if st.button("Take Screenshot"):
            screenshot_path = screenshot()  # Call the screenshot function
            if screenshot_path:
                st.write("Screenshot taken!")
                st.image(screenshot_path)
    elif choice == "Logout":
        if st.button("Confirm Logout"):
            os.system("shutdown -l")
    elif choice == "Shutdown":
        if st.button("Confirm Shutdown"):
            os.system("shutdown /s /t 1")
    elif choice == "Restart":
        if st.button("Confirm Restart"):
            os.system("shutdown /r /t 1")
    elif choice == "Open Application":
        def open_application(app_name):
            os.system(f"start {app_name}")
            st.write(f"Opening {app_name}...")

        applications = [
    {"Name": "Calculator", "Command": "calc"},
    {"Name": "Notepad", "Command": "notepad"},
    {"Name": "Microsoft Paint", "Command": "mspaint"},
    {"Name": "Google Chrome", "Command": "chrome"},
    {"Name": "Spotify", "Command": "spotify"},
    {"Name": "Microsoft Excel", "Command": "excel"},
    {"Name": "Microsoft Word", "Command": "winword"},
    {"Name": "Command Prompt", "Command": "cmd"},]

            
        

        st.write("List of available applications:")
        for app in applications:
            st.write(f"- {app}")

        
        app_to_open = st.text_input("Enter the name of the application to open:")

        
        if app_to_open:
            if st.button(f"Open {app_to_open}"):
                open_application(app_to_open)

    elif choice == "Open URL":
        url = st.text_input("Enter URL:")
        if url:
            a = "https://www."+url+".com"
            st.write(f"Opening link: {url}")
            webbrowser.open(a)
           
            

    elif choice == "Remember":
        data = st.text_input("What should I remember?")
        if data:
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
            st.write("Data remembered!")
    elif choice == "Recall":
        remember = open('data.txt', 'r')
        data = remember.read()
        st.write(f"Recalled data: {data}")
    elif choice == "Battery":
        usage = str(psutil.cpu_percent())
        battery = psutil.sensors_battery()
        st.write(f"CPU Usage: {usage}%")
        st.write(f"Battery: {battery.percent}%")
    elif choice == "Take Notes":
       st.title("Note Taker")
       st.write("Type your note below and click on the button to save.")

       note_text = st.text_area("Enter your note:")

       if st.button("Save Note"):
            take_notes(note_text)
    elif choice == "Link to QR":
        st.subheader("Generate QR Code")
        data = st.text_input("Enter data for QR code:")
        if data and st.button("Generate QR Code"):
            filename = "qr_code.png"
            generate_qr_code(data, filename)
            st.image(filename, caption="Generated QR Code", use_column_width=True)
    elif choice == "I am upset":
            st.write("Boss dont worry keep calm and just listen songs ")
            a="https://open.spotify.com/track/1z0lXDoPdmTzy0mUFrmB5F?si=ac67391d08eb4da6"
            webbrowser.open(a)
    elif choice == "I am happy":
            st.write("Boss im very glad to hear that lets enjoy with this song")
            a="https://open.spotify.com/track/7I2iaEOGWSfMOaTk8z4ZtD?si=8fa58fec8d254e62"
            webbrowser.open(a)
    elif choice == "I need motivation":
            st.write("Boss open your work i will play you a song")
            a="https://open.spotify.com/track/3OLnPo26zFl6V1vWZ78Sw3?si=74a2b5e082284837"
            webbrowser.open(a)
    
    elif choice == "Open Windows bar":
        st.write("Opening.....")
        restore_window()
    elif choice == "Lock the screen":
        st.write("Locking....")
        lock_laptop()
    elif choice == "Open search bar":
        st.write("Opening.....")
        open_search_bar()
    elif choice == "Switch tabs":
        st.write("Switching.....")
        switch_between_tabs()
    elif choice == "Chatbot mode":
        st.write("SWITCHING CHAT BOT MODE")
        subprocess.Popen(["streamlit", "run", "D:\ELISA.py"])
        
    elif choice == "Love calculator":
        st.write("SWITCHING")
        subprocess.Popen(["streamlit", "run", "D:\lovec.py"])

    

    

if __name__ == "__main__":
    main()