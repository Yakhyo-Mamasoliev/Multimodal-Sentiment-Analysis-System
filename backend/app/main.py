from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from PIL import Image
import io
from app.models.text_model import analyze_text_sentiment
from app.models.image_model import analyze_image_sentiment
from app.models.fusion_model import fuse_sentiments
from app.preprocessing import preprocess_text, preprocess_image

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins in development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Multimodal Sentiment Analysis API"}

@app.post("/analyze")
async def analyze_sentiment(
    text: str = Form(None),
    image: UploadFile = File(None)
):
    results = {}
    
    # Text analysis
    if text:
        processed_text = preprocess_text(text)
        text_sentiment = analyze_text_sentiment(processed_text)
        results["text_sentiment"] = text_sentiment
    
    # Image analysis
    if image:
        image_content = await image.read()
        pil_image = Image.open(io.BytesIO(image_content))
        processed_image = preprocess_image(pil_image)
        image_sentiment = analyze_image_sentiment(processed_image)
        results["image_sentiment"] = image_sentiment
    
    # Fusion if both are present
    if text and image:
        results["combined_sentiment"] = fuse_sentiments(
            results["text_sentiment"],
            results["image_sentiment"]
        )
    
    return results