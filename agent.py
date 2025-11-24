# import os
# from dotenv import load_dotenv
# from agents import Agent
# from openai import AsyncClient
# from agents.models.openai_chatcompletions import OpenAIChatCompletionsModel
# from tools import extract_pdf_text, generate_quiz

# load_dotenv()

# # 1. Initialize Gemini LLM
# client = AsyncClient(
# base_url="https://aistudio.google.com/app/api-keys",
#     api_key=os.getenv("OPENAI_API_KEY")
# )
# # 2. Set API Base URL and load API Key
# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=client
    
# )

# # 3. Bind Tools
# agent = Agent(
#     name="PDF Analysis Assistant",
#     instructions="You are a PDF analysis assistant. Generate clean summaries. Create quizzes based on the original PDF text only. Always use tools when needed.",
#     tools=[extract_pdf_text, generate_quiz],
#     model=model
# )

import os
from dotenv import load_dotenv
from agents import Agent
from openai import AsyncClient
from agents.models.openai_chatcompletions import OpenAIChatCompletionsModel
from tools import extract_pdf_text, generate_quiz

load_dotenv()

# Correct Gemini OpenAI-compatible API endpoint
client = AsyncClient(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
    api_key=os.getenv("GEMINI_API_KEY")
)

# Model wrapper for OpenAgents
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

agent = Agent(
    name="PDF Analysis Assistant",
    instructions=(
        "You are a PDF analysis assistant. "
        "Always use tools to extract PDF text. "
        "Summaries must be accurate, clear, and only based on extracted text. "
        "Quizzes must be based on the same text."
    ),
    tools=[extract_pdf_text, generate_quiz],
    model=model
)
