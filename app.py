import streamlit as st
from predictions import get_predictions

st.set_page_config(page_title="Language Detection Tool - Akshay Vayak", page_icon="🌐", layout="wide")

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

st.subheader("Introduction to Language Detection Tool")
st.write("""
Introducing the Language Detection Tool, a powerful creation by Akshay Vayak, designed to seamlessly integrate into your project. Utilizing a custom NLP model in TensorFlow, this tool accurately identifies the language of textual content in real-time. What sets it apart is its foundation on open data, allowing for robust training, ensuring high accuracy in language detection.""")

st.subheader("Connect with Me")
st.markdown("[Portfolio Site](https://www.akshayvayak.site)")
st.markdown("[LinkedIn](https://www.linkedin.com/in/akshay-vayak/)")
st.markdown("[Github](https://github.com/VayakAkshay)")
st.write("[Upwork](https://www.upwork.com/freelancers/akshayvayak)")
st.write("Email: akshay.markitup@gmail.com")