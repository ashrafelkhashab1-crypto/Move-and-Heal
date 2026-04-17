import streamlit as st
import google.generativeai as genai

# 1. إعدادات الصفحة (لازم تكون أول سطر بعد الـ import)
st.set_page_config(page_title="Move & Heal", layout="centered")

# 2. المفتاح (لازم يبدأ بـ AIza عشان يشتغل "هناك")
GOOGLE_API_KEY = "حطي_المفتاح_اللي_أوله_AIza_هنا"
genai.configure(api_key=GOOGLE_API_KEY)

# 3. العنوان
st.markdown("<h1 style='text-align: center; color: #16a085;'>MOVE & HEAL</h1>", unsafe_allow_html=True)
st.write("---")

# 4. خانة السؤال (تأكدي من الأقواس دي)
user_input = st.text_input("إزاي نقدر نساعدك النهاردة؟", placeholder="اكتبي سؤالك هنا...")

if user_input:
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"أنت خبير تأهيل رياضي بمركز Move & Heal. أجب بوضوح: {user_input}")
        st.success(response.text)
    except Exception as e:
        st.error(f"الخطأ في المفتاح: {e}")
        
