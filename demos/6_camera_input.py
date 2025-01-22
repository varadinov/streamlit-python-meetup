import streamlit as st
from PIL import Image
from io import BytesIO
from rembg import remove

enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    input_image = Image.open(BytesIO(picture.getvalue()))
    with st.spinner("Processing the image to remove background..."):
        output_image = remove(input_image)  # Remove background using rembg

    st.image(output_image, use_container_width=True)