from huggingface_hub import InferenceClient
from huggingface_hub import login
import streamlit as st 

# Make sure the token is correct (check for typos and spaces)
token ="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"

# Login with the access token
login(token=token)

client = InferenceClient(api_key=token)  # You can use the same token here

def llm(prompt):
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    completion = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
        messages=messages,
        max_tokens=500
    )

    return (completion.choices[0].message['content'])

st.title("Hi,I'am DeepSeek")


#This creates a input box for the chatbot 
user_prompt = st.chat_input("Enter your message: ")

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
        st.chat_message(message['role']).markdown(message['content'])


if user_prompt:
    st.chat_message('user').markdown(user_prompt)
    st.session_state.messages.append({
        'role': 'user',
        'content': user_prompt
    })
    
    response = llm(user_prompt)
    st.chat_message('assistant').markdown(response)
    st.session_state.messages.append({
        'role': 'assistant',
        'content': response
    })
