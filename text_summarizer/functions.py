import openai
import streamlit as st

def summarizeChat(prompt):
    augmented_prompt = f"summarize this video transcript text: {prompt}"
    try:
        st.session_state["summary"] = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature= 0.7,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content":  augmented_prompt}
                ]
            )["choices"][0]["message"]["content"]
    except:
        st.write('There was an error =(')
