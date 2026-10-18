import streamlit as st
from deep_translator import GoogleTranslator
 Google Translate experience
st.set_page_config(layout="wide", page_title="SIH1385 Translator")

st.markdown("""
    <style>
    /* 0. Dynamic Font Injection from Google Fonts - Fixes mobile visibility issues */
    @import url('https://googleapis.com');
    .stApp {
        background: linear-gradient(135deg, 
            rgba(255, 69, 0, 0.85) 0%,      
            rgba(10, 12, 36, 0.99) 45%,    
            rgba(10, 12, 36, 0.99) 55%,    
            rgba(0, 200, 40, 0.75) 100%   
        ) !important;
        background-attachment: fixed !important;
        color: #ffff
    }
    
   
    h1, h2, h3, p, span, label, div {
        color: #f8fafc !important;
    }
    
    /* 2. Big Title Styling with Drop Shadow & Mobile-Safe Comic Font Engine */
    .main-title {
        font-family: 'Comic Neue', 'Comic Sans MS', 'Comic Sans', sans-serif !important; 
        font-size: 3.8rem !important;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(45deg, #ff9933, #ffffff, #138808);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
        padding-bottom: 0px;
        filter: drop-shadow(0px 4px 12px rgba(255, 153, 51, 0.5));
    }
  
    .sub-title {
        font-family: 'Comic Neue', 'Comic Sans MS', 'Comic Sans', sans-serif !important; 
        font-size: 2.2rem !important; 
        font-weight: 800 !important;
        text-align: center;
        background: linear-gradient(45deg, #ff9933, #ffffff, #138808);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 35px;
        letter-spacing: 2px;
        filter: drop-shadow(0px 4px 10px rgba(0, 0, 0, 0.7)); /* Strong shadow to stand out */
    }
    
   
    .stTextArea textarea {
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.25) !important; 
        font-size: 16px !important;
        padding: 18px !important;
        background-color: rgba(15, 16, 26, 0.88) !important; 
        color: #ffffff !important;
        backdrop-filter: blur(12px);
        box-shadow: 0 10px 35px 0 rgba(0, 0, 0, 0.55);
    }
    .stTextArea textarea:focus {
        border-color: #ff9933 !important; /* Glowing Saffron Focus */
        box-shadow: 0 0 18px rgba(255, 153, 51, 0.6) !important;
    }
    
    /* Glassmorphic Output Box Styling */
    .output-container {
        background-color: rgba(22, 24, 38, 0.88)
        border: 1px solid rgba(255, 255, 255, 0.25)
        border-radius: 12px;
        min-height: 195px;
        padding: 18px;
        font-size: 16px;
        color: #ffffff !important;
        backdrop-filter: blur(12px);
        box-shadow: 0 10px 35px 0 rgba(0, 0, 0, 0.55);
    }
    
   
    .stSelectbox div[data-baseweb="select"] {
        background-color: rgba(15, 16, 26, 0.92) 
        border: 1px solid rgba(255, 255, 255, 0.25)
        color: #ffffff
        border-radius: 10px;
    }
    
    /* 4. High-Vibrancy Action Button */
    .stButton>button {
        background: linear-gradient(90deg, #ff9933 0%, #138808 100%) !important;
        color: #ffffff !important; 
        border-radius: 8px !important;
        border: none !important;
        padding: 14px 36px !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        letter-spacing: 0.5px;
        box-shadow: 0 5px 20px rgba(255, 153, 51, 0.6);
        transition: all 0.3s ease;
        display: block;
        margin: 0 auto;
    }
    .stButton>button:hover {
        transform: scale(1.03);
        box-shadow: 0 8px 25px rgba(19, 136, 8, 0.7);
    }
    </style>
""", unsafe_allow_html=True)

# App Big Title & Subtitle with dynamic gradient text
st.markdown('<p class="main-title">Regional Language Translator</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">BY <br>ORIGIN VECTORS</p>', unsafe_allow_html=True)

# Language Dropdown Selection Map
language_options = [
    ("Hindi", "hi"),
    ("Gujarati", "gu"),
    ("Marathi", "mr"),
    ("Bengali", "bn"),
    ("Tamil", "ta"),
    ("Bhojpuri", "bho"),
    ("Telugu", "te"),
    ("Punjabi", "pa"),
    ("Kannada", "kn"),
    ("Malayalam", "ml"),
    ("Assamese", "as"),
]

# Display Selectbox (Centered layout)
col_left, col_mid, col_right = st.columns([1, 2, 1])
with col_mid:
    selected_tuple = st.selectbox(
        "Choose Target Language:",
        options=language_options,
        format_func=lambda x: x[0]  
    )

# Extract language name and language code safely
lang_name, lang_code = selected_tuple

# Main Split Columns Layout (Left = Input, Right = Output)
col1, col2 = st.columns(2)

with col1:
    st.markdown("### **English (Source)**")
    user_input = st.text_area(
        label="Input text",
        placeholder="Type or paste English resource text here...",
        height=200,
        label_visibility="collapsed"
    )

with col2:
    st.markdown(f"### **{lang_name} (Target)**")
    # Empty placeholder box that mimics the Google Translate look before translation occurs
    output_placeholder = st.empty()
    output_placeholder.markdown('<div class="output-container" style="color: #cbd5e1 !important;">Translation will appear here...</div>', unsafe_allow_html=True)
st.write("")

if st.button("Translate Now"):
    if user_input.strip() != "":
        try:
            # Performs translation using the GoogleTranslator package
            translated_text = GoogleTranslator(source='en', target=lang_code).translate(user_input)
            
            # Replaces the output box placeholder with actual translated text
            output_placeholder.markdown(f'<div class="output-container"><b>{translated_text}</b></div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Translation Error: {e}")
    else:
        st.warning("Please type or paste some text first!")
