import streamlit as st
from openai import OpenAI
from openai import OpenAI

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=st.secrets["openai_api_key"])
hide_github_icon = """
#GithubIcon {
  visibility: hidden;
}
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)
# Function to communicate with ChatGPT
def chat_with_gpt(prompt):
    # Create a chat completion
    response = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-1106:personal::8kcDNcCL",
        messages=[
            {"role": "system", "content": "You assist in generating DeepMIMO config parameters based on user input"},
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content.strip()

# Set the page configuration and title
st.set_page_config(page_title="AutoDeepMIMO", page_icon="https://github.com/AhmedAlQayed/streamlit-example/blob/master/logo.png?raw=true")
# Add logo to the sidebar or header
st.image("https://github.com/AhmedAlQayed/streamlit-example/blob/master/logo.png?raw=true", width=150)
st.title("AutoDeepMIMO")



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
def change_label_style(label, font_size='12px', font_color='black', font_family='sans-serif'):
    html = f"""
    <script>
        var elems = window.parent.document.querySelectorAll('p');
        var elem = Array.from(elems).find(x => x.innerText == '{label}');
        elem.style.fontSize = '{font_size}';
        elem.style.color = '{font_color}';
        elem.style.fontFamily = '{font_family}';
    </script>
    """
    st.components.v1.html(html)

# User input
label = "Enter your network/communication system scenario:"
ingredients = st.text_input(label)
prompt = f"""Make sure to only consider the following set of parameters.
parameters['dynamic_settings'] 
parameters['OFDM']
parameters['active_BS'] 
parameters['bs_antenna'] 
parameters['ue_antenna'] 
parameters['dynamic_settings']['first_scene']
parameters['dynamic_settings']['last_scene']
parameters['num_paths'] 
parameters['active_BS'] 
parameters['user_row_first']
parameters['user_row_last'] 
parameters['row_subsampling']
parameters['user_subsampling'] 
parameters['bs_antenna']['shape'] 
parameters['bs_antenna']['spacing'] 
parameters['bs_antenna']['rotation'] 
parameters['bs_antenna']['radiation_pattern']
parameters['ue_antenna']['shape']
parameters['ue_antenna']['spacing']
parameters['ue_antenna']['rotation'] 
parameters['ue_antenna']['radiation_pattern']
parameters['enable_BS2BS'] 
parameters['OFDM_channels']
parameters['OFDM']['subcarriers'] 
parameters['OFDM']['subcarriers_limit']
parameters['OFDM']['subcarriers_sampling']
parameters['OFDM']['bandwidth'] 
parameters['OFDM']['RX_filter']. SELECT ONLY THE RELEVANT PARAMETERS from the following scenario: {ingredients} DO NOT SHOW ALL PARAMETERS. ONLY the relevant ones. WHen ASKED RANDOM PARAMETERS, YOU HAVE TO GIVE A number"""
change_label_style(label, '20px')

# Send query to the chatbot
if st.button("Generate Config Parameters!"):
    chat_response = chat_with_gpt(prompt)
    st.text_area("DeepMIMO Configuration Parameters", chat_response, height=300)

# Display images at the bottom with appropriate scaling
col1, col2 = st.columns([1, 1])
with col1:
    st.image("https://github.com/AhmedAlQayed/streamlit-example/blob/master/O1_bird.png?raw=true", use_column_width=True)
with col2:
    st.image("https://github.com/AhmedAlQayed/streamlit-example/blob/master/O1_topV2.png?raw=true", use_column_width=True)

# Footer with developer credits
st.markdown("---")
st.markdown("Developed by Ahmed Alhammadi, Technology Innovation Institute, Abu Dhabi, UAE")