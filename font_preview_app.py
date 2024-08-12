import streamlit as st
import os
from PIL import Image, ImageDraw, ImageFont
import io

# App name
APP_NAME = "FontFolio"

# Function to load fonts from the 'fonts' folder
def load_fonts(fonts_dir):
    fonts = {}
    for filename in os.listdir(fonts_dir):
        if filename.endswith(('.ttf', '.otf')):
            font_path = os.path.join(fonts_dir, filename)
            font_name = os.path.splitext(filename)[0]
            fonts[font_name] = font_path
    return fonts

# Function to render text with a specific font
def render_text(text, font_path, font_size=144):
    font = ImageFont.truetype(font_path, font_size)
    image = Image.new('RGB', (500, 500), color='white')
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), text, font=font, fill='black')
    return image

# Set page title
st.set_page_config(page_title=f"{APP_NAME}: Interactive Font Preview")

# Main app layout
st.title(f"{APP_NAME}: Interactive Font Preview")

# Load fonts from the 'fonts' folder
fonts_dir = 'fonts'
fonts = load_fonts(fonts_dir)

# Sidebar for input and font selection
with st.sidebar:
    st.header("Input")
    user_text = st.text_area("Enter text to preview:", value="Hello, World!")
    
    st.header("Font Selection")
    selected_font = st.selectbox("Choose a font:", list(fonts.keys()))

# Main content area for text preview
st.header("Preview")
if selected_font in fonts:
    preview_image = render_text(user_text, fonts[selected_font])
    st.image(preview_image, use_column_width=True)
else:
    st.error("Selected font not found.")

# Additional information
st.info(f"Note: {APP_NAME} uses custom fonts loaded from the 'fonts' folder.")

# Optional: Display font information
st.subheader("Font Details")
st.write(f"Font Name: {selected_font}")
st.write(f"Font File: {os.path.basename(fonts[selected_font])}")

# Footer
st.markdown(f"---\n*{APP_NAME} - Your Personal Font Showcase*")