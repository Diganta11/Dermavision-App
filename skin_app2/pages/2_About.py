import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Insights | DermaVision", page_icon="📊")

# --- Header ---
st.markdown("<h2 style='color:#58D68D; text-align:center;'>📊 DermaVision Insights</h2>", unsafe_allow_html=True)
st.write("")

# --- Section 1: About ---
st.markdown("<h4 style='color:#58D68D;'>🩺 About DermaVision</h4>", unsafe_allow_html=True)
st.write("""
DermaVision is an AI-powered skin lesion assessment platform built to assist early diagnosis 
of common dermatological conditions. It analyzes uploaded skin images and provides a 
preliminary classification among major skin diseases.
""")

# --- Section 2: How It Works ---
st.markdown("<h4 style='color:#58D68D;'>⚙️ How It Works</h4>", unsafe_allow_html=True)
st.write("""
The system uses a deep learning model trained on a large curated dataset of dermatological 
images (top 4 classes: **MEL**, **NV**, **BCC**, **BKL**). The prediction combines visual 
features with optional user inputs like **age**, **sex**, and **medical history** to 
generate a more personalized assessment.
""")

# --- Section 3: Model Highlights ---
st.markdown("<h4 style='color:#58D68D;'>📈 Model Highlights</h4>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
col1.metric("Classes", "4 major types")
col2.metric("Model Accuracy", "88.24%")
col3.metric("Images Trained On", "20,000+")

# --- Section 4: Research Outlook ---
st.markdown("<h4 style='color:#58D68D;'>🔬 Research Outlook</h4>", unsafe_allow_html=True)
st.write("""
Future versions will integrate broader datasets, include rare skin disorders, 
and support video-based lesion tracking for better long-term monitoring.
""")

# --- FOOTER ---
st.markdown("<hr style='border: 1px solid gray;'>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color: gray;'>© 2025 DermaVision | Built with ❤️ using Streamlit and TensorFlow | Developed by Anushka Khatua</p>",
    unsafe_allow_html=True
)
