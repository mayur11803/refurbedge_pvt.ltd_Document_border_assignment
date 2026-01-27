import streamlit as st
import cv2
import numpy as np
from detector import detect_document

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Document Detection",
    layout="centered"
)

st.title("Real-Time Document Detection")
st.caption("Works on PC & Mobile | Upload or Capture using Camera")

# --- INPUT OPTIONS ---
option = st.radio(
    "Choose input method:",
    ("Upload Image", "Use Camera"),
    horizontal=True
)

image = None

# --- UPLOAD IMAGE ---
if option == "Upload Image":
    uploaded_file = st.file_uploader(
        "Upload ID Card / Document Image",
        type=["jpg", "jpeg", "png"]
    )
    if uploaded_file is not None:
        file_bytes = np.asarray(
            bytearray(uploaded_file.read()),
            dtype=np.uint8
        )
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

# --- CAMERA INPUT ---
elif option == "Use Camera":
    camera_image = st.camera_input("Capture document")
    if camera_image is not None:
        file_bytes = np.asarray(
            bytearray(camera_image.getvalue()),
            dtype=np.uint8
        )
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

# --- PROCESS IMAGE ---
if image is not None:
    st.subheader("Original Image")
    st.image(image, channels="BGR", use_container_width=True)

    with st.spinner("Detecting document..."):
        bordered, cropped = detect_document(image)

    if bordered is not None:
        st.success("Document detected")

        st.subheader("Detected Document (with Border)")
        st.image(bordered, channels="BGR", use_container_width=True)

        st.subheader("Extracted Document")
        st.image(cropped, channels="BGR", use_container_width=True)
    else:
        st.error("Document not detected. Try a clearer image.")
