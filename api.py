from fastapi import FastAPI
from transformers import pipeline
import numpy as np

app = FastAPI()


model = pipeline('text-classification', model='allevelly/Movie_Review_Sentiment_Analysis')


@app.post('/predict')
async def predict_sentiment(text: str):
    result = model(text)
    sentiment = result[0]['label']
    score = result[0]['score']
    return {'sentiment': sentiment, 'score': score}


