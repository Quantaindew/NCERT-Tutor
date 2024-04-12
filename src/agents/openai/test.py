import os 
import requests

import json

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Retrieve the OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found in environment variables.")

print(OPENAI_API_KEY)
# Configuration for making requests to OPEN AI 
OPENAI_URL = "https://api.openai.com/v1/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}




prompt = """
A flower, also known as a bloom or blossom, is the reproductive structure found in flowering plants (plants of the division Angiospermae). Flowers consist of a combination of vegetative organs – sepals that enclose and protect the developing flower, petals that attract pollinators, and reproductive organs that produce gametophytes, which in flowering plants produce gametes. The male gametophytes, which produce sperm, are enclosed within pollen grains produced in the anthers. The female gametophytes are contained within the ovules produced in the carpels.

Most flowering plants depend on animals, such as bees, moths, and butterflies, to transfer their pollen between different flowers, and have evolved to attract these pollinators by various strategies, including brightly colored, conspicuous petals, attractive scents, and the production of nectar, a food source for pollinators.[1] In this way, many flowering plants have co-evolved with pollinators to be mutually dependent on services they provide to one another—in the plant's case, a means of reproduction; in the pollinator's case, a source of food.[2]

When pollen from the anther of a flower is deposited on the stigma, this is called pollination. Some flowers may self-pollinate, producing seed using pollen from a different flower of the same plant, but others have mechanisms to prevent self-pollination and rely on cross-pollination, when pollen is transferred from the anther of one flower to the stigma of another flower on a different individual of the same species. Self-pollination happens in flowers where the stamen and carpel mature at the same time, and are positioned so that the pollen can land on the flower's stigma. This pollination does not require an investment from the plant to provide nectar and pollen as food for pollinators.[3] Some flowers produce diaspores without fertilization (parthenocarpy). After fertilization, the ovary of the flower develops into fruit containing seeds.

Flowers have long been appreciated by humans for their beauty and pleasant scents, and also hold cultural significance as religious, ritual, or symbolic objects, or sources of medicine and food.
"""

context = '''    
    You are a helpful NCERT Tutor agent who will summarize a given chapter from NCERT and respond with a summary and a question bank with answers.
    
    Please follow these guidelines:
    1. Try to answer the question as accurately as possible, using only reliable sources like the ones provided as .
    2. Take in consideration the standard, subject, chapter, and question given.
    3. Provide a detailed summary of the chapter.
    4. Create a question bank with answers to the questions.
    5. Provide the information in the exact JSON format: {"summary": "summary", "question_bank": "question_1,question_2,...", answer_key:"answer_1,answer_2,..."}
        - summary is the summary of the chapter given
        - question bank is a newlined string of questions from the chapter
        - answer key is a newlined string of answers to the questions made from the chapter
    '''




import os
import requests

def query_openai_gpt(prompt):
   
    data = {
        "model": "gpt-4-turbo",
        "messages": [
            {"role": "system", "content": context},
            {"role": "user", "content": prompt}
        ]
    }

    # Make the POST request to the OpenAI API
    response = requests.post(OPENAI_URL, json=data, headers=HEADERS)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        response_json = response.json()
        # Retrieve the content from the first choice in the response
        return response_json["choices"][0]["message"]["content"]
    else:
        # Handle errors (e.g., invalid API key, rate limits)
        response.raise_for_status()

# Example usage:
# Ensure you have set the OPENAI_API_KEY environment variable before running this.
response = query_openai_gpt(prompt)
print(response)
