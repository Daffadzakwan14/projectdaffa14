import streamlit as st
from PIL import Image
import io

# Judul aplikasi
st.title("Image Rotation App")

# Instruksi
st.write("Unggah gambar, pilih sudut rotasi, dan unduh hasilnya dalam format PNG, JPG, atau PDF.")

# Mengunggah gambar
uploaded_file = st.file_uploader("Upload an image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

# Slider untuk menentukan sudut rotasi
rotation_angle = st.slider(
    "Rotation Angle (in degrees)", 
    min_value=0, 
    max_value=360, 
    value=0, 
    step=1, 
    help="Pilih sudut untuk memutar gambar (0-360 derajat)."
)

if uploaded_file is not None:
    # Membaca file gambar
    img = Image.open(uploaded_file)
    
    # Menampilkan gambar asli
    st.subheader("Original Image")
    st.image(img, caption="Original Image", use_column_width=True)
    
    # Melakukan rotasi pada gambar
    rotated_img = img.rotate(rotation_angle, expand=True)
    
    # Menampilkan gambar hasil rotasi
    st.subheader("Rotated Image")
    st.image(rotated_img, caption=f"Rotated Image ({rotation_angle}°)", use_column_width=True)
    
    # Opsi format unduhan
    st.subheader("Download Rotated Image")
    format_option = st.radio(
        "Choose the file format to download:",
        options=["PNG", "JPG", "PDF"]
    )
    
    # Konversi ke format yang dipilih dan unduh
    if format_option == "PNG":
        buffer = io.BytesIO()
        rotated_img.save(buffer, format="PNG")
        st.download_button(
            label="Download as PNG",
            data=buffer.getvalue(),
            file_name="rotated_image.png",
            mime="image/png"
        )
    elif format_option == "JPG":
        buffer = io.BytesIO()
        rotated_img.convert("RGB").save(buffer, format="JPEG")
        st.download_button(
            label="Download as JPG",
            data=buffer.getvalue(),
            file_name="rotated_image.jpg",
            mime="image/jpeg"
        )
    elif format_option == "PDF":
        buffer = io.BytesIO()
        rotated_img.convert("RGB").save(buffer, format="PDF")
        st.download_button(
            label="Download as PDF",
            data=buffer.getvalue(),
            file_name="rotated_image.pdf",
            mime="application/pdf"
        )
