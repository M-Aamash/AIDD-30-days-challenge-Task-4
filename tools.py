# from agents import function_tool
# from pypdf import PdfReader
# from pypdf.errors import PdfReadError

# @function_tool
# def extract_pdf_text(file_path: str) -> str:
#     """
#     Extracts text from a PDF file.
#     Args:
#         file_path: The path to the PDF file.
#     Returns:
#         The extracted text from the PDF, or an empty string if the file is not found or cannot be read.
#     """
#     try:
#         reader = PdfReader(file_path)
#         text = ""
#         for page in reader.pages:
#             text += page.extract_text() or ""
#         return text
#     except FileNotFoundError:
#         return ""
#     except PdfReadError:
#         # Handle cases where the PDF is corrupt or cannot be read
#         return ""

# @function_tool
# def generate_quiz(text: str) -> str:
#     """
#     Generates quiz questions based on the provided text.
#     This function only passes data; the logic for quiz generation stays in the LLM.
#     Args:
#         text: The text content to generate quiz from.
#     Returns:
#         The text content passed. The LLM will use this to generate the quiz.
#     """
#     return text


from agents import function_tool
from pypdf import PdfReader

@function_tool
def extract_pdf_text(file_path: str) -> str:
    """
    Extracts text from a PDF file.
    """
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    except Exception:
        return ""

@function_tool
def generate_quiz(text: str) -> str:
    """
    Gives text to LLM for quiz generation.
    """
    return text
