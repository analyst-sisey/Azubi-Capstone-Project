# Azubi-Capstone-Project

# Introduction 
This repository contains a comprehensive projecct that analysed the movie reviews dataset on ZINDI and created 3 machine learning models to classify the reviews's sentiments. 3 Apps where then created to provide a user-friendly interface for non-technical users to easily interact with the models.The best performing model was then deployed using FastAPI for developers to incorporate the model into their own applications. Below is the details of each task.

# Data Analysis and Model Creation

The objective of this project is to analyse the Movie Review dataset available on ZINDI to develop a NLP machine learning model which when given a review sentence, classify whether the sentence is of positive, negative, or neutral sentiment. This objective was accomplished using the CRISP-DM methodology.
3 Models where created using pre-trained models from the Hugging Face platform. These models are:

- [x] Distilbert-Base-uncased: This is a smaller and faster version of the BERT model that has been trained on a smaller corpus of text. It is a good choice for sentiment analysis when speed is a concern.
- [x] XLNet-Base-cased: This is a pre-trained model that is based on a different type of neural network architecture called a transformer-XL. It has been shown to perform well on a variety of natural language processing tasks, including sentiment analysis.
- [x] GPT-2 (Generative Pre-trained Transformer 2) is a state-of-the-art natural language processing model developed by OpenAI. Since GPT-2 is specifically designed for wide range of tasks, it can be used for text classification tasks, including sentiment analysis. 

**The project notebook Movie_Review_Sentiment.ipynb in this repository contains detailed explanations and code for this project** 
This file was created using GOOGLE colab notebook.

[The article for this project can be found here](https://medium.com/@alihu.alhassan/from-data-to-prediction-a-comprehensive-guide-to-analyzing-visualizing-and-modeling-the-titanic-3ca458d4da83)

# APPs Creation for user Interaction
To make our model easily accessible to others, we have created 3 apps to provide a user-friendly interface that allows users to input their review and receive a prediction of their sentiment. It also allows users to compare the performance of the models. These apps are;


- [x] A Streamlit app that allows users to input their review and receive a prediction of their sentiment. 
- [x] A Gradio app that allows users to input their review and receive a prediction of their sentiment. 
- [x] A Gradio app that allows users to compare the performance of each model on a given review. 


# Developing an API using FastAPI

This project creates an API that is requested to interact with the model. The FastAPI is a RESTful API that can be used by developers to incorporate our model into their own applications.


# How to run this project

To run this app on your local machine, you need to have Python 3 installed. 
You can download Python 3 from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Once you have Python 3 installed, follow these steps to install the required libraries:
1.	Clone this repository to your local machine:

`git clone https://github.com/your-username/movie-review-sentiment-analysis.git` 

2.	Navigate to the project directory:

`cd movie-review-sentiment-analysis` 

3.	Install the required libraries:

`pip install -r requirements.txt` 


# Usage

To run the streamlit app, use the following command:
`streamlit run streamlitApp.py` 

To run the gradio app, use the following command:
`python gradioaApp.py` 

To run the api, use the following command:
`python api.py` 

This will launch the app in your web browser. You can enter a movie review in the text box and clicK ENTER to see the sentiment analysis results.
**Since we are fetching the model directly from hugging Face, this apps rquire interner connection to work**
# Contributing
If you would like to contribute to this project, feel free to fork the repository and submit a pull request. You can also submit issues or feature requests through the GitHub issue tracker.
# License
This project is licensed under the MIT License. See the LICENSE file for details.
