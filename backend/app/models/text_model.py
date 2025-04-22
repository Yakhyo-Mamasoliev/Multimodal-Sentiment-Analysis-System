from transformers import pipeline
import numpy as np

# Simple text sentiment analyzer using Hugging Face transformers
# In a real project, you might fine-tune or train your own model
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_text_sentiment(text):
    """
    Analyze sentiment of the given text
    Returns sentiment (positive/negative/neutral) and score
    """
    # For a simple project, we're using a pre-trained model
    try:
        result = sentiment_analyzer(text)[0]
        
        # Convert to common format
        label = result["label"].lower()
        score = result["score"]
        
        # Map LABEL_0 and LABEL_1 to negative and positive if needed
        if label == "label_0":
            label = "negative"
        elif label == "label_1":
            label = "positive"
            
        # Normalize score between -1 and 1
        if label == "negative":
            normalized_score = -score
        else:
            normalized_score = score
            
        return {
            "sentiment": label,
            "score": normalized_score,
            "confidence": score
        }
    except Exception as e:
        print(f"Error in text sentiment analysis: {e}")
        return {
            "sentiment": "neutral",
            "score": 0.0,
            "confidence": 0.0
        }