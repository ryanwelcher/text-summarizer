import streamlit as st
import os
from text_summarizer.functions import summarizeChat

try:
  if "summary" not in st.session_state:
      st.session_state["summary"] = ""
  
  st.title("Transcript Summarizer")

  prompt_text = st.text_area(label="Prompt to use:", value="Summarize this video transcript text in the first person plural as streamer RyanWelcherCodes")
  
  input_text = st.text_area(label="Enter full text:", value="", height=250)
  st.button(
      "Submit",
      on_click=summarizeChat,
      kwargs={"text": input_text, "prompt": prompt_text},
  )
  output_text = st.text_area(label="Summarized text:", value=st.session_state["summary"], height=250)
except:
  st.write('There was an error =(')