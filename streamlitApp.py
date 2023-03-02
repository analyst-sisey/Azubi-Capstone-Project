import streamlit as st
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import base64

@st.cache(allow_output_mutation=True)
def load_model():
    model_name = "allevelly/Movie_Review_Sentiment_Analysis"
    model = AutoModelForSequenceClassification.from_pretrained(model_name,id2label={0: 'negative review', 1: 'positive review'})
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer

model, tokenizer = load_model()


def predict_sentiment(review):
    inputs = tokenizer.encode_plus(
        review,
        max_length=512,
        add_special_tokens=True,
        return_token_type_ids=False,
        padding='max_length',
        return_attention_mask=True,
        return_tensors='pt',
    )

    outputs = model(**inputs)
    logits = outputs.logits
    probabilities = torch.softmax(logits, dim=1).detach().cpu().tolist()[0]

    return probabilities
#add background image to th app
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('image1.jpg')    
# Add a title and intro text
st.title("Movie Review Sentiment Analysis")

review = st.text_input("Enter a movie review and press ENTER:")
if review:
    probabilities = predict_sentiment(review)
    if probabilities[1] >= 0.6:
        st.header("This Movie Review is Positive ")
    else:
        st.header("This Movie Review is Negative ")
        
    st.write("Positive Review:", probabilities[1])
    st.write("Negative Review:", probabilities[0])
st.balloons()