from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low
import requests
import json

class Question(Model):
    question : str
    chapter: int
    subject: str
    standard: int

class Text(Model):
    pdf: str
    success: bool
    question: str
    chapter: str
    subject: str
    standard: str


ncert = Agent(
    name="ncert",
    port=8001,
    seed="sigmar secret phrase",
    endpoint=["http://127.0.0.1:8001/submit"],
)

fund_agent_if_low(ncert.wallet.address())



@ncert.on_event("startup")
async def startup_handler(ctx: Context):
    ctx.logger.info("NCERT Agent Started")
    ctx.logger.info(f"{ncert.address}")

@ncert.on_query(model=Question, replies=Text)
async def question_handler(ctx: Context, sender: str, query: Question):
    try:
        ctx.logger.info(f"Question received: {query.question} {query.chapter} {query.subject} {query.standard}")
        api_url = "https://ncert-tutor-dev-dbkt.3.us-1.fl0.io/send-pdf-content"
        payload = {
            "standard": query.standard,
            "subject": query.subject,
            "chapter": query.chapter,
        }
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response = requests.post(api_url, json=payload, headers=headers)
        data = response.json()["content"]
        sender = "agent1qgpldhjj7vsp25xvnm7muw0dulzvhugf8pvpehaza82j4cw6dmc22x0m8y2"
        ctx.logger.info(f'{data}')

        await ctx.send(sender, Text(pdf=data, success=True, question=query.question, chapter=query.chapter, subject=query.subject, standard=query.standard))
    except Exception as e:
        await ctx.send(sender, Text(pdf=str(e), success=False, question=query.question, chapter=query.chapter, subject=query.subject, standard=query.standard))
        ctx.logger.info(e)
    return
if __name__ == "__main__":
    ncert.run()