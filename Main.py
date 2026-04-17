import streamlit as st
import google.generativeai as genai
import os

# 1. المفتاح الصح من صورتك
K = "AQ.Ab8RN6LemP5v2_pajAbGl4rmEERU0v19_5G_vH6I2I6SndL8"
genai.configure(api_key=K)

st.set_page_config(page_title="Move & Heal", layout="centered")

# 2. لو الصورة موجودة اعرضيها، لو لا اعرضي الاسم
if os.path.exists("logo.png"):
    st.image("logo.png", use_container_width=True)
else:
    st.markdown("<h1 style='text-align: center; color: #16a085;'>MOVE & HEAL</h1>", unsafe_allow_html=True)

st.write("---")

# 3. السؤال والرد
user_input = st.text_input("إزاي نقدر نساعدك النهاردة؟")

if user_input:
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"أنت خبير تأهيل رياضي بمركز Move & Heal. أجب بوضوح: {user_input}")
        st.success(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
 
