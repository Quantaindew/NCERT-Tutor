import json
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import requests
from PyPDF4 import PdfFileReader

from io import BytesIO


app = FastAPI()

class Request(BaseModel):
    standard: int
    subject: str
    chapter: int

def generate_url(class_num, subject, chapter_num):
    class_mapping = {9: 'ie', 10: 'je',8:'he',7:'ge',6:'fe',5:'ee',4:'de',3:'ce',2:'be',1:'ae'}
    subject_mapping = {
        'science': 'sc', 
        'social science': 'ss', 
        'english': {
            1: 'mr',
            2: 'mr',
            3: 'sa',
            4: 'en',
            5: 'en',
            6: 'hl',
            7: 'hc',
            8: 'hd',
            9: 'be',
            10: 'ff',
        },
        'evs':'ap',
    }
    
    class_str = class_mapping.get(class_num, '')
    subject_str = subject_mapping.get(subject.lower(), '')
    
    # If the subject is English, get the specific code for the class
    if subject.lower() == 'english':
        subject_str = subject_mapping['english'].get(class_num, '')
    

    if class_str and subject_str:
        url = f"https://ncert.nic.in/textbook/pdf/{class_str}{subject_str}{chapter_num}.pdf"
        return url
    else:
        return "Invalid input"

@app.post('/send-pdf-content')
def generate_url_api(request_data: Request):
    try:
        url = generate_url(request_data.standard, request_data.subject, request_data.chapter)
        if not url:
            raise ValueError("Generated URL is empty or invalid.")
        
        # Download the PDF
        response = requests.get(url)
        response.raise_for_status()

        # Read the PDF
        reader = PdfFileReader(BytesIO(response.content))

        # Extract the text
        text = ""
        for page in range(reader.getNumPages()):
            text += reader.getPage(page).extractText()

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return {"content": text}
@app.get('/')
def home():
    instructions = """
    # Usage instructions for the endpoint 
    1. Open Postman.
    2. Set the HTTP method to POST.
    3. Enter the URL of your Flask server. If it's running locally on the default port, the URL will be http://localhost:5000/generate_url.
    4. Go to the "Body" tab, select "raw", and then select "JSON" from the dropdown menu.
    5. Enter a JSON object with the keys 'class', 'subject', and 'chapter'. For example:
    {
        "class": 10,
        "subject": "maths",
        "chapter": 2
    }
    6. Click "Send" to make the request.
    """
    return instructions



