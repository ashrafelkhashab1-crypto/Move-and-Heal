import streamlit as st

# 1. Page Configuration (Keep Wide Layout)
st.set_page_config(page_title="Move & Heal Clinic", page_icon="🌿", layout="wide")

# 2. Custom CSS for High-End Design
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    
    /* Hero Header Styling with Image Background */
    .hero-container {
        text-align: center;
        padding: 100px 20px;
        background-image: linear-gradient(rgba(22, 160, 133, 0.8), rgba(22, 160, 133, 0.9)), 
                          url('https://images.unsplash.com/photo-1598128558393-70ff21433be0?q=80&w=2000&auto=format&fit=crop'); /* High-end Clinic image */
        background-size: cover;
        background-position: center;
        border-radius: 20px;
        margin-bottom: 30px;
        color: white;
    }
    
    /* Elegant Logo Styling */
    .logo-text {
        font-family: 'Times New Roman', Times, serif; /* Luxury serif font */
        font-weight: bold;
        font-size: 75px;
        color: #d4af37; /* Royal Gold */
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin: 0;
        letter-spacing: 3px;

import streamlit as st

# 1. Page Configuration (Keep Wide Layout)
st.set_page_config(page_title="Move & Heal Clinic", page_icon="🌿", layout="wide")

# 2. Custom CSS for High-End Design
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    
    /* Hero Header Styling with Image Background */
    .hero-container {
        text-align: center;
        padding: 100px 20px;
        background-image: linear-gradient(rgba(22, 160, 133, 0.8), rgba(22, 160, 133, 0.9)), 
                          url('https://images.unsplash.com/photo-1598128558393-70ff21433be0?q=80&w=2000&auto=format&fit=crop'); /* High-end Clinic image */
        background-size: cover;
        background-position: center;
        border-radius: 20px;
        margin-bottom: 30px;
        color: white;
    }
    
    /* Elegant Logo Styling */
    .logo-text {
        font-family: 'Times New Roman', Times, serif; /* Luxury serif font */
        font-weight: bold;
        font-size: 75px;
        color: #d4af37; /* Royal Gold */
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin: 0;
        letter-spacing: 3px;
    }
    .logo-subtext {
        font-size: 25px;
        color: white; /* Clean white for contrast */
        letter-spacing: 12px;
        text-transform: uppercase;
        margin-top: -15px;
        opacity: 0.9;
    }
    
    /* Input and Box styling */
    .stTextInput>div>div>input { border: 2px solid #16a085; border-radius: 12px; height: 50px; }
    .welcome-card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        border-top: 5px solid #d4af37;
        box-shadow: 0 6px 10px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Professional Hero Header with Logo and Image
st.markdown("""
    <div class="hero-container">
        <h1 class="logo-text">MOVE & HEAL</h1>
        <p class="logo-subtext">CLINIC</p>
    </div>
    """, unsafe_allow_html=True)

# 4. Main Content Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🩺 Digital Health Consultation")
    user_input = st.text_input("Describe your symptoms, injury, or therapy goal:", placeholder="e.g., knee pain when running, post-ACL surgery")
    
    if user_input:
        # Simple Logic for automated replies
        query = user_input.lower()
        if "acl" in query or "knee" in query:
            st.success("💡 Clinic Tip: ACL recovery usually focuses on strengthening the quadriceps and improving range of motion.")
        elif "ankle" in query or "sprain" in query:
            st.success("💡 Clinic Tip: For ankle sprains, follow the RICE protocol (Rest, Ice, Compression, Elevation) immediately.")
        else:
            st.info("Thank you for sharing. We are setting up our medical AI to give you tailored advice shortly.")

with col2:
    st.markdown("<div class='welcome-card'>", unsafe_allow_html=True)
    st.markdown("### ✨ Our Mission")
    st.write("Helping you move freely and heal safely. Every step counts towards your recovery.")
    st.markdown("---")
    st.markdown("📍 Specializations:\n- Sports Injury Rehab\n- Joint & Bone Health\n- Performance Optimization")
    st.markdown("</div>", unsafe_allow_html=True)

# 5. Footer
st.markdown("<br><br><p style='text-align: center; color: #7f8c8d;'>An impact begins with a step • Move & Heal 2026</p>", unsafe_allow_html=True)

