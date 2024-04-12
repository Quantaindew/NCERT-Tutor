
# Here we demonstrate how an agent can respond to plain text questions with data from an AI model and convert it into a machine readable format.
# Note: the AI model used here is not actually able to verify its information and is not guaranteed to be correct. The purpose of this example is to show how to interact with such a model.
#
# In this example we will use:
# - 'agent': this is your instance of the 'Agent' class that we will give an 'on_interval' task
# - 'ctx': this is the agent's 'Context', which gives you access to all the agent's important functions
# - 'requests': this is a module that allows you to make HTTP requests
#
# To use this example, you will need to provide an API key for OPEN AI: https://platform.openai.com/account/api-keys
# You can define your OPENAI_API_KEY value in the .env file

import os 
import requests
import uagents
from uagents import Agent, Context, Model

if OPENAI_API_KEY == "YOUR_OPENAI_API_KEY":
    raise Exception("You need to provide an API key for OPEN AI to use this example")

# Configuration for making requests to OPEN AI 
OPENAI_URL = "https://api.openai.com/v1/chat/completions"
MODEL_ENGINE = "gpt-4-turbo"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}



class Error(Model):
    text: str

class Question(Model):
    question: str
    chapter: str
    subject: str
    standard: str

class Text(Model):
    pdf: str
    success: bool
    question: Question

#class based on {"summary": "summary", "question_bank": ["question_1","question_2",...], answer_key:["answer_1","answer_2",...]}
class Response(Model):
    summary: str
    question_bank: list
    answer_key: list

# Send a prompt and context to the AI model and return the content of the completion
def get_completion(context: str, prompt: str):
    data = {
        "model": MODEL_ENGINE,
        "response_format": "json",
        "messages": [
            {"role": "system", "content": context},
            {"role": "user", "content": prompt},
        ]
    }

    try:
        response = requests.post(OPENAI_URL, headers=HEADERS, data=json.dumps(data))
        messages = response.json()['choices']
        message = messages[0]['message']['content']
    except Exception as ex:
        return None

    print("Got response from AI model: " + message)
    return message


# Instruct the AI model to retrieve data and context for the data and return it in machine readable JSON format
def get_data(ctx: Context, request: str):
    context = '''    
    You are a helpful NCERT Tutor agent who will summarize a given chapter from NCERT and respond with a summary and a question bank with answers.
    
    Please follow these guidelines:
    1. Try to answer the question as accurately as possible, using only reliable sources like the ones provided as .
    2. Take in consideration the standard, subject, chapter, and question given.
    3. Provide a detailed summary of the chapter.
    4. Create a question bank with answers to the questions.
    5. Provide the information in the exact JSON format: {"summary": "summary", "question_bank": ["question_1","question_2",...], answer_key:["answer_1","answer_2",...]}
        - summary is the summary of the chapter given
        - question bank is a list of questions from the chapter
        - answer key is a list of answers to the questions made from the chapter
    '''

    response = get_completion(context, request)

    try:
        ## try to convert response to json
        data = json.loads(response)
        ##return json data
        return data
    except Exception as ex:
        ctx.logger.exception(f"An error occurred retrieving data from the AI model: {ex}")
        return Error(text="Sorry, I wasn't able to answer your request this time. Feel free to try again.")

# Message handler for data requests sent to this agent
@agent.on_message(model=Text)
async def handle_request(ctx: Context, request: Text):
    ctx.logger.info(f"Got request from {sender}: {request.success}")
    request_dict = request.to_dict()
    # Serialize the dictionary to a JSON string
    request_json = json.dumps(request_dict)
    response = get_data(ctx, f"{request_json}") 
    sender = ""
    await ctx.send(sender, Response(summary=response.summary, question_bank=response.question_bank, answer_key=response.answer_key))
    