# import streamlit as st
# import tempfile
# import os
# import asyncio
# from agents import Runner
# from agent import agent

# # Set up an event loop for Streamlit
# def get_or_create_eventloop():
#     try:
#         return asyncio.get_event_loop()
#     except RuntimeError as ex:
#         if "There is no current event loop in thread" in str(ex):
#             loop = asyncio.new_event_loop()
#             asyncio.set_event_loop(loop)
#             return asyncio.get_event_loop()

# loop = get_or_create_eventloop()

# async def main():
#     st.title("PDF Summarizer & Quiz Generator")

#     uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

#     if uploaded_file is not None:
#         with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
#             tmp_file.write(uploaded_file.getvalue())
#             temp_file_path = tmp_file.name

#         st.success("PDF uploaded successfully!")

#         if st.button("Summarize PDF"):
#             st.info("Generating summary...")
#             try:
#                 # summary_response = await Runner.run(agent, f"Please summarize the PDF file located at {temp_file_path}")
#                 # st.subheader("Summary")
#                 # print(summary_response.final_output)
#                 summary_response, meta = await Runner.run(agent, f"Please summarize the PDF file located at {temp_file_path}")
#                 print(summary_response.output_text)

#                 st.session_state.summary = summary_response.output_text

#                 st.session_state.temp_file_path = temp_file_path
#             except Exception as e:
#                 st.error(f"Error generating summary: {e}")

#         if "summary" in st.session_state and st.session_state.summary:
#             if st.button("Create Quiz"):
#                 if "temp_file_path" in st.session_state:
#                     st.info("Generating quiz questions...")
#                     try:
#                         quiz_response, meta = await Runner.run(agent ,f"Please generate a quiz from the PDF file located at {st.session_state.temp_file_path}")
#                         st.subheader("Generated Quiz")
#                         print(quiz_response.output_text)
#                     except Exception as e:
#                         st.error(f"Error generating quiz: {e}")
#                 else:
#                     st.warning("Could not find the uploaded PDF file to generate the quiz.")

#         # This cleanup is problematic in Streamlit's execution model.
#         # The file might be deleted before the "Create Quiz" button is pressed.
#         # We'll store the path in the session state and delete it on the next run if a new file is uploaded.
#         if "temp_file_to_delete" in st.session_state:
#             if os.path.exists(st.session_state.temp_file_to_delete):
#                 os.remove(st.session_state.temp_file_to_delete)
#             del st.session_state.temp_file_to_delete
        
#         if uploaded_file:
#              st.session_state.temp_file_to_delete = temp_file_path


# if __name__ == "__main__":
#     loop.run_until_complete(main())
import streamlit as st
import tempfile
import os
import asyncio
from agents import Runner
from agent import agent


# Fix Streamlit async loop
def get_or_create_eventloop():
    try:
        return asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop

loop = get_or_create_eventloop()


async def main():
    st.title("📄 PDF Summarizer & Quiz Generator")

    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.getvalue())
            pdf_path = tmp.name

        st.success("PDF uploaded successfully!")

        # ----------------------
        # SUMMARY BUTTON
        # ----------------------
        if st.button("Summarize PDF"):
            st.info("Generating summary...")
            try:
                response, meta = await Runner.run(
                    agent,
                    f"Summarize the PDF located at {pdf_path}"
                )

                summary_text = response.output_text

                st.subheader("Summary")
                st.write(summary_text)

                st.session_state.summary = summary_text
                st.session_state.pdf_path = pdf_path

            except Exception as e:
                st.error(f"Error generating summary: {e}")

        # ----------------------
        # QUIZ BUTTON
        # ----------------------
        if st.session_state.get("summary"):
            if st.button("Create Quiz"):
                st.info("Generating quiz...")
                try:
                    quiz_response, meta = await Runner.run(
                        agent,
                        f"Create a quiz based on the PDF located at {st.session_state.pdf_path}"
                    )

                    quiz_text = quiz_response.output_text

                    st.subheader("Generated Quiz")
                    st.write(quiz_text)

                except Exception as e:
                    st.error(f"Error generating quiz: {e}")


if __name__ == "__main__":
    loop.run_until_complete(main())
