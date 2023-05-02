import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time
from transformers import BertForQuestionAnswering, BertTokenizer, pipeline

model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

############################################################
# Use BERT Pre-trained Model
############################################################
def generate_answer(text):

    question, context = text.split(' ||| ')
    
    answer = nlp({
        'question': question,
        'context': context
    })['answer']
    
    return answer


############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    # TODO Add code here
    pass


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    for text in request.text:
        response = generate_answer(text)
        output.append(response)

    return SimpleText(dict(text=output))
