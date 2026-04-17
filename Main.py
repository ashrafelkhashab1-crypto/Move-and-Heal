import streamlit as st
import google.generativeai as genai

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="Move & Heal Wellness", layout="centered")

# 2. العنوان وشكل الموقع
st.markdown("<h1 style='text-align: center; color: #16a085;'>MOVE & HEAL</h1>", unsafe_allow_html=True)
st.write("---")

# 3. الربط بالمفتاح (بطريقة السرية)
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    st.error("المفتاح غير موجود في الإعدادات السرية (Secrets)")

# 4. خانة السؤال والرد
user_input = st.text_input("إزاي نقدر نساعدك النهاردة؟")

if user_input:
    try:
        response = model.generate_content(user_input)
        st.success(response.text)
    except Exception as e:
        st.error(f"حدث خطأ: {e}")
