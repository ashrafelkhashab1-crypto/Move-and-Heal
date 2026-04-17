import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Move & Heal Clinic", page_icon="🌿", layout="wide")

# 2. Custom CSS for Logo and Styling
st.markdown("""
    <style>
    .main { background-color: #f0fdf9; }
    
    /* Logo Styling */
    .logo-container {
        text-align: center;
        padding: 20px;
        margin-bottom: 20px;
    }
    .logo-text {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: bold;
        font-size: 50px;
        color: #16a085; /* Turquoise */
        letter-spacing: 2px;
        margin: 0;
    }
    .logo-subtext {
        font-size: 18px;
        color: #d4af37; /* Gold */
        letter-spacing: 5px;
        text-transform: uppercase;
        margin-top: -10px;
    }
    
    /* Input and Boxes styling */
    .stTextInput>div>div>input { border: 2px solid #16a085; border-radius: 10px; }
    .welcome-card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        border-left: 5px solid #d4af37;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Custom Logo Header
st.markdown("""
    <div class="logo-container">
        <h1 class="logo-text">MOVE & HEAL</h1>
        <p class="logo-subtext">CLINIC</p>
    </div>
    """, unsafe_allow_html=True)

# 4. Main Content Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🩺 Digital Health Consultation")
    user_input = st.text_input("Ask about sports injuries, joints, or physical therapy:")
    
    if user_input:
        # Simple Logic for automated replies
        query = user_input.lower()
        if "acl" in query or "knee" in query:
            st.success("💡 Clinic Tip: Knee injuries often require strengthening the quadriceps to reduce joint load.")
        elif "ankle" in query or "sprain" in query:
            st.success("💡 Clinic Tip: For ankle sprains, follow the RICE protocol (Rest, Ice, Compression, Elevation) for the first 48 hours.")
        else:
            st.info("Thank you for your inquiry. Our medical system is being updated to provide you with a detailed response shortly.")

with col2:
    st.markdown("<div class='welcome-card'>", unsafe_allow_html=True)
    st.markdown("### ✨ Our Mission")
    st.write("Helping you move freely and heal safely. Every step counts towards your recovery.")
    st.markdown("---")
    st.markdown("📍 Specializations:\n- Sports Injury Rehab\n- Joint & Bone Health\n- Medical Awareness")
    st.markdown("</div>", unsafe_allow_html=True)

# 5. Footer
st.markdown("<br><br><p style='text-align: center; color: #7f8c8d;'>An impact begins with a step • Move & Heal 2026</p>", unsafe_allow_html=True)
