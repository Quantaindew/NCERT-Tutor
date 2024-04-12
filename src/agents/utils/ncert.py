from flask import Flask, request, jsonify

app = Flask(__name__)

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
        }
    }
    
    class_str = class_mapping.get(class_num, '')
    subject_str = subject_mapping.get(subject.lower(), '')
    
    # If the subject is English, get the specific code for the class
    if subject.lower() == 'english':
        subject_str = subject_mapping['english'].get(class_num, '')
    
    chapter_str = str(chapter_num).zfill(2) # pad with zeros to make it 2 digits

    if class_str and subject_str:
        url = f"https://ncert.nic.in/textbook/pdf/{class_str}{subject_str}1{chapter_str}.pdf"
        return url
    else:
        return "Invalid input"

@app.route('/generate_url', methods=['POST'])
def generate_url_api():
    data = request.get_json()
    class_num = data.get('class')
    subject = data.get('subject')
    chapter_num = data.get('chapter')
    
    url = generate_url(class_num, subject, chapter_num)
    return jsonify({'url': url})

@app.route('/', methods=['GET'])
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


if __name__ == '__main__':
    app.run(debug=True,port=8080)
