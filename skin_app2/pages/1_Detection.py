import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import time

st.set_page_config(page_title="Detection | DermaVision", page_icon="🔍")

st.markdown("<h2 style='color:#5DADE2; text-align:center;'>🔍 Skin Disease Detection</h2>", unsafe_allow_html=True)
st.write("Upload a skin lesion image to analyze and get a personalized AI-based diagnosis.")

# --- Input Fields ---  
with st.form("detection_form"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=1, max_value=120, step=1)
    with col2:
        sex = st.selectbox("Sex", ["Male", "Female", "Other"])
    medical_history = st.text_area("Existing Medical Conditions (optional)", height=60)
    uploaded_file = st.file_uploader("Upload Skin Image", type=["jpg", "jpeg", "png"])
    analyze_btn = st.form_submit_button("Analyze 🔎")

if analyze_btn:
    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", width=300)
        st.info("🔄 Scanning... Please wait")

        # Simulated scanning bar  
        progress = st.progress(0)
        for percent in range(100):
            time.sleep(0.02)
            progress.progress(percent + 1)
        st.success("✅ Scanning Completed")

        # Load model (your model)  
        model = tf.keras.models.load_model("final_model.h5")

        # Preprocess image  
        img = image.resize((224, 224))
        img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

        # Predict  
        preds = model.predict(img_array)
        class_names = ["Melanoma (MEL)", "Melanocytic Nevus (NV)", "Basal Cell Carcinoma (BCC)", "Benign Keratosis (BKL)"]
        predicted_class = class_names[np.argmax(preds)]
        confidence = float(np.max(preds) * 100)

        st.markdown(f"<h4 style='color:#5DADE2;'>Prediction:</h4> <b>{predicted_class}</b>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='color:#5DADE2;'>Confidence:</h4> {confidence:.2f}%", unsafe_allow_html=True)

        # --- Description of the disease ---  
        st.markdown("### 📝 What this means")
        if "Melanoma" in predicted_class:
            st.write("Melanoma is a serious form of skin cancer that develops in pigment-producing cells (melanocytes). Early detection is critical for a good prognosis.")
        elif "Nevus" in predicted_class:
            st.write("A melanocytic nevus is commonly known as a mole — usually benign, but changes in size, shape or colour should be monitored.")
        elif "Basal" in predicted_class:
            st.write("Basal cell carcinoma is the most common skin cancer type. It grows slowly, often in sun-exposed areas, and rarely spreads but should be treated early.")
        elif "Keratosis" in predicted_class:
            st.write("Benign keratosis-like lesions are non-cancerous growths often due to sun damage or ageing — usually harmless but monitoring is wise.")

        # --- Dynamic Guidelines ---  
        st.markdown("---")
        st.subheader("📋 General Guidelines")
        if "Melanoma" in predicted_class:
            st.write("""
            - Immediately consult a dermatologist for evaluation and possible biopsy.  
            - Monitor the lesion for asymmetry, irregular borders, colour variation, or increase in size.  
            - Avoid intense sun exposure and tanning beds; wear SPF 50+ daily.  
            - Perform monthly self-exams of skin and have annual professional checks, especially if older than 50.
            """)
        elif "Nevus" in predicted_class:
            st.write("""
            - Usually harmless, but keep an eye for changes: itchiness, bleeding, rapid growth.  
            - Use broad-spectrum sunscreen and limit sun exposure.  
            - Consider professional check if many moles or family history of skin cancer.
            """)
        elif "Basal" in predicted_class:
            st.write("""
            - Early removal or treatment reduces risk of local tissue damage.  
            - Wear protective clothing and sunscreen; avoid repeated sunburns.  
            - Annual skin exam is advisable if over 60 or with significant sun history.
            """)
        elif "Keratosis" in predicted_class:
            st.write("""
            - Though benign, these lesions may irritate or change; keep skin moisturized.  
            - Use SPF daily and avoid peak UV hours.  
            - Seek check-up if lesion starts bleeding, itching, or growing in older age.
            """)

        # --- Age-group screening/notes ---  
        st.markdown("---")
        if age < 20:
            st.info("👦 Teen/Young adult: While skin issues are less likely serious, keep good sun-protection habits and get a skin check if you notice any unusual growth.")
        elif age > 60:
            st.warning("👴👵 Senior adult: Skin cancer risk increases with age. Regular professional skin exams (once yearly) and thorough self-checks every 3-6 months are strongly encouraged. {If you have sun-damage history, prioritize a dermatologist visit.}")
        else:
            st.write("🧑 Adult (20-60): Maintain sun protection, monitor any changing lesions annually, and consult a dermatologist especially if history of sun exposure or skin cancer risk factors.")

    else:
        st.warning("⚠️ Please upload an image before analyzing.")
