import streamlit as st
import google.generativeai as genai
import os

# 1. المفتاح الخاص بكِ جاهز هنا
GOOGLE_API_KEY = "AQ.Ab8RN6Llxv48ksuOtwLBt24F4dMlDt4oOPWW-k0ZRrS8wCPLEQ".strip()
genai.configure(api_key=GOOGLE_API_KEY)

# 2. إعدادات الصفحة
st.set_page_config(
    page_title="Move & Heal Wellness Center",
    page_icon="🏥",
    layout="centered"
)

# 3. تصميم الـ CSS الفاخر (الألوان والخطوط)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .title-container { text-align: center; padding: 20px; }
    .main-title { color: #2c3e50; font-size: 45px; font-weight: bold; margin-bottom: 0px; }
    .sub-title { color: #16a085; font-size: 20px; letter-spacing: 2px; font-weight: bold; }
    .response-area { 
        padding: 20px; 
        background-color: white; 
        border-radius: 15px; 
        border-left: 5px solid #16a085;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. محتوى الصفحة
# هنا الكود بيشوف: لو الصورة موجودة بيعرضها، لو مش موجودة بيعرض الاسم نص عادي
if os.path.exists("logo.png"):
    st.image("logo.png", width=250)
else:
    st.markdown('<div class="title-container"><h1 class="main-title">MOVE & HEAL</h1><p class="sub-title">WELLNESS CENTER</p></div>', unsafe_allow_html=True)

st.info("👋 مرحباً بكِ في Move & Heal بالرحاب. اسألي أي سؤال عن العلاج الطبيعي والتأهيل.")

st.write("---")

user_input = st.text_input("إزاي نقدر نساعدك النهاردة؟", placeholder="اكتبي سؤالك هنا...")

if user_input:
    try:
        with st.spinner('جاري استشارة خبير Move & Heal...'):
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = f"أنت خبير في التأهيل الرياضي بمركز Move & Heal. أجب بوضوح على: {user_input}"
            response = model.generate_content(prompt)
            
            st.markdown('<div class="response-area">', unsafe_allow_html=True)
            st.markdown("### الإجابة:")
            st.success(response.text)
            st.markdown('</div>', unsafe_allow_html=True)
    except Exception as e:
        st.error(f"حدث خطأ: {e}")

st.write("---")
st.markdown("<p style='text-align: center; color: gray;'>📍 EL REHAB CITY, CAIRO</p>", unsafe_allow_html=True)
 
