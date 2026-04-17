
import streamlit as st

st.set_page_config(page_title="Move & Heal | Clinical Excellence", page_icon="🌿", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Montserrat:wght@300;400&display=swap');

    .header-container {
        text-align: center;
        padding: 50px 20px;
        background-color: #fbfcfc;
        border-bottom: 2px solid #e8f5f2;
        margin-bottom: 40px;
    }
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 60px;
        color: #0d5a5a; /* Deep Turquoise from your logo */
        margin: 0;
        letter-spacing: 1px;
    }
    .sub-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 16px;
        color: #b08d57; /* Muted Gold from your logo */
        letter-spacing: 7px;
        text-transform: uppercase;
        margin-top: -5px;
    }
    .stTextInput>div>div>input {
        border: none;
        border-bottom: 2px solid #0d5a5a;
        border-radius: 0px;
        font-size: 18px;
    }
    .feature-card {
        padding: 25px;
        border-radius: 8px;
        border: 1px solid #eee;
        border-left: 4px solid #b08d57;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="header-container">
        <h1 class="main-title">MOVE & HEAL</h1>
        <p class="sub-title">Medical Rehabilitation Center</p>
    </div>
    """, unsafe_allow_html=True)

col1, space, col2 = st.columns([1.5, 0.2, 1])

with col1:
    st.markdown("### 🩺 Professional Clinical Inquiry")
    st.write("Submit case details for specialized rehabilitation assessment.")
    user_input = st.text_input("", placeholder="Enter clinical symptoms or diagnosis...")
    
    if user_input:
        st.info("Clinical analysis in progress... Our system is being synchronized with the latest rehab protocols.")

with col2:
    st.markdown("<div class='feature-card'>", unsafe_allow_html=True)
    st.markdown("#### ✨ Clinical Vision")
    st.write("Specialized in restorative movement and evidence-based healing protocols.")
    st.markdown("---")
    st.markdown("Excellence Areas:")
    st.markdown("- Sports Medicine\n- Neurological Rehab\n- Orthopedic Recovery")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><br><p style='text-align: center; color: #999; font-size: 11px; letter-spacing: 3px;'>MOVE & HEAL • IMPACT BEGINS WITH A STEP • 2026</p>", unsafe_allow_html=True)
