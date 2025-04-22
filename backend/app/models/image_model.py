import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing import image

# Load pre-trained model
# In a real project, you'd fine-tune this for sentiment detection
base_model = MobileNetV2(weights='imagenet', include_top=True)

# We'll use the features from the base model to make a simple prediction
def analyze_image_sentiment(img_array):
    """
    A simplified version that uses image features to predict sentiment
    In a real project, you would use a model trained specifically for sentiment
    """
    try:
        # Preprocess the image for the model
        img_array = preprocess_input(img_array)
        
        # Get features from the base model
        features = base_model.predict(np.expand_dims(img_array, axis=0))
        
        # Simple heuristic: Use the average of the top 5 activations to determine sentiment
        # This is just for demonstration - a real system would use a trained classifier
        top_features = np.mean(np.sort(features[0])[-5:])
        
        # Normalize the score between -1 and 1
        sentiment_score = (top_features - 5) / 10  # Arbitrary normalization
        
        # Classify based on the score
        if sentiment_score > 0.2:
            sentiment = "positive"
        elif sentiment_score < -0.2:
            sentiment = "negative"
        else:
            sentiment = "neutral"
            
        return {
            "sentiment": sentiment,
            "score": float(sentiment_score),
            "confidence": abs(float(sentiment_score))
        }
    except Exception as e:
        print(f"Error in image sentiment analysis: {e}")
        return {
            "sentiment": "neutral",
            "score": 0.0,
            "confidence": 0.0
        }