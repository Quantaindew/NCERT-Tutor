 
# Here we demonstrate how we can create a question reading system agent that is compatible with DeltaV
    
# After running this agent, it can be registered to DeltaV on Agentverse Services tab. For registration you will have to use the agent's address
 
# Import required libraries
import requests
from uagents import Model, Protocol, Agent, Context
from ai_engine import UAgentResponse, UAgentResponseType
from uagents.setup import fund_agent_if_low

agent = Agent(
    name="Question System", 
    seed="your_agent_seed_here", 
    port=8001, 
    endpoint="http://localhost:8001/submit"
    )

# Define Question Reading Model
class Question(Model):
    question : str
    chapter: str
    subject: str
    standard: str

class ChapterUrl(Model):
    url: str 

# Define Protocol for question reading system
question_protocol = Protocol("Question System")
 
fund_agent_if_low(ncert.wallet.address())

# Define a handler for the Question system protocol
@question_protocol.on_message(model=Question, replies = UAgentResponse)
async def on_question_request(ctx: Context, sender: str, msg: Question):
    #Printing the question response on logger
    ctx.logger.info(f"Received question request from {sender} with title: {msg.question}")
    chapter_url = await ctx.send("agent1qvwqu6a0km09mq4f6j6kmke9smswmgcergmml9a54av9449rqtmmxy4qwe6", Question(question = msg.question, chapter = msg.chapter, subject = msg.subject, standard = msg.standard))
    await ctx.send(dasdas,ChapterUrl(url = chapter_url))
    #Creating hyperlink and sending final response to the DeltaV GUI
    message = f"you asked for help with chapter: {msg.chapter} from {msg.standard} in {msg.subject}"
    await ctx.send(sender, UAgentResponse(message = message, type = UAgentResponseType.FINAL))
 
 
# Include the Generate Question protocol in your agent
agent.include(question_protocol)


if __name__ == "__main__":
    agent.run()