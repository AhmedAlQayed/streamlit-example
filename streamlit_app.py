import streamlit as st
from openai import OpenAI

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=st.secrets["openai_api_key"])

# Function to communicate with ChatGPT
def chat_with_gpt(prompt):
    # Create a chat completion
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You assist in generating DeepMIMO config parameters based on user input"},
            {"role": "user", "content": prompt}
        ],
        model="ft:gpt-3.5-turbo-1106:personal::8iikVOli",
    )
    return response.choices[0].message.content.strip()

# Set the page configuration and title
st.set_page_config(page_title="AutoDeepMIMO", page_icon="https://github.com/AhmedAlQayed/streamlit-example/blob/master/logo.png?raw=true")
st.title("AutoDeepMIMO")

# Add logo to the sidebar or header
st.sidebar.image("https://github.com/AhmedAlQayed/streamlit-example/blob/master/logo.png?raw=true", width=150)

# Custom styles for the page
st.markdown("""
    <style>
        body {
            background-color: #e6e6fa;
            color: #483d8b;
            font-family: 'Georgia', serif;
        }
        h1 {
            color: #800000;
            font-family: 'Raleway', sans-serif;
            margin-bottom: 20px;
        }
        input, select {
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #483d8b;
            color: #e6e6fa;
            border: none;
            border-radius: 4px;
            font-family: 'Raleway', sans-serif;
            padding: 8px 16px;
            text-decoration: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #e64a19;
        }
        .widget-box {
            background-color: #ffffff;
            border-radius: 4px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            margin-bottom: 16px;
            padding: 30px;
        }
        .reportview-container {
            background: #fff8e1;
        }
        .main {
            background: #fff8e1;
        }
        .block-container {
            background: #fff8e1;
        }
        .stButton > button {
            width: 100%;  /* Make the button expand to the full width */
        }
    </style>
    """, unsafe_allow_html=True)

# User input
ingredients = st.text_input("Enter your network/communication system scenario:")
prompt = f"{ingredients}"

# Send query to the chatbot
if st.button("Generate Config Parameters!"):
    recipe_response = chat_with_gpt(prompt)
    st.text_area("DeepMIMO Configuration Parameters", recipe_response, height=300)

# Display images at the bottom with appropriate scaling
col1, col2 = st.columns([1, 1])
with col1:
    st.image("https://github.com/AhmedAlQayed/streamlit-example/blob/master/O1_bird.png?raw=true", use_column_width=True)
with col2:
    st.image("https://github.com/AhmedAlQayed/streamlit-example/blob/master/O1_topV2.png?raw=true", use_column_width=True)

# Footer with developer credits
st.markdown("---")
st.markdown("Developed by Ahmed Alhammadi, Technology Innovation Institute, Abu Dhabi, UAE")