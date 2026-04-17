import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Move & Heal | Professional Clinic", page_icon="⚖️", layout="wide")

# 2. Luxury & Minimalist CSS
st.markdown("""
    <style>
    /* Background and Fonts */
    .main { background-color: #ffffff; }
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@300;400&display=swap');

    /* Logo Section */
    .header-container {
        text-align: center;
        padding: 60px 20px;
        background-color: #fcfdfd;
        border-bottom: 1px solid #eee;
        margin-bottom: 40px;
    }
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 65px;
        color: #16a085; /* Turquoise */
        margin: 0;
        letter-spacing: 2px;
    }
    .sub-title {
        font-family: 'Lato', sans-serif;
        font-size: 18px;
        color: #d4af37; /* Gold */
        letter-spacing: 10px;
        text-transform: uppercase;
        margin-top: -10px;
        font-weight: 400;
    }

    /* Content Cards */
    .feature-card {
        padding: 30px;
        border-radius: 2px;
        border: 1px solid #f0f0f0;
        background-color: #ffffff;
        transition: all 0.3s ease;
    }
    .feature-card:hover {
        border-color: #d4af37;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
    }

    /* Input Styling */
    .stTextInput>div>div>input {
        border: none;
        border-bottom: 2px solid #16a085;
        border-radius: 0px;
        padding: 10px 0px;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Elegant Header
st.markdown("""
    <div class="header-container">
        <h1 class="main-title">MOVE & HEAL</h1>
        <p class="sub-title">Medical Rehabilitation Clinic</p>
    </div>
    """, unsafe_allow_html=True)

# 4. Professional Layout
col1, space, col2 = st.columns([1.5, 0.2, 1])

with col1:
    st.markdown("### 🩺 Clinical Inquiry")
    st.write("Please describe the clinical case or the injury details for professional assessment.")
    user_input = st.text_input("", placeholder="e.g. Analysis of Lower Motor Neuron Lesion...")
    
    if user_input:
        st.info("System is processing your clinical data... A specialized response will be generated shortly.")

with col2:
    st.markdown("<div class='feature-card'>", unsafe_allow_html=True)
    st.markdown("#### ✨ Clinic Vision")
    st.write("Bridging the gap between acute injury and full functional recovery through evidence-based practice.")
    st.markdown("---")
    st.markdown("Core Specializations:")
    st.markdown("- Sports Medicine\n- Neuro-Rehabilitation\n- Post-Surgical Recovery")
    st.markdown("</div>", unsafe_allow_html=True)

# 5. Footer
st.markdown("<br><br><br><p style='text-align: center; color: #bbb; font-family: Lato; font-size: 12px; letter-spacing: 2px;'>EST. 2026 | THE IMPACT BEGINS WITH A STEP</p>", unsafe_allow_html=True)
