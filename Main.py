import streamlit as st

# 1. إعدادات المتصفح
st.set_page_config(page_title="Move & Heal Clinic", page_icon="🌿", layout="wide")

# 2. لمسة جمالية بالألوان (تيركواز وذهبي)
st.markdown("""
    <style>
    .main { background-color: #f0fdf9; }
    .stTextInput>div>div>input { border: 2px solid #16a085; }
    h1 { color: #16a085; text-align: center; border-bottom: 2px solid #d4af37; padding-bottom: 10px; }
    .footer { position: fixed; bottom: 0; width: 100%; text-align: center; color: #7f8c8d; font-size: 14px; }
    </style>
    """, unsafe_allow_html=True)

# 3. محتوى الموقع
st.markdown("<h1>MOVE & HEAL CLINIC 🌿</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🩺 استشاراتك الطبية الذكية")
    user_input = st.text_input("اسألي عن إصابات الملاعب، المفاصل، أو التأهيل الطبيعي:")
    
    if user_input:
        if "صليبي" in user_input or "ركبة" in user_input:
            st.success("💡 نصيحة دكتورة العيادة: إصابات الركبة تتطلب تقوية لعضلات الـ Quadriceps لتقليل الحمل على المفصل.")
        elif "كاحل" in user_input or "التواء" in user_input:
            st.success("💡 نصيحة دكتورة العيادة: في أول 48 ساعة من الالتواء، نطبق قاعدة RICE (راحة - ثلج - ضغط - رفع).")
        else:
            st.info("شكراً لتواصلك.. سيتم الرد على استشارتك من خلال نظامنا الطبي المحدث قريباً.")

with col2:
    st.markdown("### ✨ رسالة العيادة")
    st.info("نحن هنا لنساعدك على العودة للحركة بحرية وأمان. كل خطوة محسوبة هي طريقك للشفاء.")
    st.markdown("---")
    st.markdown("📍 تخصصاتنا:\n- تأهيل إصابات الملاعب\n- صحة المفاصل والعظام\n- الوعي الطبي للرياضيين")

# 4. التذييل
st.markdown("<div class='footer'>تأثير يبدأ بخطوة • Move & Heal 2026</div>", unsafe_allow_html=True)
