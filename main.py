import getpass
import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chat_models import init_chat_model

# Set up Google API key
if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API Key: ")

# Initialize the model with correct model name
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

try:
    response = model.invoke(messages)
    print("Translation:", response.content)
except Exception as e:
    print(f"Error occurred: {e}")
    print("Make sure you have installed the required packages:")
    print("pip install langchain langchain-google-genai")