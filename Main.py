import streamlit as st
import google.generativeai as genai

# إعداد مفتاح الذكاء الاصطناعي الخاص بكِ
genai.configure(api_key="AQ.Ab8RN6IAYlYH6SdebaBLh-lIm5b8yom6GyegDdAwAxbhLbDaYg")

# إعدادات الصفحة
st.set_page_config(page_title="Move & Heal Wellness Center", page_icon="🏥")

# تصميم الواجهة
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .title-text {
        color: #2c3e50;
        text-align: center;
        font-family: 'Arial';
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='title-text'>MOVE & HEAL</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #16a085;'>WELLNESS CENTER</h3>", unsafe_allow_html=True)

st.write("---")

# رسالة الترحيب
st.info("Your journey from injury to the peak of performance starts here, at the heart of El Rehab City.")

# الجزء التفاعلي
st.subheader("إزاي نقدر نساعدك في رحلة تعافيك؟")
user_input = st.text_input("اكتب سؤالك هنا:")

if user_input:
    try:
        with st.spinner('جاري استشارة خبير الذكاء الاصطناعي...'):
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(user_input)
            st.markdown("### الرد:")
            st.write(response.text)
    except Exception as e:
        st.error(f"حصلت مشكلة بسيطة: {e}")

st.write("---")
st.caption("📍 EL REHAB CITY, CAIRO")
