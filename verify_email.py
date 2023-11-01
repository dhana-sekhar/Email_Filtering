import openai
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts.prompt import PromptTemplate
import os
os.environ['OPENAI_API_KEY'] = 


openai.api_key = 


with open('email1.txt') as f:
    paragraph1 = f.read()

with open('attachment1.txt') as f: 
    paragraph2 = f.read()

name = "user name"
email = "username@gmail.com"
fin = "ASDF12345"

template = f"""you are a q&a bot now answer the following from the given two paragra
paragraph1: {paragraph1}\n\nparagraph2: {paragraph2}\n\n

paragraph1 is the email intended to send to the policy holder

now answer me the follwoing question like in the example

examples:
what is the policy no:  <policy number>
what is the fin no: <policy holder fin number>
what is the policy holder name: <policy holder name>
what is the email address of the policy holder: < policy holder email>
does both the paragraphs belongs to the same person: <yes/no>
what is the sentiment of the two paragraphs: <paragraph1: (neutral/anger/happy/sad) paragraph2:(neutral/anger/happy/sad)

you should answer the following questions as in the example now i want you to answer only from the paragraph, if you dont know the answer say that you dont know.


here are my questions

what is the policy no:  
what is the fin no: 
what is the policy holder name: 
what is the email address of the policy holder: 
does both the paragraphs belongs to the same person: 
what is the sentiment of the two paragraphs: 
"""

template1 = f"""you are a q&a bot now answer the following from the given two paragra
paragraph1: {paragraph1}\n\nparagraph2: {paragraph2}\n\n

paragraph1 is the email intended to send to the policy holder

from the database we know the name, email, fin no as ground truth about the policy holder
Name: {name}, email: {email}, fin no: {fin}


now answer me the follwoing question like in the example

examples:
what is the policy no:  <policy number>
what is the fin no: <policy holder fin number>
what is the policy holder name: <policy holder name>
what is the email address of the policy holder: < policy holder email>
does both the paragraphs belongs to the same person names: <yes/no>
does both the paragraphs belongs to the same person email: <yes/no>
does both the paragraphs belongs to the same person fin: <yes/no>
does both the paragraphs belongs to the same person: <check if both email and name are yes/no then you can answer as yes/no>
what is the sentiment of the two paragraphs: <paragraph1: (neutral/anger/happy/sad) paragraph2:(neutral/anger/happy/sad)

you should answer the following questions as in the example now i want you to answer only from the paragraphs not from the data base, if you dont know the answer from the paragraph or if you couldnt find the answer from the paragraph say that you dont know.


here are my questions

what is the policy no:  
what is the fin no: 
what is the policy holder name: 
what is the email address of the policy holder: 
does both the paragraphs belongs to the same person names: 
does both the paragraphs belongs to the same person email: 
does both the paragraphs belongs to the same person fin: 
does both the paragraphs belongs to the same person: 
what is the sentiment of the two paragraphs: 
"""


from langchain.chains import LLMChain
llm = OpenAI(model_name="gpt-3.5-turbo-16k")
print(template1)
print(llm(template1))
