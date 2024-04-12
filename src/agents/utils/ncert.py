from flask import Flask, request, jsonify

app = Flask(__name__)

def generate_url(class_num, subject, chapter_num):
    class_mapping = {9: 'ie', 10: 'ke'}
    subject_mapping = {'science': 'sc', 'maths': 'mh'}
    
    class_str = class_mapping.get(class_num, '')
    subject_str = subject_mapping.get(subject.lower(), '')
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

if __name__ == '__main__':
    app.run(debug=True)
