# Incognito Tab - Goa College of Engineering NCERT Tutor Video Demo

You can watch a video demo of our project: [Google Drive Video Folder](<insert link here>)

## Vision of our project
- To simplify and improve learning attitude and aptitude
- To reach many students with all the help ncessary to ace thier exams
- To simplify and have the tedious tasks of memorizing done easy with autonomous agents.
  

## Project Information

### Abstract
Our project, NCERT Tutor, is designed to simplify the learning process by providing a personalized tutoring experience. It asks the user for their class, subject, and chapter they want to learn or have a doubt in, fetches the corresponding chapter PDF from the NCERT website, summarizes the content, and creates notes along with important questions through a seamless interaction enabled via delta v. The agents in our project deployed on Agentverse is fully operational through Delta V.

### Agents used in our Project, aligning with Vision of Incognito Tab
- **User Agent**
  - Interacts with other agents based on user input query
  - Knows the preferences of the user based on previous interactions with agents
  - Aims to maximize the educational value of the user while also providing the best options towards user query
- **NCERT Content Fetcher**
  - Fetches the chapter PDF from the NCERT website based on user input
- **Content Summarizer**
  - Summarizes the fetched content to provide a concise overview


### Sample Flow of our NCERT Tutor
1. User inputs their class, subject, and chapter.
2. User Agent captures the input and calls the NCERT Content Fetcher to retrieve the chapter PDF.
3. NCERT Content Fetcher fetches the PDF and passes it to the Content Summarizer.
4. Content Summarizer summarizes the content and passes it to the Note Creator.
5. Note Creator creates notes based on the summary and presents them to the user.

## Screenshots
Screenshots will be added here.

## Technology Stack
- Python
- Fetch.ai
- uAgent Library
- Agentverse

## Getting Started

### Installation
1. Clone the repository:

 ```git clone https://github.com/Quantaindew/NCERT-Tutor.git```

2. Install the required dependencies:

```
cd NCERT-Tutor
```

3.Initialize the environment:

```
poetry install
poetry shell
```

4.Running the ecosystem of the agent :

```
cd src/conversation
python question.py
```

```
cd src/ncert
python ncertagent.py
```

```
cd src/openai
python openai.py 
```
Run the above commands in order in different terminals
