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
prompt = f"""Make sure to only consider the following set of parameters:
parameters['dynamic_settings'] 
parameters['OFDM']
parameters['bs_antenna'] 
parameters['ue_antenna'] 
parameters['dynamic_settings']['first_scene'] = 1
parameters['dynamic_settings']['last_scene'] = 1

parameters['num_paths'] = 5
parameters['active_BS'] = np.array([1])
parameters['user_row_first'] = 1
parameters['user_row_last'] = 1
parameters['row_subsampling'] = 1
parameters['user_subsampling'] = 1

parameters['bs_antenna']['shape'] = np.array([1, 8, 4])
parameters['bs_antenna']['spacing'] = 0.5
parameters['bs_antenna']['rotation'] = np.array([0, 0, 0])
parameters['bs_antenna']['radiation_pattern'] = 'isotropic'

parameters['ue_antenna']['shape'] = np.array([1, 4, 2])
parameters['ue_antenna']['spacing'] = 0.5
parameters['ue_antenna']['rotation'] = np.array([0, 0, 0])
parameters['ue_antenna']['radiation_pattern'] = 'isotropic'

parameters['enable_BS2BS'] = 1

parameters['OFDM_channels'] = 1 # Frequency (OFDM) or time domain channels
parameters['OFDM']['subcarriers'] = 512
parameters['OFDM']['subcarriers_limit'] = 64
parameters['OFDM']['subcarriers_sampling'] = 1
parameters['OFDM']['bandwidth'] = 0.05
parameters['OFDM']['RX_filter'] = 0. Now here is the scenario: {ingredients}"""
change_label_style(label, '20px')

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