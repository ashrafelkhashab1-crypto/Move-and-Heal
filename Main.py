import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Move & Heal Clinic", page_icon="🌿", layout="wide")

# 2. Custom CSS (Modified to avoid Syntax Error)
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    
    .hero-container {
        text-align: center;
        padding: 100px 20px !important;
        background-image: linear-gradient(rgba(22, 160, 133, 0.8), rgba(22, 160, 133, 0.9)), 
                          url('https://images.unsplash.com/photo-1598128558393-70ff21433be0?q=80&w=2000&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        border-radius: 20px;
        margin-bottom: 30px;
        color: white;
    }
    
    .logo-text {
        font-family: 'serif';
        font-weight: bold;
        font-size: 70px;
        color: #d4af37;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin: 0;
    }
    .logo-subtext {
        font-size: 22px;
        color: white;
        letter-spacing: 10px;
        text-transform: uppercase;
        margin-top: -10px;
    }
    
    .welcome-card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        border-top: 5px solid #d4af37;
        box-shadow: 0 6px 10px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Hero Header
st.markdown("""
    <div class="hero-container">
        <p class="logo-text">MOVE & HEAL</p>
        <p class="logo-subtext">CLINIC</p>
    </div>
    """, unsafe_allow_html=True)

# 4. Content Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🩺 Digital Health Consultation")
    user_input = st.text_input("Describe your symptoms or injury:", placeholder="e.g., knee pain, ankle sprain")
    
    if user_input:
        query = user_input.lower()
        if "knee" in query or "acl" in query:
            st.success("💡 Tip: Knee stability is key. Focus on quad strengthening exercises.")
        elif "ankle" in query:
            st.success("💡 Tip: Use compression and rest for early stage ankle recovery.")
        else:
            st.info("Thank you. We are analyzing your input to provide medical guidance.")

with col2:
    st.markdown("<div class='welcome-card'>", unsafe_allow_html=True)
    st.markdown("### ✨ Our Mission")
    st.write("Professional care for athletes and non-athletes. Healing through movement.")
    st.markdown("---")
    st.markdown("📍 Focus Areas:\n- Injury Prevention\n- Post-Surgical Rehab\n- Joint Health")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: #7f8c8d;'>An impact begins with a step • Move & Heal 2026</p>", unsafe_allow_html=True)

