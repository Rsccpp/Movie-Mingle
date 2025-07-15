# app_1.py

import base64
import streamlit as st
from model import load_data, get_recommendations

# Page Config
st.set_page_config(page_title="Movie Recommender", layout="centered")

# Set background image
def set_background(image_path):
    with open(image_path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        @media only screen and (min-width: 360px and max-width: 480px) {{
            .stApp {{
                background-size: cover;
                background-position: top center;
            }}
        }}
        </style>
    """, unsafe_allow_html=True)

set_background("image.png")

# Inject custom CSS for UI improvement
st.markdown("""
    <style>
    .title-bar {
        position: fixed;
        top: 0;
        width: 100%;
        padding: 18px;
        background-color: rgba(0, 0, 0, 0.75);
        text-align: center;
        z-index: 1000;
        border-bottom: 1px solid #666;
    }

    .title-bar h1 {
        font-size: 3rem;
        margin: 0;
        color: #f0f0f0;
        font-family: sans-serif;
    }

    .block-container {
        padding-top: 110px !important;
        color: #dddddd;
    }

    .form-box {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 35px;
        border-radius: 18px;
        max-width: 700px;
        margin: 30px auto;
        box-shadow: 0 0 20px rgba(0,0,0,0.4);
    }

    .form-box h2 {
        color: #B10DC9;
        font-size: 2rem;
        margin-bottom: 15px;
        text-align: center;
        font-family: 'Segoe UI', Tahoma;
    }

    label, .stTextInput input, .stSelectbox div, .stSlider, .stButton button {
        color: #dddddd !important;
        font-size: 1rem;
    }

    .stButton button {
        background-color: #1E90FF;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 8px 20px;
        margin-top: 15px;
    }

    .stButton button:hover {
        background-color: #0f70c9;
    }

    .recommendation {
        background: rgba(255,255,255,0.1);
        padding: 12px;
        margin: 8px 0;
        border-left: 4px solid #9B59B6;
        border-radius: 6px;
        font-size: 2rem;
    }

    .recommendation-header {
        font-size: 1.5rem;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 15px;
        color: #ffffff;
        font-family: 'Segoe UI';
    }
    </style>

    <div class="title-bar">
        <h1>🎬 Movie Mingle</h1>
            <p style='font-size: 28px; color: white;'>Find movies you’ll love. Instantly.

    </div>
    
   
    
""", unsafe_allow_html=True)

# --- Main App UI ---

with st.container():
    st.markdown('<div class="form-box">', unsafe_allow_html=True)

    # st.markdown("<h2>🎥 Movie Mingle</h2>", unsafe_allow_html=True)
    st.write("Enter a movie you like and get similar recommendations!")

    # Load data
    df = load_data()
    movie_list = df['title'].dropna().unique().tolist()

    # Selectbox
    movie_name = st.selectbox("Search and select a movie:", sorted(movie_list))

    # Slider
    num_recommendations = st.slider("How many recommendations would you like?", 1, 20, 5)

    # Button
    if st.button("Get Recommendations"):
        recommendations = get_recommendations(movie_name, num_recommendations)
        st.markdown(f"<div class='recommendation-header'>Top {num_recommendations} Movies similar to '{movie_name}':</div>", unsafe_allow_html=True)
        for i, rec in enumerate(recommendations, 1):
            st.markdown(f"<div class='recommendation'>{i}. {rec}</div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

