# Incognito Tab - Goa College of Engineering NCERT Tutor Video Demo

### You can watch a video demo of our project: [demo video](https://drive.google.com/drive/folders/175eGJjyQfFjJ36Qk0ACPx_CXWFQbdVnE?usp=drive_link)

## Vision of our project
- To simplify and improve learning attitude and aptitude
- To reach many students with all the help ncessary to ace thier exams
- To simplify and have the tedious tasks of memorizing and concept revision done easy with autonomous agents.

## Future scopes of your project
- To create a more conversational and seamless experience  by allowing the user to ask further questions about the chapter and get those included in the notes aswell by implementing the experimental [Dialogue module](https://github.com/Quantaindew/uAgents/blob/main/integrations/fetch-ai-engine/src/ai_engine/chitchat.py)
- To implement an additional feature that lets the user also practice questions with the help of flashcards , this will be an interactive experience   for the user to retain concepts and revise quicker .



  

## Project Information

### Abstract
Our project, NCERT Tutor, is designed to simplify the learning process by providing a personalized tutoring experience. It asks the user for their class, subject, and chapter they want to learn or have a doubt in, then fetches the corresponding chapter PDF from the NCERT website, summarizes the content, and creates notes along with important questions through a seamless interaction enabled via delta v. The agents in our project deployed on Agentverse is fully operational through Delta V.

### Agents used in our Project, aligning with Vision of Incognito Tab
- **Interact Agent**
  - The first pillar and the initiator of the entire sequence of the workflow based on the user input done through delta v.
  - Knows the preferences of the user based on previous interactions with agents
  - Aims to maximize the educational value of the user while also providing the best options towards user query
``question.py``
- **NCERT Content Fetcher**
  - The second pillar who fetches the knowledge necessary in the form of chapter PDF from the NCERT website database based on user input.
``ncertagent.py``
- **Content Summarizer**
  - The third pillar who summarizes the fetched content to provide a concise overview.
``openai.py``
-**Conclusive agent**
- The final pillar of our command chain who completes the entire flow giving the user the entire analysis of the conversation, doubts and quizes done before thus concluding the pursuits of user with a fulfilling experience.
``end.py``

### Sample Flow of our NCERT Tutor
1. User inputs their class, subject, and chapter.
2. User Agent captures the input and calls the NCERT Content Fetcher to retrieve the chapter PDF.
3. NCERT Content Fetcher fetches the PDF and passes it to the Content Summarizer.
4. Content Summarizer summarizes the content and passes it to the Note Creator.
5. Note Creator creates notes based on the summary and presents them to the user.

## Content of PPt:
attached ppt [[here](https://drive.google.com/file/d/1iGu_jOVT7fEgck_SGkd_uoLkFQtYrsbZ/view?usp=sharing)] 



## Technology Stack
- Python
- Fetch.ai
- uAgent Library
- Agentverse

## Getting Started

### Installation
1. Clone the repository:

```
git clone https://github.com/Quantaindew/NCERT-Tutor.git
```

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
cd src/uagents/ncert
poetry shell
python ncertagent.py
```


```
cd src/uagents/openai
poetry shell
python openai.py 
```
###
Reminder: the openai agent requires a gpt4 api key which needs to be put into the .env file in the same directory as the agent (you will find a .env-template file)
###

```
cd src/uagents/ending
poetry shell
python openai.py 
```
```
cd src/uagents/conversation
poetry shell
python question.py
```
reminder: for the conversation agent demo to run locally , you will need to uncomment the hardcoded query 👇 in the ``` question.py``` file .
``` python
@agent.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info("Question System Agent Started")
    ctx.logger.info(f"{agent.address}")
    await #ctx.send("agent1qvwqu6a0km09mq4f6j6kmke9smswmgcergmml9a54av9449rqtmmxy4qwe6", Question(question = "Can you provide a summary of the chapter 'colors' from standard 3 English?", chapter = 101, subject = "english", standard = 3, sender = agent.address))
    
# uncomment this ☝️ query to run the demo locally.

```



Run the above commands in order in different terminals
