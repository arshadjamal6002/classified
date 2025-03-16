import os
import time
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

# Constants
MEDIA_FOLDER = "medias"
LOGO_PATH = "Actualisation_Logo_White.png"  # Updated logo path

# Initialize application
def initialize():
    if not os.path.exists(MEDIA_FOLDER):
        os.makedirs(MEDIA_FOLDER)
    load_dotenv()
    api_key = '123'
    if not api_key:
        st.error("API key for Gemini is missing. Please check your environment variables.")
        st.stop()
    genai.configure(api_key=api_key)

# Save uploaded file
def save_uploaded_file(uploaded_file):
    file_path = os.path.join(MEDIA_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    return file_path

# Analyze video
def initial_analysis(video_path):
    video_file = genai.upload_file(path=video_path)
    st.write(f"Completed upload: {video_file.uri}")
    
    while video_file.state.name == "PROCESSING":
        st.write("Waiting for video to be processed...")
        time.sleep(10)
        video_file = genai.get_file(video_file.name)
    
    if video_file.state.name == "FAILED":
        st.error("Video processing failed. Please try again.")
        st.stop()
    
    st.success("Video processing complete! You can now ask questions.")
    return video_file

# Generate insights
def get_insights(uploaded_video, prompt):
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
    st.write("Generating insights...")
    response = model.generate_content([prompt, uploaded_video], request_options={"timeout": 600})
    
    if response and hasattr(response, "text"):
        st.subheader("Insights")
        st.write(response.text)
    else:
        st.error("Failed to generate insights. Please try again with a different prompt.")

# Streamlit App
def app():
    st.set_page_config(page_title="Video Insights Generator", layout="centered")
    
    # Custom CSS for clean white background and centered elements
    st.markdown("""
        <style>
            body {
                background-color: #ffffff;
                color: #000000;
                font-family: 'Arial', sans-serif;
            }
            .stApp {
                background-color: #ffffff;
            }
            .title-container {
                text-align: center;
                margin-bottom: 20px;
            }
            h1 {
                font-size: 42px !important;
                font-weight: bold !important;
                color: #41b4de !important;
                text-align: center !important;
            }
            h2 {
                font-size: 24px;
                font-weight: bold;
                color: black;
                text-align: center;
            }
        </style>
        """, unsafe_allow_html=True)

    # Logo and Title
    st.markdown("<div class='title-container'>", unsafe_allow_html=True)
    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, width=300)  # Centered, bigger logo
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<h1>VIDEO INSIGHTS</h1>", unsafe_allow_html=True)
    st.markdown("<h2>Chat with AI</h2>", unsafe_allow_html=True)


    
    if "uploaded_video" not in st.session_state:
        st.session_state.uploaded_video = None
    
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov", "mkv"])
    
    if uploaded_file is not None and st.session_state.uploaded_video is None:
        file_path = save_uploaded_file(uploaded_file)
        st.video(file_path)
        st.write("Uploading and processing video...")
        st.session_state.uploaded_video = initial_analysis(file_path)
        
        # Remove file after processing
        if os.path.exists(file_path):
            os.remove(file_path)
    
    if st.session_state.uploaded_video is not None:
        prompt = st.text_input("Ask a question about the video")
        if prompt:
            get_insights(st.session_state.uploaded_video, prompt)

# Run application
initialize()
app()