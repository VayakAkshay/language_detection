import streamlit as st
from predictions import get_predictions


languages = ['English', 'Malayalam', 'Hindi', 'Tamil', 'Portugeese', 'French',
       'Dutch', 'Spanish', 'Greek', 'Russian', 'Danish', 'Italian',
       'Turkish', 'Sweedish', 'Arabic', 'German', 'Kannada']

st.subheader("Language Detection")

with st.expander("Supported Languages", expanded=False):
    for language in languages:
        st.write(f"- {language}")

user_input = st.text_area("Enter text:")

if user_input:
    language_name = get_predictions(user_input)
    st.write("Output:", language_name)
else:
    st.write("Textarea is null or empty. Please enter some text.")