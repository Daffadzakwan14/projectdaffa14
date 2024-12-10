import streamlit as st
from PIL import Image

# Judul aplikasi
st.title("Image Rotation App")

# Instruksi
st.write("Unggah gambar, pilih sudut rotasi, dan unduh hasilnya.")

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
    
    # Menyediakan tombol untuk mengunduh gambar hasil rotasi
    st.subheader("Download Rotated Image")
    rotated_img_path = "rotated_image.png"
    rotated_img.save(rotated_img_path)
    
    with open(rotated_img_path, "rb") as file:
        st.download_button(
            label="Download Rotated Image",
            data=file,
            file_name="rotated_image.png",
            mime="image/png"
        )
