
Role: Senior Python AI Engineer

Objective:
Build an AI-powered PDF Summarizer + Quiz Generator Agent using Streamlit UI, OpenAgents SDK, Gemini CLI, Context7 MCP, and PyPDF for text extraction.

1. Project Overview

The goal is to develop a Streamlit-based intelligent agent that can:

A. PDF Summarizer

User uploads a PDF

Text extracted using PyPDF

Agent produces a clean, meaningful summary

Developer may choose any UI style (card, block, container)

B. Quiz Generator

After summarization, user clicks Create Quiz

Agent reads the original PDF (not the summary)

Generates:

MCQs

or Mixed-style questions

This is the minimum mandatory feature set.
Students may extend functionality if they want.

2. Critical Technical Constraints

You must strictly follow these rules:

1. Zero-Bloat Protocol (CRITICAL)

No extra code.

No unnecessary comments, widgets, styles, or animations.

Follow exact patterns from SDK documentation.

Do NOT invent features.

2. Model & API Requirements

Use OpenAI Agents SDK (NOT the standard openai library)

Model: gemini-2.0-flash

Base URL:

https://generativelanguage.googleapis.com/v1beta/openai/


API Key: Load from environment variable:

GEMINI_API_KEY

3. SDK Specificity

Tools must follow exact syntax in openai-agents documentation

Agent initialization must use OpenaiChatCompletionModel

No guessing — only verified syntax allowed

4. Error Recovery Protocol

If any of these occur:

SyntaxError

ImportError

AttributeError

Then:

👉 STOP immediately
👉 Call MCP tool: get-library-docs
👉 Re-read official syntax
👉 Rewrite only after confirmation

5. Dependency Management

Use uv for all installations

If dependency already exists: Do NOT reinstall

3. Architecture & File Structure

Root directory (no extra folders unless shown):

.
├── .env                     # API Key (GEMINI_API_KEY)
├── tools.py                 # Tools for PDF text extraction
├── agent.py                 # Agent configuration + tool binding
├── app.py                   # Streamlit UI app
├── pyproject.toml           # UV configuration
└── sample.pdf               # (Optional) Test file

4. Implementation Steps

Follow this order exactly.

Step 1: Documentation & Pattern Analysis

Before writing code:

Action:

Use MCP tool:

get-library-docs(openai-agents)

Analyze:

Study:

Tool creation pattern

FunctionTool / decorators

Agent initialization

How to pass OpenaiChatCompletionModel

How to register tools

How to send messages

How to read tool outputs

If unsure → call the docs tool again.

Step 2: Tool Implementation (tools.py)
Required Tools
1. extract_pdf_text(file_path: str)

Use PyPDF2 or PyPDF

Return plain text

Handle FileNotFoundError (return empty string)

2. generate_quiz(text: str)

Agent will generate questions

This function only passes data; logic stays in LLM

Format:

Tools must use the exact SDK format discovered in Step 1:

Examples (not final syntax until docs are verified):

@tool decorator OR

FunctionTool(...) wrapper

Use only verified syntax.

Step 3: Agent Configuration (agent.py)

Implement:

1. Initialize Gemini LLM

Using SDK-verified class:

OpenaiChatCompletionModel(model="gemini-2.0-flash")

2. Set API Base URL
base_url = "https://generativelanguage.googleapis.com/v1beta/openai/",

3. Bind Tools

Import tools from tools.py

Register using SDK-correct syntax:

agent = Agent(
    model=model,
    tools=[extract_pdf_text, generate_quiz]
)

4. System Prompt

Agent should follow:

"You are a PDF analysis assistant. Generate clean summaries. Create quizzes based on the original PDF text only. Always use tools when needed."

Step 4: Streamlit Application (app.py)

Use minimal, zero-bloat Streamlit.

UI Flow:
1. PDF Upload

st.file_uploader

Save temporary file

Call agent → summary

2. Display Summary

Simple output (block / card / container)

3. Generate Quiz Button

When clicked:

Pass original text to agent

Display MCQs or mixed questions

Restrictions

No advanced Streamlit components unless required

No extra CSS

No animations

No session-based memory unless needed for functionality

Flow Pattern

(Exact style is enforced)

if st.button("Summarize PDF"):
    response = agent.run(...)
    st.write(response)

if st.button("Create Quiz"):
    response = agent.run(...)
    st.write(response)

5. Environment & Dependencies
.env

GEMINI_API="GEMINI_API_KEY",

pyproject.toml Required Packages

openai-agents

streamlit

PyPDF2 or pypdf

python-dotenv

Installation Rules

Use uv add

Do NOT reinstall packages if already present

6. Testing Scenarios
Test 1: PDF Summarization

Upload sample PDF

Click “Summarize PDF”

Agent should:

Extract text

Generate clean summary

Test 2: Quiz Generation

Upload PDF

Summarize

Click “Create Quiz”

Agent must generate:

MCQs

or mixed format

Test 3: Error Handling

Missing file → empty string

Corrupt PDF → agent response

Wrong tool syntax → check SDK docs

Test 4: Agent Behavior

Summary uses extracted text

Quiz uses original text

No hallucinated features