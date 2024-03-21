# import the Streamlit library
import streamlit as st
from streamlit_option_menu import option_menu
from utils.constants import *

# configure page settings
st.set_page_config(page_title='Lindokuhle Dlomo Profile' ,layout="wide",initial_sidebar_state="auto", page_icon='👧🏻') # always show the sidebar

# load local CSS styles
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("styles/styles_main.css")

# get the variables from constants.py
pronoun = info['Pronoun']

# app sidebar
with st.sidebar:
    st.markdown("""
                # Chat with my AI assistant
                """)
    with st.expander("Click here to see FAQs"):
        st.info(
            f"""
            - What are {pronoun} strengths and weaknesses?
            - What is {pronoun} expected salary?
            - What is {pronoun} latest project?
            - When can {pronoun} start to work?
            - Tell me about {pronoun} professional background
            - What is {pronoun} skillset?
            - What is {pronoun} contact?
            - What are {pronoun} achievements?
            """
        )

    st.markdown(""" <a href={}> <em>👉 checkout my LinkedIN Profile </a>""".format(info['LinkedIn']), unsafe_allow_html=True)
    st.markdown(""" <a href={}> <em>👉 Check out my Github Profile</a>""".format(info['Github']), unsafe_allow_html=True)      
    st.caption(f"© Made by Lindokuhle Dlomo 2024. All rights reserved.")

import requests

def hero(content1, content2):
    st.markdown(f'<h1 style="text-align:center;font-size:60px;border-radius:2%;">'
                f'<span>{content1}</span><br>'
                f'<span style="color:black;font-size:22px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

with st.container():
    col1,col2 = st.columns([8,3])

full_name = info['Full_Name']
with col1:
    hero(f"Hi, I'm {full_name}👋", info["Intro"])
    st.write("")
    st.write(info['About'])

    from streamlit_extras.switch_page_button import switch_page
    col_1, col_2, temp = st.columns([0.35,0.2,0.45])
    with col_1:
        btn1 = st.button("Chat with My AI Assistant")
        if btn1:
            switch_page("AI_Assistant_Chat")
    with col_2:
        btn2 = st.button("My Resume")
        if btn2:
            switch_page("Resume")

import streamlit.components.v1 as components

def change_button_color(widget_label, background_color='transparent'):
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{widget_label}') {{ 
                    elements[i].style.background = '{background_color}'
                }}
            }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)

change_button_color('Chat with My AI Assistant', '#0cc789') 

from  PIL import Image
with col2:
    profile = Image.open("images/profile.jpeg")
    st.image(profile, width=280)
          
with st.container():
    st.write("---")
    st.subheader('🚀 Project Showcase')

    projects = projects

    def display_project(col, project):
        with col:
            st.markdown(
                f'<a href="{project["link"]}" target="_blank" class="portfolio-item" data-id="3">'
                f'<img src="{project["image_url"]}" style="width:100%;height:auto;"></a>',
                unsafe_allow_html=True,
            )
            st.markdown(f'<p style="font-size: 16px; font-weight: bold;">{project["title"]}</p>', unsafe_allow_html=True)
            st.markdown(f'<p style="font-size: 14px">{project["description"]}</p>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,1,1])
    columns = [col1, col2, col3]

    # adjust the range(0, len(projects), 3) accordingly if the length of your projects is not a multiple of 3
    for i in range(0, len(projects), 3):
        for j, col in enumerate(columns):
            if i + j < len(projects):  # Check if project index is within range
                display_project(col, projects[i + j])
st.markdown(""" <a href={}> <em>👀 Click here to see more </a>""".format('www.github.com/Lindo-OTG'), unsafe_allow_html=True)
    

st.write("---")
with st.container():  
    col1,col2 = st.columns([0.95, 0.05])
    with col_1:
        st.subheader("📨 Contact Me")
        email = info["Email"]
        contact_form = f"""
        <form action="https://formsubmit.co/{email}" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
