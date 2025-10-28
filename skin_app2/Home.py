import streamlit as st

st.set_page_config(page_title="Home | DermaVision", page_icon="🏠")

# --- Title ---
st.markdown("<h2 style='color:#5DADE2; text-align:center;'>🏥 Welcome to DermaVision</h2>", unsafe_allow_html=True)

# --- Description ---
st.write("""
An AI-driven dermatology assistant that analyzes skin lesions using advanced deep learning models, helping users gain early awareness and reliable guidance for better skin health.

Upload your image on the **Detection** page to get a detailed diagnosis and preventive insights.
""")

# --- Highlights Section ---
st.markdown("---")
st.subheader("🌟 Key Features")
st.markdown("""
- 🔍 **AI-based Skin Disease Detection** — Fast, accurate, and informative.  
- 📊 **Confidence Scores & Guidelines** — Understand your result better.  
- 🧠 **Smart Insights** — Personalized health advice based on your age group.  
- 💬 **Contact Page** — Share feedback or connect with the developer.  
""")

# --- FOOTER ---
st.markdown("<hr style='border: 1px solid gray;'>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color: gray;'>© 2025 DermaVision | Built with ❤️ using Streamlit and TensorFlow | Developed by Anushka Khatua</p>",
    unsafe_allow_html=True
)