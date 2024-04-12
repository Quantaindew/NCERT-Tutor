 
# Here we demonstrate how we can create a news reading system agent that is compatible with DeltaV
    
# After running this agent, it can be registered to DeltaV on Agentverse Services tab. For registration you will have to use the agent's address
 
# Import required libraries
import requests
from ai_engine import UAgentResponse, UAgentResponseType
 
# Define Question Reading Model
class Question(Model):
    news : str
 
# Define Protocol for news reading system
news_protocol = Protocol("Question System")
 
# Define a handler for the Question system protocol
@news_protocol.on_message(model=Question, replies = UAgentResponse)
async def on_news_request(ctx: Context, sender: str, msg: Question):
    #Printing the news response on logger
    ctx.logger.info(f"Received news request from {sender} with title: {msg.news}")
    #Creating hyperlink and sending final response to the DeltaV GUI
    message = f"<a href='{msg.news}'>YOUR NEWS CONTENT</a>"
    await ctx.send(sender, UAgentResponse(message = message, type = UAgentResponseType.FINAL))
 
 
# Include the Generate Question protocol in your agent
agent.include(news_protocol)