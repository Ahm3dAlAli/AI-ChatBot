# 🤖Cognitive Assistance Chatbot 💬 
Welcome to part of the backened development of Cognitive Assistance Chatbot by OpenFabric! This chatbot is designed to provide users with quick and accurate answers to science-related questions using advanced NLP technology.

## Introduction
This chatbot is an AI solution for those seeking fast and accurate answers to science-related questions. Our chatbot utilizes advanced NLP technology to process user queries and provide relevant answers in real-time. It is powered by the BERT (Bidirectional Encoder Representations from Transformers) model, which is trained on a massive amount of text data and can provide highly accurate responses to a wide range of science-related questions. The chatbot is implemented in Python using the transformers library by Hugging Face.

## Usage
To use the chatbot, simply input a science-related question followed by a context (i.e., a text snippet containing the information needed to answer the question), separated by the delimiter |||. The chatbot will process your query and generate an answer.

For example, the following input would generate a response to the question "What is the atomic number of carbon?":

What is the atomic number of carbon? ||| The atomic number of carbon is 6.

## Running the App
To run the chatbot app, you can either run the start.sh script locally or use the Dockerfile to build a Docker image of the app and run it in a container.

## Local Execution
To run the app locally, make sure you have Python 3.8 or later installed on your system and run the following commands:

$ pip install -r requirements.txt
$ sh start.sh

This will start the app on your local machine at http://localhost:5000.

## Docker Execution
To build a Docker image of the app and run it in a container, make sure you have Docker installed on your system and run the following commands:


$ docker build -t cognitive-assistance-chatbot .
$ docker run -p 5000:5000 cognitive-assistance-chatbot

This will build the Docker image and start the app in a container. You can access the app at http://localhost:5000.

## Licensing
This chatbot is licensed under the OpenFabric license
