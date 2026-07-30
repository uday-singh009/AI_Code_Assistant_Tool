import streamlit as st
from main import code_assistant

st.set_page_config(
    page_title="AI Code Assistant",
    page_icon="💻",
    layout="wide"
)

st.title("💻 AI Code Assistant")
st.write(
    "Generate, Debug, Explain, Optimize and Review code using Google Gemini AI."
)

# Sidebar
st.sidebar.header("Settings")

task = st.sidebar.selectbox(
    "Select Task",
    [
        "Generate Code",
        "Debug Code",
        "Explain Code",
        "Optimize Code",
        "Generate Documentation",
        "Review Code"
    ]
)

language = st.sidebar.selectbox(
    "Programming Language",
    [
        "Python",
        "Java",
        "C",
        "C++",
        "JavaScript",
        "TypeScript",
        "Go",
        "Rust",
        "PHP",
        "HTML",
        "CSS",
        "SQL",
        "Other"
    ]
)

st.subheader("Code / Prompt")

code = st.text_area(
    "Enter your code or describe what you want:",
    height=300,
    placeholder="Example:\nWrite a Python program to find the factorial of a number."
)

if st.button("🚀 Generate Response", use_container_width=True):

    if code.strip() == "":
        st.warning("Please enter some code or a prompt.")
    else:
        with st.spinner("AI is working..."):
            response = code_assistant(task, language, code)

        st.subheader("Result")

        st.markdown(response)

st.sidebar.markdown("---")

st.sidebar.info(
"""
### Features

✅ Generate Code

✅ Debug Code

✅ Explain Code

✅ Optimize Code

✅ Generate Documentation

✅ Review Code

Powered by Google Gemini AI
"""
)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit & Google Gemini AI")