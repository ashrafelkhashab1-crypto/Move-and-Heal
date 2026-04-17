import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Move & Heal Clinic", page_icon="🌿", layout="centered")

# تصميم احترافي بسيط
st.markdown("""
    <style>
    .main { background-color: #f0fdfa; }
    h1 { color: #16a085; text-align: center; font-family: 'Arial'; }
    .stButton>button { background-color: #d4af37; color: white; width: 100%; border-radius: 20px; }
    .welcome-box { padding: 20px; border-radius: 15px; border: 2px solid #d4af37; text-align: center; background-color: white; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>MOVE & HEAL CLINIC</h1>", unsafe_allow_html=True)
st.markdown("<div class='welcome-box'><h3>أهلاً بيكي يا دكتورة في موقعك الجديد ✨</h3><p>الموقع شغال وجاهز للربط بالذكاء الاصطناعي</p></div>", unsafe_allow_html=True)

st.write("---")

# خانة الدردشة (مؤقتة)
user_input = st.text_input("إزاي نقدر نساعدك في إصابات الملاعب أو المفاصل؟")

if user_input:
    st.info("تم استلام سؤالك.. بنحدث حالياً نظام الرد التلقائي ليناسب استشاراتك.")

# قسم النصائح
st.subheader("💡 نصيحة Move & Heal")
st.success("الوقاية من إصابات الرباط الصليبي بتبدأ بتمارين تقوية العضلات المحيطة بالركبة.")
