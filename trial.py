# import streamlit as st
# import os
# import pathlib
# import textwrap
# from PIL import Image


# import google.generativeai as genai


# genai.configure(api_key="AIzaSyCnrTo0OAgZNMVoPGjVhBNllossBP6FVKY")

# ## Function to load OpenAI model and get responses

# def get_gemini_response(input, image, prompt):
#     model = genai.GenerativeModel('gemini-pro-vision')
#     response = model.generate_content([input, image[0], prompt])
#     return response.text
    

# def input_image_setup(uploaded_file):
#     # Check if a file has been uploaded
#     if uploaded_file is not None:
#         # Read the file into bytes
#         bytes_data = uploaded_file.getvalue()

#         image_parts = [
#             {
#                 "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
#                 "data": bytes_data
#             }
#         ]
#         return image_parts
#     else:
#         raise FileNotFoundError("No file uploaded")


# ##initialize our streamlit app

# st.set_page_config(page_title="Gemini Image Demo")

# st.header("Gemini Application")
# input = st.text_input("Input Prompt: ", key="input")
# uploaded_file = st.file_uploader("Choose an image or PDF...", type=["jpg", "jpeg", "png", "pdf"])
# image = ""   
# if uploaded_file is not None:
#     if uploaded_file.type.startswith('image/'):
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Uploaded Image.", use_column_width=True)
#     elif uploaded_file.type == 'application/pdf':
#         st.write("Uploaded PDF:", uploaded_file.name)

# submit = st.button("Tell me about the image")

# input_prompt = """
#                You are an expert in understanding invoices.
#                You will receive input images as invoices &
#                you will have to answer questions based on the input image
#                """

# ## If ask button is clicked

# if submit:
#     image_data = input_image_setup(uploaded_file)
#     response = get_gemini_response(input_prompt, image_data, input)
#     st.subheader("The Response is")
#     st.write(response)

import streamlit as st
from PIL import Image
from pdf2image import convert_from_bytes
import io

import google.generativeai as genai

genai.configure(api_key="AIzaSyCnrTo0OAgZNMVoPGjVhBNllossBP6FVKY")

## Function to load OpenAI model and get responses
def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        if uploaded_file.type == 'application/pdf':
            # Convert PDF to images
            images = convert_from_bytes(uploaded_file.read())
            image_parts = []
            for image in images:
                img_byte_arr = io.BytesIO()
                image.save(img_byte_arr, format='PNG')
                img_byte_arr.seek(0)
                image_parts.append({
                    "mime_type": 'image/png',
                    "data": img_byte_arr.getvalue()
                })
            return image_parts
        elif uploaded_file.type.startswith('image/'):
            # Read the image file into bytes
            bytes_data = uploaded_file.getvalue()
            return [{
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }]
        else:
            raise ValueError("Unsupported file type. Please upload an image or PDF.")
    else:
        raise FileNotFoundError("No file uploaded")

##initialize our streamlit app
st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image or PDF...", type=["jpg", "jpeg", "png", "pdf"])

submit = st.button("Tell me about the image")

input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """

## If submit button is clicked
if submit:
    if uploaded_file is not None:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_prompt, image_data, input)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload an image or PDF.")
