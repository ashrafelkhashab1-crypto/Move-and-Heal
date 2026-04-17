import streamlit as st
import google.generativeai as genai
import os

# 1. إعدادات الصفحة
st.set_page_config(page_title="Move & Heal", layout="centered")

# 2. المفتاح اللي في صورتك الأخيرة (تأكدي إنه بين علامتين تنصيص)
GOOGLE_API_KEY = "AQ.Ab8RN6Llxv48ksuOtwLBt24F4dMlDt4oOPWW-k0ZRrS8wCPLEQ"
genai.configure(api_key=GOOGLE_API_KEY)

# 3. عرض العنوان أو اللوجو
st.markdown("<h1 style='text-align: center; color: #16a085;'>MOVE & HEAL</h1>", unsafe_allow_html=True)
st.write("---")

# 4. خانة السؤال (دي أهم حتة لازم تظهر)
user_input = st.text_input("إزاي نقدر نساعدك النهاردة؟", placeholder="اكتبي سؤالك هنا...")

if user_input:
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"أنت خبير في Move & Heal. أجب على: {user_input}")
        st.success(response.text)
    except Exception as e:
        st.error(f"Error: {e}")

# 5. لو حابة تضيفي الـ CSS خليه في الآخر خالص عشان ما يعطلش الكود
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    </style>
    """, unsafe_allow_html=True)
