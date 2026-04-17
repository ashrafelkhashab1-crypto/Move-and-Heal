import streamlit as st
import google.generativeai as genai

# 1. أهم سطر: لازم يكون أول أمر برمجي عشان الموقع يفتح
st.set_page_config(page_title="Move & Heal Wellness", layout="centered")

# 2. العنوان والتنسيق
st.markdown("<h1 style='text-align: center; color: #16a085;'>MOVE & HEAL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>الرحاب، القاهرة - مساعدك الطبي الذكي</p>", unsafe_allow_html=True)
st.write("---")

# 3. المفتاح (استخدمت آخر واحد بعتيه في الصورة)
# ملحوظة: لو الخانات ظهرت وطلع لك 401، يبقى لازم تغيري المفتاح بواحد يبدأ بـ AIza
API_KEY = "AQ.Ab8RN6Llxv48ksuOtwLBt24F4dMlDt4oOPWW-k0ZRrS8wCPLEQ"

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception:
    pass

# 4. خانة السؤال (هتظهر دلوقتي 100% لأن ترتيب الكود اتصلح)
user_input = st.text_input("إزاي نقدر نساعدك النهاردة؟", placeholder="اكتبي سؤالك هنا...")

if user_input:
    try:
        with st.spinner('جاري الرد...'):
            response = model.generate_content(f"أنت خبير تأهيل رياضي. أجب على: {user_input}")
            st.success(response.text)
    except Exception as e:
        st.error(f"Error: {e}")

st.write("---")
st.caption("Move & Heal Clinic - Rehab City")
