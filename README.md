# langchain-llm-translator

A minimal LangChain app that translates text from English into another language using Google Gemini chat models and a `ChatPromptTemplate`.

## Prerequisites
- Python 3.9+
- A Google AI API key (Gemini)

## Install
```bash
pip install langchain langchain-google-genai
```

## Configure API key
`main.py` securely prompts for your API key at runtime using `getpass.getpass(...)`. When you run the script, enter your key when prompted. Nothing is echoed to the console.

## Run
```bash
python main.py
```
Expected output (example):
```
Translation: Ciao!
```

## How it works
- Uses `ChatPromptTemplate` to construct a multi-message prompt:
  - System: `"Translate the following from English into {language}"`
  - User: `"{text}"`
- Formats the template with runtime variables and invokes a Gemini chat model.

Key variables in `main.py` you can edit:
- `target_language` – the desired output language (default: `"Italian"`)
- `text_to_translate` – the English text to translate (default: `"hi!"`)

## Model
The script initializes: `init_chat_model("gemini-2.5-flash", model_provider="google_genai")`.

If your environment doesn’t have this model, switch to a currently available one (e.g., `"gemini-1.5-flash"`).

## Troubleshooting
- Ensure packages are installed: `pip install langchain langchain-google-genai`
- Verify your API key is valid and entered correctly at the prompt
- Network and regional availability may affect model access

## Reference
- LangChain tutorial: Build a simple LLM application with chat models and prompt templates — https://python.langchain.com/docs/tutorials/llm_chain/