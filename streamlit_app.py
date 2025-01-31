import streamlit as st 

about_page = st.Page(
    page = "views/about.py",
    title = "Home",
    icon = ":material/account_circle:",
    # default = True
    
)

project_page = st.Page(
    page = "views/chatbot.py",
    title = "DeepThink(R1)",
    icon = ":material/chat_bubble_outline:"
)



pg = st.navigation(
    {
        "info" : [about_page],
        "chat" : [project_page],
    }
)


st.logo(r"assets\logo.png")


pg.run()
