import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

# Maximum size allowed for processing
MAX_WIDTH = 8000
MAX_HEIGHT = 8000

# Function to apply the Laplacian filter to an image
def apply_laplacian(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    laplacian_8u = cv2.convertScaleAbs(laplacian)
    laplacian_color = cv2.cvtColor(laplacian_8u, cv2.COLOR_GRAY2BGR)
    result = cv2.addWeighted(image, 0.8, laplacian_color, 0.2, 0)
    return result

# Function to resize the image if it's too large
def resize_image(image):
    height, width = image.shape[:2]
    if width > MAX_WIDTH or height > MAX_HEIGHT:
        scale = min(MAX_WIDTH / width, MAX_HEIGHT / height)
        new_size = (int(width * scale), int(height * scale))
        resized_image = cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)
        return resized_image
    return image

# Function to improve image resolution and quality
def enhance_image(image):
    # Resize image if necessary
    image = resize_image(image)
    
    # Load the super resolution model
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel("EDSR_x3.pb")  # Example model, you may use other models like "EDSR_x2.pb"
    sr.setModel("edsr", 3)  # Use EDSR model with scaling factor of 3

    # Apply super resolution
    upscaled_image = sr.upsample(image)

    # Denoise the image
    denoised_image = cv2.fastNlMeansDenoisingColored(upscaled_image, None, 10, 10, 7, 21)

    # Sharpen the image
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened_image = cv2.filter2D(denoised_image, -1, kernel)

    return sharpened_image

# Convert OpenCV image to bytes
def image_to_bytes(image):
    _, buffer = cv2.imencode('.jpg', image)
    return buffer.tobytes()

# Streamlit application
st.title("Image Enhancement")
st.write("Upload an image to apply Laplacian edge detection, improve resolution and quality, and download the enhanced image.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert the file to an OpenCV image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    # Apply Laplacian filter
    processed_image = apply_laplacian(image)

    # Enhance image resolution and quality
    enhanced_image = enhance_image(processed_image)

    # Convert processed image to displayable format
    st.image(image, caption='Original Image', use_column_width=True)
    st.image(processed_image, caption='Processed Image with Laplacian Filter', use_column_width=True)
    st.image(enhanced_image, caption='Enhanced Image', use_column_width=True)

    # Convert enhanced image to bytes
    enhanced_image_bytes = image_to_bytes(enhanced_image)

    # Create a download button
    st.download_button(
        label="Download Enhanced Image",
        data=enhanced_image_bytes,
        file_name="enhanced_image.jpg",
        mime="image/jpeg"
    )
