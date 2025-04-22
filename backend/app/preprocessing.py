import re
import numpy as np
from PIL import Image

def preprocess_text(text):
    """
    Basic text preprocessing
    """
    if not text:
        return ""
        
    # Convert to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    
    # Remove user mentions (like @username)
    text = re.sub(r'@\w+', '', text)
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def preprocess_image(pil_image):
    """
    Preprocess image for the model
    """
    # Resize the image
    pil_image = pil_image.resize((224, 224))
    
    # Convert PIL image to numpy array
    img_array = np.array(pil_image)
    
    # Handle grayscale images
    if len(img_array.shape) == 2:
        img_array = np.stack([img_array, img_array, img_array], axis=-1)
    
    # Ensure the image has 3 channels (RGB)
    if img_array.shape[-1] > 3:
        img_array = img_array[:, :, :3]
    
    return img_array