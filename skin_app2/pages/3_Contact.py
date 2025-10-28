import streamlit as st
import datetime

st.set_page_config(page_title="Contact | DermaVision", page_icon="📬")

st.markdown("<h2 style='color:#5DADE2; text-align:center;'>📬 Contact & Feedback</h2>", unsafe_allow_html=True)
st.write("We value your feedback. Please share your thoughts or queries below!")

with st.form("feedback_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Email Address")
    feedback = st.text_area("Your Feedback or Message")
    submitted = st.form_submit_button("Submit Feedback 💌")

if submitted:
    if name and email and feedback:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("user_feedback.csv", "a", encoding="utf-8") as f:
            f.write(f"{timestamp},{name},{email},{feedback}\n")
        st.success("✅ Thank you! Your feedback has been recorded.")
    else:
        st.warning("⚠️ Please fill all fields before submitting.")

# --- FOOTER ---
st.markdown("<hr style='border: 1px solid gray;'>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color: gray;'>© 2025 DermaVision | Built with❤️ using Streamlit and TensorFlow | Developed by Anushka Khatua</p>",
    unsafe_allow_html=True
)