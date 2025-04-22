def fuse_sentiments(text_result, image_result):
    """
    Simple fusion mechanism that combines text and image sentiment scores
    
    Args:
        text_result: Dictionary with text sentiment analysis
        image_result: Dictionary with image sentiment analysis
        
    Returns:
        Dictionary with combined sentiment analysis
    """
    # Weighted average of scores (giving more weight to text)
    text_weight = 0.7
    image_weight = 0.3
    
    combined_score = (text_result['score'] * text_weight + 
                      image_result['score'] * image_weight)
    
    # Determine sentiment based on the combined score
    if combined_score > 0.15:
        sentiment = "positive"
    elif combined_score < -0.15:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    
    # Calculate confidence
    combined_confidence = (text_result['confidence'] * text_weight + 
                           image_result['confidence'] * image_weight)
    
    return {
        "sentiment": sentiment,
        "score": float(combined_score),
        "confidence": float(combined_confidence),
        "text_contribution": text_weight,
        "image_contribution": image_weight
    }