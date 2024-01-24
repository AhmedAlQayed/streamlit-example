import streamlit as st
from openai import OpenAI
# Initialize the OpenAI client with your API key
client = OpenAI(api_key=st.secrets["openai_api_key"])

# Function to communicate with ChatGPT
def chat_with_gpt(prompt):
    # Create a chat completion
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="gpt-4-1106-preview",
    )

    return response.choices[0].message.content.strip()


# Streamlit app
st.markdown(
    """
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
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Recipe Maker Chatbot")

# Choose input type
with st.sidebar:
    st.header("Instructions")
    st.write(
        "Please choose an input type below and provide the corresponding input in the provided text field. Then click 'Cook me a meal!' to generate your recipe.")
    input_type = st.selectbox("Choose input type:", ["Ingredients", "Recipe Name"])

# Get user input
if input_type == "Ingredients":
    ingredients = st.text_input("Enter ingredients separated by commas:")
    prompt = f"Create a recipe using the following ingredients: {ingredients}. Provide a recipe name, ingredients and detailed steps. Add calories for the recipe as well"
else:
    recipe_name = st.text_input("Enter the recipe name:")
    prompt = f"Provide ingredients and detailed steps for the following recipe: {recipe_name}.Add calories for the recipe as well."

recipe_response = ""

# Send query to the chatbot
if st.button("Cook me a meal!"):
    recipe_response = chat_with_gpt(prompt)

    # Split the response into lines and find the recipe name
    lines = recipe_response.split('\n')
    recipe_name = ""
    ingredients_and_steps = ""
    for line in lines:
        if "recipe name" in line.lower():
            recipe_name = line.strip()
        else:
            ingredients_and_steps += line.strip() + "\n"

    # Output
    with st.container():
        st.markdown(f"## {recipe_name}")
        st.markdown(ingredients_and_steps)

        # Add a box to display the entire response
    st.text_area("Generated Recipe", recipe_response, height=300)

