import getpass
import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

# Set up Google API key
if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API Key: ")

# Initialize the model with correct model name
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

# Example inputs (feel free to replace with user input or CLI args)
target_language = "Italian"
text_to_translate = "hi!"

prompt = prompt_template.invoke({"language": target_language, "text": text_to_translate})

try:
    response = model.invoke(prompt)
    print("Translation:", response.content)
except Exception as e:
    print(f"Error occurred: {e}")
    print("Make sure you have installed the required packages:")
    print("pip install langchain langchain-google-genai")