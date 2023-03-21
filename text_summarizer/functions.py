import openai
import streamlit as st

def summarizeChat(prompt,text):
    augmented_text = f"{prompt}: {text}"
    try:
        st.session_state["summary"] = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature= 0.7,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content":  augmented_text}
                ]
            )["choices"][0]["message"]["content"]
    except:
        st.write('There was an error =(')
